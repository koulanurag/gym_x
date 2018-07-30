import logging
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

logger = logging.getLogger(__name__)


class TomitaG(gym.Env):
    """
        Tomita Grammer : 0*1*0*1*
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
        obs = self.np_random.choice(self.alphabet, p=self._probs)
        if self._enforce_valid_string:
            for i, m in enumerate(self._mode_steps):
                if m != 0:
                    obs = i % 2
                    self._mode_steps[i] -= 1
                    break

        self.all_observations.append(obs)
        return np.array([obs])

    def get_desired_action(self):
        # return self.accept_action if self._enforce_valid_string or self.is_string_valid() else self.reject_action
        return self.accept_action if self.is_string_valid() else self.reject_action

    def is_string_valid(self,obs=None):
        obs = self.all_observations if obs is None else obs
        valid = True
        one_zero_count = 0
        for i in range(len(obs) - 1):
            if obs[i] == 1 and obs[i + 1] == 0:
                one_zero_count += 1
            if one_zero_count > 1:
                valid = False
                break
        return valid

    def reset(self):
        self._clock = 0
        self.max_episode_steps = self.np_random.choice(range(self.min_steps, self.max_steps + 1))
        self._enforce_valid_string = (self.np_random.random_sample() <= 0.25)

        self._mode_steps = [0 for _ in range(4)]
        _modes = [_ for _ in range(4)]
        self.np_random.shuffle(_modes)

        for m in _modes:
            self._mode_steps[m] = self.np_random.randint(0, self.max_episode_steps - sum(self._mode_steps))

        self.max_episode_steps = sum(self._mode_steps)

        self._probs = self.np_random.random_sample()
        self._probs = [self._probs, 1 - self._probs]
        self.np_random.shuffle(self._probs)

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
