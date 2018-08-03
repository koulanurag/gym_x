import gym, gym_x
import os
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test env')
    parser.add_argument('--env', default='TomitaD-v0', help="Name of the environment")

    args = parser.parse_args()

    env = gym.make(args.env)
    env.seed(0)
    done = False
    valid_count = 0
    ep_count = 1000
    for ep in range(ep_count):
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
        valid = not ('000' in ''.join([str(_[0]) for _ in all_observations]))
        if valid:
            valid_count += 1
        print(valid)
    print(valid_count / ep_count)
