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
        next_obs = self._get_observation()
        info = {'desired_action': self.get_desired_action()}
        return next_obs, reward, done, info

    def _get_observation(self):
        obs = self.np_random.choice(self.alphabet, p=self._probs)
        if self._enforce_valid_string and 0<self._clock < self.max_episode_steps:
            if self._next_zeros >= 0:
                if self._next_zeros == 0:
                    obs = 1
                else:
                    obs = 0
                self._next_zeros -= 1
            elif 0 < self._clock and self.all_observations[-1] ==0  and self.last_one_count % 3 == 0:
                self._next_zeros = 2 * self.np_random.randint(2, (
                        self.max_episode_steps - len(self.all_observations)) // 8 + 4)
                self._next_zeros -= 1
                obs = 0
                self.last_one_count = 0
        self.last_one_count += obs
        self.all_observations.append(obs)
        return np.array([obs])

    def get_desired_action(self):
        return self.accept_action if self.is_string_valid() else self.reject_action

    def is_string_valid(self):
        valid = False
        count = [0, 0]
        first_one = True
        for i, o in enumerate(self.all_observations):
            if first_one and o == 1:
                first_one = False
            if not first_one and o == 1 and i > 1 and self.all_observations[i - 1] == 0:
                if count[1] % 2 != 0 and count[0] % 2 != 0:
                    valid = False
                    break
                count[o] = 1
            else:
                count[o] += 1

        return valid

    def reset(self):
        self._clock = 0
        self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
        # self._enforce_valid_string = (self.np_random.random_sample() <= 0.5)
        self._enforce_valid_string = 1
        self.all_observations = []
        self._next_zeros = 0
        # self._probs = self.np_random.random_sample()
        # self._probs = [self._probs, 1 - self._probs]
        self._probs = [0.5, 0.5]
        self.last_one_count = 0
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
