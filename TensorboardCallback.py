from stable_baselines3.common.callbacks import BaseCallback


class TensorboardCallback(BaseCallback):
    """
    Custom callback for plotting additional values in tensorboard.
    """

    def __init__(self, verbose=0):
        super().__init__(verbose)

    def _on_step(self) -> bool:
        # Log scalar value (here a random variable)
        dummy_vec_env = self.model.get_env()
        env = dummy_vec_env.envs[0]
        runs = max(env.unwrapped.wins+env.unwrapped.losses+env.unwrapped.ties,
                   env.unwrapped.record_limit)
        win_rate = env.unwrapped.wins / runs
        loss_rate = env.unwrapped.losses / runs
        avg_reward = (env.unwrapped.wins - env.unwrapped.losses) / runs
        self.logger.record("rates/loss_rate", loss_rate)
        self.logger.record("rates/win_rate", win_rate)
        self.logger.record("rates/avg_reward", avg_reward)
        return True
