# gym-x
Environments designed to test various aspects of reinforcement learning policies using recurrent networks. Their minimal state representation could be found [here](../docs/README.md). 

## Installation
```bash
cd gym-x
pip install -e .
```

## Usage:
```python
>>> import gym
>>> import gym_x
>>> env = gym.make('GoldRushDiscrete-v0')
>>> env.action_space
Discrete(4)
>>> env.reset()
array([1., 1.])
>>> env.step(env.action_space.sample())
(array([0., 0.]), 0, False, {'desired_action': 3})
```

