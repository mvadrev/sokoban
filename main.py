import environment 
import numpy as np
from Qlearn import QLearning

if __name__ == "__main__":
    
    # Initialize environment
    env = environment.Sokoban()
    
    actionMap = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
    # print(env.currentState)
    # next_state , reward, dones,meta = env.step(3)
    # print("lll",next_state, reward)
    

    ql = QLearning(env)
    # state = '0,0,0,0,0,0,5,1,2,0,0,3,1,3,0,0,2,1,1,0,0,0,0,0,0'
    # action = ql.epsilonGreedy(state)
    # print("Action to take is:", actionMap[action])
    ql.learn(6)
    

