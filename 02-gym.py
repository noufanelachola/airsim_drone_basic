import gymnasium as gym

env = gym.make('CartPole-v1', render_mode="human")

observation, info = env.reset()

for i in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, terminated, trunacated, info = env.step(action)

    if terminated or trunacated:
        observation, info = env.reset()

env.close()
