import gym, gym_x
import os
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test env')
    parser.add_argument('--env', default='GoldRushRead-v0', help="Name of the environment")

    args = parser.parse_args()

    env = gym.make(args.env)
    env.seed(0)
    done = False
    for ep in range(10):
        done = False
        obs = env.reset()
        action = env.env.get_desired_action()
        total_reward = 0
        all_observations = [obs]
        while not done:
            obs, reward, done, info = env.step(action)
            action = env.env.get_desired_action()
            total_reward += reward
            if not done:
                all_observations.append(obs)
        print('Episode: {} Total Reward: {}  Obs: {}'.format(ep, total_reward,
                                                             ''.join([str(_[0]) for _ in all_observations])))
        one_count = all_observations.count(1)
        zero_count = all_observations.count(0)
        print(one_count, zero_count)
        print((one_count - zero_count) % 3 == 0 and total_reward == 1)
