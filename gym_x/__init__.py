import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Gold Rush
register(
    id='GoldRushSneak-v0',
    entry_point='gym_x.envs.goldrush::GoldRushS',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)
register(
    id='GoldRushBlind-v0',
    entry_point='gym_x.envs.goldrush:GoldRushB',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)
register(
    id='GoldRushRead-v0',
    entry_point='gym_x.envs.goldrush:GoldRushR',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=300,
    nondeterministic=False,
)

# Tomita Grammer
register(
    id='TomitaA-v0',
    entry_point='gym_x.envs.tomita:TomitaA',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaB-v0',
    entry_point='gym_x.envs.tomita:TomitaB',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaC-v0',
    entry_point='gym_x.envs.tomita:TomitaC',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaD-v0',
    entry_point='gym_x.envs.tomita:TomitaD',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaE-v0',
    entry_point='gym_x.envs.tomita:TomitaE',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaF-v0',
    entry_point='gym_x.envs.tomita:TomitaF',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
register(
    id='TomitaG-v0',
    entry_point='gym_x.envs.tomita:TomitaG',
    tags={'wrapper_config.TimeLimit.max_episode_steps': 300,
          'discrete': False},
    reward_threshold=1,
    nondeterministic=False,
)
