import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import math

logger = logging.getLogger(__name__)


class TomitaF(gym.Env):
    """
        Tomita Grammer : the difference between number of 1s and number of 0s is a multiple of 3
        Alphabet : {0,1}
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.alphabet = [0, 1]

        self.total_actions = 2  # 0: Reject ; 1: Accept
        self.accept_action = 1
        self.reject_action = 0

        self.action_space = spaces.Discrete(self.total_actions)

        self._clock = None
        self.seed()

        self.min_steps = 3
        self.max_steps = 30

        self.enc = True
        self.all_observations = []
        self._enforce_valid_string = True

    def step(self, action):
        if action >= self.total_actions:
            raise ValueError("action must be one of %r" % range(self.total_actions))

        self._clock += 1
        done = True if self._clock >= self.max_episode_steps else False
        reward = 1 if done and self.get_desired_action() == action else 0
        next_obs = self._get_observation() if not done else self.__get_random_observation()
        info = {'desired_action': self.get_desired_action() if not done else None}
        return next_obs, reward, done, info

    def __get_random_observation(self):
        return self.np_random.choice(self.alphabet)

    def _get_observation(self):
        if self._enforce_valid_string:
            obs = self._generated_obs[self._clock]
        else:
            obs = self.np_random.choice(self.alphabet, p=self._probs)
        self.all_observations.append(obs)
        self._counts[obs] += 1
        return np.array([obs])

    def get_desired_action(self):
        return self.accept_action if self._enforce_valid_string or self.is_string_valid() else self.reject_action

    def is_string_valid(self):
        return (self._counts[1] - self._counts[0]) % 3 == 0

    def reset(self):
        self._clock = 0
        self._probs = self.np_random.random_sample()
        self._probs = [self._probs, 1 - self._probs]
        self.np_random.shuffle(self._probs)

        self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
        self._enforce_valid_string = (self.np_random.random_sample() <= 0.25)
        if self._enforce_valid_string:
            zero_count = self.np_random.randint(0, self.max_episode_steps // 2)
            one_count = zero_count + 3 * self.np_random.randint(1, 10)
            self._generated_obs = [1 for _ in range(one_count)]
            self._generated_obs += [0 for _ in range(zero_count)]
            self.np_random.shuffle(self._generated_obs)
            self.max_episode_steps = len(self._generated_obs)

        self.all_observations = []
        self._counts = [0, 0]  # each alphabet count
        obs = self._get_observation()

        return obs

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        seed2 = seeding.hash_seed(seed1 + 1) % 2 ** 31
        return [seed1, seed2]

    def render(self, mode="human", close=False):
        pass
