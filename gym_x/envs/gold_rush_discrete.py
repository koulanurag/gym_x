import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np


class GoldRushD(gym.Env):
    """
    A simple synthetic environment having multiple doors.
    There are specific no. of steps required to be made once you reach a door to acquire the gold.
    Each observation has a unique action and no. of steps.
    Ideal policy would take corresponding no. of steps for each observation and will ignore observations
    while taking those steps.

    Observation Space : Discrete
    Action Space : Discrete
    """

    def __init__(self):
        self.obs_size = 2
        self._valid_observations = np.array([[float(_) for _ in ('{0:0' + str(self.obs_size) + 'b}').format(i)]
                                             for i in range(2 ** self.obs_size)])
        self.total_actions = 4
        self.action_space = spaces.Discrete(self.total_actions)
        self.obs_mode_map = {i: i % self.total_actions for i in range(len(self._valid_observations))}
        self._mode_steps = [2, 3, 2, 3]

        self._clock = None
        self._curr_mode_steps = None
        self._curr_mode = None
        self.seed()

    def step(self, action):
        if action >= self.total_actions:
            raise ValueError("action must be one of %r" % range(self.total_actions))

        reward = 1 if action == self.get_desired_action() else 0

        self._curr_mode_steps += 1
        self._clock += 1
        next_obs = self._get_observation()
        self._update_mode()
        done = True if self._clock % self.spec.max_episode_steps == 0 else False
        info = {'desired_action': self.get_desired_action()}
        return next_obs, reward, done, info

    def _get_observation(self):
        self._curr_obs_index = self.np_random.choice(range(len(self._valid_observations)))
        return np.array(self._valid_observations[self._curr_obs_index])

    def _update_mode(self):
        if self._curr_mode_steps >= self._mode_steps[self._curr_mode]:
            self._curr_mode_steps = 0
            self._curr_mode = self.obs_mode_map[self._curr_obs_index]

    def get_desired_action(self):
        return self._curr_mode

    def reset(self):
        self._clock = 0
        self._curr_mode_steps = 0
        obs = self._get_observation()
        self._curr_mode = self.obs_mode_map[self._curr_obs_index]
        return obs

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        seed2 = seeding.hash_seed(seed1 + 1) % 2 ** 31
        return [seed1, seed2]
