import gym, gym_x
import os
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test env')
    parser.add_argument('--env', default='TomitaG-v0', help="Name of the environment")

    args = parser.parse_args()

    env = gym.make(args.env)
    env.seed(0)
    ep_count = 1000
    valid_count = 0
    done = False
    for ep in range(ep_count):
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
        obs = all_observations
        valid = True
        one_zero_count = 0
        for i in range(len(obs) - 1):
            if obs[i][0] == 1 and obs[i + 1][0] == 0:
                one_zero_count += 1
            if one_zero_count > 1:
                valid = False
                break

        if valid:
            valid_count += 1
        print(valid)
    print(valid_count / ep_count)
