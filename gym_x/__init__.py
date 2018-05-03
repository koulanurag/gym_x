import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='GoldRushDiscrete-v0',
    entry_point='gym_x.envs.gold_rush_discrete:GoldRushD',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': True},
    reward_threshold=300,
    nondeterministic=False,
)
register(
    id='GoldRushContinuous-v0',
    entry_point='gym_x.envs.gold_rush_cont:GoldRushC',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)
register(
    id='GoldRushBlind-v0',
    entry_point='gym_x.envs.gold_rush_blind:GoldRushB',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)
register(
    id='GoldRushRead-v0',
    entry_point='gym_x.envs.gold_rush_read:GoldRushR',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)
