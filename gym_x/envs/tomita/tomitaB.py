import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)


class TomitaB(gym.Env):
    """
        Tomita Grammer : (10)*
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

        self._counts = [0, 0]
        self.enc = True
        self.all_observations = []
        self._enforce_valid_string = True

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
        if self._enforce_valid_string or (self._partial_valid_string and self._partial_valid_len >= self._clock):
            obs = (1 - self.all_observations[-1]) if len(self.all_observations) > 0 else 1
        else:
            obs = self.np_random.choice(self.alphabet, p=self._probs)

        self._counts[obs] += 1
        self.all_observations.append(obs)
        return np.array([obs])

    def get_desired_action(self):
        if self._enforce_valid_string:
            # Accept even length strings
            action = self.accept_action if sum(self._counts) % 2 == 0 else self.reject_action
        else:
            action = self.accept_action if self.is_string_valid() else self.reject_action
        return action

    def is_string_valid(self):
        if len(self.all_observations) > 1 and len(self.all_observations) % 2 == 0:
            valid = True
            for i, o in enumerate(self.all_observations):
                if (i % 2 == 0 and o != 1) or (i % 2 == 1 and o != 0):
                    valid = False
                    break
        else:
            valid = False
        return valid

    def reset(self):
        self._clock = 0
        self._enforce_valid_string = (self.np_random.random_sample() <= 0.5)
        self._partial_valid_string, self._partial_valid_len = False, 0
        if self._enforce_valid_string:
            self.max_episode_steps = self.np_random.choice(range(2, self.max_steps + 1, 2))
        else:
            self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
            self._partial_valid_string = (self.np_random.random_sample() <= 0.25)
            if self._partial_valid_string:
                self._partial_valid_len = self.np_random.choice(range(0, self.max_episode_steps, 2))

        self.all_observations = []
        self._counts = [0, 0]
        self._probs = self.np_random.random_sample()
        self._probs = [self._probs, 1 - self._probs]
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
