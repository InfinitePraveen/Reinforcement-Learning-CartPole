# Reinforcement Learning CartPole

A lightweight, notebook-first reinforcement learning project that trains an agent to balance a pole on the CartPole environment using tabular Q-learning.

The project is designed for CPU-only computers and keeps the training workflow small enough for a normal laptop. The trained Q-table is saved and used by a Flask web application so the learned policy can be demonstrated interactively.

## Project Highlights

- Q-learning from scratch with a compact discretized state space
- OpenAI Gym-compatible CartPole environment through Gymnasium
- CPU-only training; no GPU required
- Small model artifact (`models/q_table.npy`)
- Notebook-based experimentation and evaluation
- Flask web demo with an animated CartPole-style visualization
- GitHub and LinkedIn links included in the web app
- No `src/`, preprocessing package, or unnecessary module scripts

## Requirements

Python 3.12 is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the notebooks

Start Jupyter:

```bash
jupyter notebook
```

Run:

1. `notebooks/01_environment_setup.ipynb`
2. `notebooks/02_q_learning_training.ipynb`
3. `notebooks/03_evaluate_agent.ipynb`

The training notebook saves the learned Q-table to:

```text
models/q_table.npy
```

## Run the Flask web app

After generating the model:

```bash
python app.py
```

Open the local address shown by Flask in your browser.

The demo lets you start an episode, step the trained agent through the environment, reset it, and view the current reward/step count.

## Repository Structure

```text
Reinforcement-Learning-CartPole/
├── data/
│   └── README.md
├── models/
│   ├── README.md
│   └── q_table.npy
├── notebooks/
│   ├── 01_environment_setup.ipynb
│   ├── 02_q_learning_training.ipynb
│   └── 03_evaluate_agent.ipynb
├── static/
│   ├── app.js
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── CHANGELOG.md
├── CONTRIBUTE.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Algorithm

CartPole has a continuous state space, while tabular Q-learning needs discrete states. The project therefore discretizes:

- Cart position
- Cart velocity
- Pole angle
- Pole angular velocity

The agent selects between the two CartPole actions using an epsilon-greedy policy.

The Q-learning update is:

```text
Q(s,a) ← Q(s,a) + α [r + γ max Q(s',a') − Q(s,a)]
```

where `α` is the learning rate and `γ` is the discount factor.

## Dataset / Environment

CartPole is a simulation environment rather than a conventional downloaded dataset. The environment generates observations, actions and rewards during interaction. This repository therefore does not download a large dataset.

## Author

**Praveen Kumar**

- GitHub: https://github.com/InfinitePraveen
- LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## License

MIT License
