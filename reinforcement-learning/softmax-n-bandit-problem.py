import numpy as np
import random
import matplotlib.pyplot as plt

# Vals is an action-value vector
# Returns a probabilistic distribution over the actions
# Tau is the temperature param: the higher the value, the more similar the probs will be

def softmax(av,tau=1.12):
    return np.exp(av/tau)/ np.sum( np.exp(av/tau) )


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

n = 10
eps = 0.2
record = np.zeros((n,2)) # column 0: times of taking action i, column 1: current mean
probs = np.random.rand(n)

if __name__ == "__main__":

    fig, ax = plt.subplots(1,1)

    ax.set_xlabel("Plays")

    ax.set_ylabel("Avg Reward")

    rewards = [0]
	
    for i in range(500):
	    
        p = softmax(record[:,1])

        c = np.random.choice(np.arange(n),p=p)

        r = get_reward(probs[c])

        record = update_record(record,c,r)
        
        mean_reward = ((i+1)*rewards[-1]+r)/(i+2)
        
        rewards.append(mean_reward)

    ax.scatter(np.arange(len(rewards)),rewards)
    plt.show()