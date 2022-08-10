# Expected reward function for taking action k
# This is the Q_k(a) function
# Also know as value function

from secrets import choice
import numpy as np
import random
import matplotlib.pyplot as plt


def exp_reward(action,history):
    rewards_for_action = history[action]
    return sum(rewards_for_action)/len(rewards_for_action)

def get_best_action(actions,history):
    exp_rewards = [ exp_reward(action,history) for action in actions ]
    return np.argmax(exp_rewards)

def get_action_value(index):
    pass

# Exploitation method or greedy method
# do not reuse actions again
def get_best_action(actions):
	best_action = 0
	max_action_value = 0
	for i in range(len(actions)): #A 
		cur_action_value = get_action_value(actions[i]) #B
		if cur_action_value > max_action_value:
			best_action = i
			max_action_value = cur_action_value
	return best_action


# Epsilon-greedy strategy
n = 10
probs = np.random.rand(n) # Hidden probabilities
eps = 0.2
record = np.zeros((n,2)) # column 0: times of taking action i, column 1: current mean

def get_reward(prob,n = 10):
	reward = 0
	for i in range(n):
		if random.random() < prob:
			reward += 1
	return reward


def update_record(record,action,r):
	new_r = (record[action,0]*record[action,1]+r)/(record[action,0]+1)
	record[action,0] +=1
	record[action,1] = new_r
	return record

def get_best_action(record):
	arm_index = np.argmax(record[:,1],axis=0)
	return arm_index

if __name__ == "__main__":

	fig, ax = plt.subplots(1,1)

	ax.set_xlabel("Plays")

	ax.set_ylabel("Avg Reward")

	rewards = [0]
	
	for i in range(500):
		
		if random.random()> eps:
			c = get_best_action(record)
		else:
			c = np.random.randint(n)

		r = get_reward(probs[c])

		record = update_record(record,c,r)

		mean_reward = ((i+1)*rewards[-1]+r)/(i+2)

		rewards.append(mean_reward)

	ax.scatter(np.arange(len(rewards)),rewards)
	plt.show()


