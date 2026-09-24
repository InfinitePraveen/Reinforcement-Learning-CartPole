from pathlib import Path
import numpy as np
import gymnasium as gym
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "q_table.npy"

BINS = (8, 8, 12, 12)
STATE_LIMITS = np.array([2.4, 3.0, 0.2095, 3.5], dtype=np.float32)

if MODEL_PATH.exists():
    Q_TABLE = np.load(MODEL_PATH)
else:
    Q_TABLE = np.zeros(BINS + (2,), dtype=np.float32)

env = None
observation = None
total_reward = 0.0
steps = 0

def discretize(obs):
    clipped = np.clip(obs, -STATE_LIMITS, STATE_LIMITS)
    scaled = (clipped + STATE_LIMITS) / (2 * STATE_LIMITS)
    indices = (scaled * np.array(BINS)).astype(int)
    return tuple(np.clip(indices, 0, np.array(BINS) - 1))

def state_payload(action=None, done=False):
    if observation is None:
        return {"started": False}
    return {
        "started": True,
        "observation": [round(float(x), 5) for x in observation],
        "action": action,
        "reward": total_reward,
        "steps": steps,
        "done": done,
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/api/reset")
def reset():
    global env, observation, total_reward, steps
    if env is not None:
        env.close()
    env = gym.make("CartPole-v1")
    observation, _ = env.reset(seed=42)
    total_reward = 0.0
    steps = 0
    return jsonify(state_payload())

@app.post("/api/step")
def step():
    global observation, total_reward, steps, env
    if env is None or observation is None:
        return jsonify({"error": "Start an episode first."}), 400

    state = discretize(observation)
    action = int(np.argmax(Q_TABLE[state]))
    observation, reward, terminated, truncated, _ = env.step(action)
    total_reward += float(reward)
    steps += 1
    done = bool(terminated or truncated)

    if done:
        observation = np.asarray(observation)

    return jsonify(state_payload(action=action, done=done))

@app.get("/api/status")
def status():
    return jsonify({
        "model": str(MODEL_PATH.name),
        "model_loaded": MODEL_PATH.exists(),
        "q_table_shape": list(Q_TABLE.shape),
        "algorithm": "Tabular Q-learning",
    })

@app.post("/api/close")
def close():
    global env, observation
    if env is not None:
        env.close()
    env = None
    observation = None
    return jsonify({"closed": True})

if __name__ == "__main__":
    app.run(debug=True)
