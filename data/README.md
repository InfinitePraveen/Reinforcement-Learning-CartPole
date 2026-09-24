# Data

This project uses the Gymnasium CartPole simulation environment instead of a static downloaded dataset.

At every environment step, CartPole generates:

- Observation: cart position, cart velocity, pole angle and pole angular velocity
- Action: move the cart left or right
- Reward: positive reward for keeping the pole balanced
- Termination signal: indicates when the episode ends

No large dataset is stored in this folder, which keeps the project lightweight for CPU-only systems.
