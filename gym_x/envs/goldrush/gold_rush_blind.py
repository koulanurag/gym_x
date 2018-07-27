import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)


class GoldRushB(gym.Env):
    """
    A simple synthetic environment.
    The agent need to follow a fixed endless path without paying any attention to the observations.

    Observation Space : Continuous
    Action Space : Discrete
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.obs_size = 1
        self._valid_observations = np.array([[float(_) for _ in ('{0:0' + str(self.obs_size) + 'b}').format(i)]
                                             for i in range(2 ** self.obs_size)])
        self.total_actions = 4
        self.action_space = spaces.Discrete(self.total_actions)
        self.obs_mode_map = {i: i % self.total_actions for i in range(len(self._valid_observations))}
        self._mode_steps = [2, 3, 2, 3]  # sum =10

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
        # done = True if (reward == 0 or self._clock % self.spec.max_episode_steps == 0) else False
        info = {'desired_action': self.get_desired_action()}
        return next_obs, reward, done, info

    def _get_observation(self):
        return self.np_random.randn(self.obs_size)

    def _update_mode(self):
        if self._curr_mode_steps >= self._mode_steps[self._curr_mode]:
            self._curr_mode_steps = 0
            self._curr_mode = (self._curr_mode + 1) % len(self._mode_steps)

    def get_desired_action(self):
        return self._curr_mode

    def reset(self):
        self._clock = 0
        self._curr_mode_steps = 0
        obs = self._get_observation()
        self._curr_mode = 0
        return obs

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        seed2 = seeding.hash_seed(seed1 + 1) % 2 ** 31
        return [seed1, seed2]

    def render(self, mode="human", close=False):
        pass
