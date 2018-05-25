import gym, gym_x
import os
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test env')
    parser.add_argument('--env', default='GoldRushRead-v0', help="Name of the environment")

    args = parser.parse_args()

    env = gym.make(args.env)

    done = False
    for ep in range(10):
        done = False
        env.seed(ep)
        obs = env.reset()
        action = env.env.get_desired_action()
        total_reward = 0
        while not done:
            obs, reward, done, info = env.step(action)
            action = env.env.get_desired_action()
            total_reward += reward
        print('Episode: {} Total Reward: {}'.format(ep, total_reward))
