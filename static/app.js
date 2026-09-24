const startBtn = document.getElementById("startBtn");
const stepBtn = document.getElementById("stepBtn");
const resetBtn = document.getElementById("resetBtn");
const stepsEl = document.getElementById("steps");
const rewardEl = document.getElementById("reward");
const actionEl = document.getElementById("action");
const statusEl = document.getElementById("status");
const cart = document.getElementById("cart");
const pole = document.getElementById("pole");

async function post(url) {
    const response = await fetch(url, { method: "POST" });
    return response.json();
}

function update(data) {
    if (data.error) {
        statusEl.textContent = data.error;
        return;
    }
    if (!data.started) return;

    stepsEl.textContent = data.steps;
    rewardEl.textContent = Number(data.reward).toFixed(0);
    actionEl.textContent = data.action === null || data.action === undefined ? "-" : data.action;
    statusEl.textContent = data.done ? "Episode ended" : "Running";

    const position = data.observation[0];
    const angle = data.observation[2];
    const x = Math.max(-43, Math.min(43, position / 2.4 * 43));
    cart.style.left = `calc(50% + ${x}px)`;
    pole.style.transform = `rotate(${angle * 180 / Math.PI}deg)`;
    stepBtn.disabled = data.done;
}

startBtn.addEventListener("click", async () => {
    const data = await post("/api/reset");
    update(data);
    stepBtn.disabled = false;
});

stepBtn.addEventListener("click", async () => {
    const data = await post("/api/step");
    update(data);
});

resetBtn.addEventListener("click", async () => {
    const data = await post("/api/reset");
    update(data);
    stepBtn.disabled = false;
});
