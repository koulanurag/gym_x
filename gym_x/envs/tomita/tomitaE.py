import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)


class TomitaE(gym.Env):
    """
        Tomita Grammer : even number of 0's and even number of 1s
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

        self.min_steps = 1
        self.max_steps = 50

        self.enc = True
        self.all_observations = []
        self._enforce_valid_string = True

        self._counts = [0, 0]  # each alphabet count

    def step(self, action):
        if action >= self.total_actions:
            raise ValueError("action must be one of %r" % range(self.total_actions))

        self._clock += 1
        done = True if self._clock >= self.max_episode_steps else False
        reward = 1 if done and self.get_desired_action() == action else 0
        next_obs = self._get_observation() if not done else self._get_random_observation()
        info = {'desired_action': self.get_desired_action() if not done else None}
        return next_obs, reward, done, info

    def _get_random_observation(self):
        return self.np_random.choice(self.alphabet)

    def _get_observation(self):
        if self._enforce_valid_string:
            obs = self._generated_obs[self._clock]
            # if self._clock > 0:
            #     prob = [self._counts[1] / sum(self._counts), self._counts[0] / sum(self._counts)]
            # else:
            #     prob = [0.5, 0.5]
            # obs = self.np_random.choice(self.alphabet, p=prob)
        else:
            obs = self.np_random.choice(self.alphabet, p=self._probs)

        self.all_observations.append(obs)
        self._counts[obs] += 1
        return np.array([obs])

    def get_desired_action(self):
        return self.accept_action if self.is_string_valid() else self.reject_action

    def is_string_valid(self):
        return self._counts[0] % 2 == 0 and self._counts[1] % 2 == 0

    def reset(self):
        self._clock = 0

        self._enforce_valid_string = (self.np_random.random_sample() <= 0.4)  # Equally sample Accept and Reject
        if self._enforce_valid_string:
            obs = self.np_random.choice([0, 1])

            obs_count = self.np_random.choice(range(2, self.max_steps, 2))
            non_obs_count = self.np_random.choice(range(0, self.max_steps - obs_count + 1, 2))

            self._generated_obs = [obs] * obs_count
            self._generated_obs += [1 - obs] * non_obs_count
            self.np_random.shuffle(self._generated_obs)

            self.max_episode_steps = len(self._generated_obs)
        else:
            self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))

        self._probs = self.np_random.random_sample()
        self._probs = [self._probs, 1 - self._probs]
        self.np_random.shuffle(self._probs)

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
