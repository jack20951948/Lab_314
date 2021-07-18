import numpy as np
import gym
from gym.wrappers import Monitor

BOX_DIM = 162
MAX_STEPS = 100000
TRAILS = 200

x_vec = np.zeros(BOX_DIM) # state vector
w = np.zeros(BOX_DIM)     # action weights
v = np.zeros(BOX_DIM)     # critic weights
e = np.zeros(BOX_DIM)     # action weight eligibilities
x_bar = np.zeros(BOX_DIM) # critic weight eligibilities

def Activation(x):
    # Activation function : [step function]
    if x >= 0: return 1
    else: return 0

def ACE(learn, decay, reward, gamma, p_before):
    # ACE : generate [improved reinforcement signal (reward_hat)]
    global v, x_vec, x_bar
    
    if reward == -1: 
        p = 0
    else: 
        p = v.dot(x_vec)
        
    reward_hat = reward + gamma*p - p_before
    v += learn * reward_hat * x_bar
    x_bar = decay*x_bar + (1-decay)*x_vec
    
    return reward_hat, p

def ASE(learn, decay, reward):
    # ASE : generate [action]
    global w, x_vec, e
    
    sigma = 0.01
    noise = sigma*np.random.randn()
    
    y = Activation(w.dot(x_vec) + noise)
    w += learn * reward * e
    e = decay*e + (1-decay)*(y*2-1)*x_vec

    return y

def Box(ob):
    # box system : [4-dim state] to [162-dim state] 
    x, x_dot, theta, theta_dot = ob
    box = 0
    
    one_degree = 0.0174532
    six_degrees = 0.1047192
    twelve_degrees = 0.2094384
    fifty_degrees = 0.87266

    if x < -2.4 or x > 2.4  or theta < -1*twelve_degrees or theta > twelve_degrees :
        return Box([0,0,0,0])

    if x < -0.8 : box = 0
    elif x < 0.8 : box = 1
    else: box = 2

    if x_dot < -0.5 : box = box
    elif x_dot < 0.5 : box += 3
    else: box += 6
    
    if theta < -1*six_degrees : box = box
    elif theta < -1*one_degree : box += 9
    elif theta < 0: box += 18
    elif theta < one_degree : box += 27
    elif theta < six_degrees : box += 36
    else : box += 45

    if theta_dot < -fifty_degrees : box = box
    elif theta_dot < fifty_degrees : box += 54
    else : box += 108

    state = np.zeros(BOX_DIM)
    state[box] = 1

    return state


### Simulation by using OpenAI Gym
### https://gym.openai.com/docs

env = gym.make('CartPole-v0')
env = Monitor(env, '/home/jack/Desktop/cart-pole', force=True)

for i in range(0, TRAILS):
    ob = env.reset()
    p_before = 0
        
    for j in range(0, MAX_STEPS):
     x_vec = Box(ob)
     reward_hat, p_before = ACE(learn=0.5, decay=0.8, reward=0, gamma=0.95, p_before=p_before)
     action = ASE(learn=1000, decay=0.9, reward=reward_hat)
     
     if j > 30000: 
       env.render()
         
     ob, _, done, _ = env.step(action)

     if done:
         x_vec = Box(ob)
         reward_hat, p_before = ACE(learn=0.5, decay=0.8, reward=-1, gamma=0.95, p_before=p_before)
         ASE(learn=1000, decay=0.9, reward=reward_hat)
         break

    if i % 10 == 0 :
     print("Trial {0:3} was {1:5} steps".format(i, j))
    if j == MAX_STEPS-1 :
     print("Pole balanced successfully for at least {} steps at Trail {}".format(MAX_STEPS, i))
     break

env.close()