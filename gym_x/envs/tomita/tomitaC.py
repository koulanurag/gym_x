import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)


class TomitaC(gym.Env):
    """
        Tomita Grammer : An odd number of consecutive 1s is always followed by an even number of consecutive 0s
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
        self._next_zeros = None
        self.seed()

        self.min_steps = 10
        self.max_steps = 50
        self.last_one_count = 0
        self.enc = True
        self.all_observations = []
        self._enforce_valid_string = True

    def step(self, action):
        if action >= self.total_actions:
            raise ValueError("action must be one of %r" % range(self.total_actions))

        self._clock += 1
        done = True if self._clock >= self.max_episode_steps else False
        reward = 1 if done and self.get_desired_action() == self.accept_action else 0
        next_obs = self._get_observation() if not done else self._get_random_observation()
        info = {'desired_action': self.get_desired_action() if not done else None}
        return next_obs, reward, done, info

    def _get_observation(self):
        obs = self.np_random.choice(self.alphabet, p=self._probs)
        if self._enforce_valid_string:
            obs = self._generated_observation[self._clock]
        self.all_observations.append(obs)
        return np.array([obs])

    def _get_random_observation(self):
        return self.np_random.choice(self.alphabet)

    def get_desired_action(self):
        return self.accept_action if self.is_string_valid() else self.reject_action

    def is_string_valid(self):
        valid = True
        count = [0, 0]
        first_one = True
        last_i = len(self.all_observations) - 1

        for i, o in enumerate(self.all_observations):
            count[o] += 1
            if first_one and o == 1:
                first_one = False
                count = [0, 1]
            elif (not first_one and o == 1 and i > 0 and self.all_observations[i - 1] == 0):
                if (count[1] - 1) % 2 != 0 and count[0] % 2 != 0:
                    valid = False
                    break
                count = [0, 1]
            elif i == last_i and o == 0:
                if count[1] % 2 != 0 and count[0] % 2 != 0:
                    valid = False
                    break
                count = [0, 1]

        return valid

    def reset(self):
        self._clock = 0
        self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
        self._enforce_valid_string = (self.np_random.random_sample() <= 0.5)
        self._probs = self.np_random.random_sample()
        self._probs = [self._probs, 1 - self._probs]
        print(self._enforce_valid_string)
        if self._enforce_valid_string:
            self._generated_observation = []
            obs = self.np_random.choice([0, 1])
            while len(self._generated_observation) < self.max_episode_steps:
                n = self.np_random.randint(0, 10)
                self._generated_observation += [obs] * n
                if obs == 1 and n % 2 != 0:
                    self._generated_observation += [0] * 2 * self.np_random.randint(1, 5)
                    obs = 1
                else:
                    obs = self.np_random.choice([0, 1])

            self.max_episode_steps = len(self._generated_observation)

        self.all_observations = []
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

    def _temp(self):
        self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
        self._generated_observation = []
        while len(self._generated_observation) < self.max_episode_steps:
            obs = self.np_random.choice([0, 1])
            n = self.np_random.randint(0, 10)
            self._generated_observation += [obs] * n
            if obs == 1 and n % 2 != 0:
                self._generated_observation += [0] * 2 * self.np_random.randint(1, 10)

        self.max_episode_steps = len(self._generated_observation)
