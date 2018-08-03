import gym, gym_x
import os
import random
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test env')
    parser.add_argument('--env', default='TomitaC-v0', help="Name of the environment")

    args = parser.parse_args()

    env = gym.make(args.env)
    env.seed(0)
    done = False
    valid_count = 0
    ep_count = 1000
    all_ep_reward = 0
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
        all_ep_reward += total_reward
        valid = True
        count = [0, 0]
        first_one = True
        last_i = len(all_observations) - 1

        for i, o in enumerate(all_observations):
            o = o[0]
            count[o] += 1
            if first_one and o == 1:
                first_one = False
                count = [0, 1]
            elif (not first_one and o == 1 and i > 0 and all_observations[i - 1] == 0):
                if (count[1] - 1) % 2 != 0 and count[0] % 2 != 0:
                    valid = False
                    break
                count = [0, 1]
            elif i == last_i and o == 0:
                if count[1] % 2 != 0 and count[0] % 2 != 0:
                    valid = False
                    break
                count = [0, 1]
        if valid:
            valid_count += 1
        print(valid)

    print(valid_count / ep_count)
    print(all_ep_reward/ep_count)
