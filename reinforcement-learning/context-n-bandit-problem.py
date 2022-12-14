import numpy as np
import random
import torch
import matplotlib.pyplot as plt

class ContextBandit:

    def __init__(self, arms = 10):
        self.arms = arms
        self.init_distribution(arms)
        self.update_state()

    def init_distribution(self,arms):
        # Number of states = number of arms in this example
        self.bandit_matrix = np.random.rand(arms,arms)

    def reward(self,prob):
        reward = 0
        for _ in range(self.arms):
            if random.random() < prob:
                reward += 1
        return reward

    def get_state(self):
        return self.state

    def update_state(self):
        self.state = np.random.randint(0,self.arms)

    def get_reward(self,arm):
        return self.reward(self.bandit_matrix[self.get_state()][arm])

    def choose_arm(self,arm):
        reward = self.get_reward(arm)
        self.update_state()
        return reward

'''
env = ContextBandit()
state = env.get_state()
reward = env.choose_arm(1)
print(state,reward)
'''

def one_hot(N, pos, val=1):
    one_hot_vec = np.zeros(N)
    one_hot_vec[pos] = val
    return one_hot_vec

def softmax(av, tau=1.12):
    softm = ( np.exp(av / tau) / np.sum( np.exp(av / tau) ) )
    return softm

def running_mean(x,N=50):
    c = x.shape[0] - N
    y = np.zeros(c)
    conv = np.ones(N)
    for i in range(c):
        y[i] = (x[i:i+N] @ conv)/N
    return y

def train(env, epochs=15000, learning_rate=1e-2):

    cur_state = torch.Tensor(one_hot(arms,env.get_state())) 

    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    rewards = []

    for _ in range(epochs):

        y_pred = model(cur_state) # Predict rewards based on current state

        av_softmax = softmax(y_pred.data.numpy(), tau=2.0) 

        av_softmax /= av_softmax.sum() # Normalize to sum 1

        choice = np.random.choice(arms, p=av_softmax) 

        cur_reward = env.choose_arm(choice) 

        one_hot_reward = y_pred.data.numpy().copy() 
        
        one_hot_reward[choice] = cur_reward 

        reward = torch.Tensor(one_hot_reward)

        rewards.append(cur_reward)

        loss = loss_fn(y_pred, reward)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        cur_state = torch.Tensor(one_hot(arms,env.get_state())) 

    return np.array(rewards)

loss_fn = torch.nn.MSELoss()

arms = 10

N, D_in, H, D_out = 1, arms, 100, arms

model = torch.nn.Sequential(
    torch.nn.Linear(D_in,H),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out),
    torch.nn.ReLU(),
)

env = ContextBandit(arms)

rewards = train(env)

plt.plot(running_mean(rewards,N=500))
plt.show()