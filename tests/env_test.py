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
    for ep in range(100):
        done = False
        obs = env.reset()
        action = env.env.get_desired_action()
        total_reward = 0
        all_observations = [obs]
        all_actions = [action]
        while not done:
            obs, reward, done, info = env.step(action)
            action = env.env.get_desired_action()
            total_reward += reward
            if not done:
                all_observations.append(obs)
                all_actions.append(action)
        print('Episode: {} Total Reward: {}  Obs: {}, Action: {}'.format(ep, total_reward,
                                                                         ''.join([str(_[0]) for _ in all_observations]),
                                                                         all_actions))
