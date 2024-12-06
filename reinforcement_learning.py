from blackjack import BlackJackGame
import os
from TensorboardCallback import TensorboardCallback
from stable_baselines3 import A2C, PPO


def main():
    logdir = "logs"

    if not os.path.exists(logdir):
        os.makedirs(logdir)

    RECORDING = 500
    TRINING_TIMESTEPS = 100000

    def train(model, env, log_name, log_interval=1):
        env.hard_reset()
        model = model("MlpPolicy", env, tensorboard_log=logdir,
                      learning_rate=0.001)
        model.learn(total_timesteps=TRINING_TIMESTEPS,
                    callback=TensorboardCallback(),
                    tb_log_name=log_name, log_interval=log_interval)
        return model

    normal_env = BlackJackGame(mute=True, num_decks=1, card_count=False,
                               record_limit=RECORDING)
    train(A2C,
          normal_env,
          "A2C_without_counting_cards",
          log_interval=100)

    train(PPO,
          normal_env,
          "PPO_without_counting_cards")

    counting_env = BlackJackGame(mute=True, num_decks=1, card_count=True,
                                 record_limit=RECORDING)
    train(A2C,
          counting_env,
          "A2C_with_counting_cards",
          log_interval=100)

    ppo_counting = train(PPO,
                         counting_env,
                         "PPO_with_counting_cards")

    model, env = ppo_counting, counting_env
    for episode in range(10):
        print("------------------------------------------------------")
        state = counting_env.reset()[0]
        done = False
        episode_reward = 0

        env.render()
        while not done:
            action, _ = model.predict(state, deterministic=True)
            state, reward, done, truncated, _ = env.step(action)
            episode_reward += reward
            env.render()

        if episode_reward == 1:
            print(f"Player won this round.")
        if episode_reward == -1:
            print(f"Player lost this round.")
        if episode_reward == 0:
            print(f"This round was a tie.")
