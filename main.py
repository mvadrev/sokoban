import environment 
import numpy as np
from Qlearn import QLearning
from semigradsarsa import SemiGradientSarsa


if __name__ == "__main__":
    
    # Initialize environment
    env = environment.Sokoban()
    
    actionMap = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
    # print(env.currentState)
    # next_state , reward, dones,meta = env.step(3)
    # print("lll",next_state, reward)
    # print("Current",env.reset())
    # for i in range(11):
    #     n, r, m, c  = env.step(0)
    #     print("Reward is", n, r, m, c)
    # print(n)
    ql = QLearning(env)
    # # # state = '0,0,0,0,0,0,5,1,2,0,0,3,1,3,0,0,2,1,1,0,0,0,0,0,0'
    # # # action = ql.epsilonGreedy(state)
    # # print("Action to take is:", actionMap[action])
    ql.learn(5000)
    # # print(ql.stateTable)
    # ql.predict()

    # s = SemiGradientSarsa(env, 1e-5, 0.5)
    # s.train(2)

    # model = {}
    # with open ('C:\\Users\\mvadr\OneDrive\\Desktop\\asn1 RL\\Sokoban\\mode.pkl','rb') as pick:
    #     model = pickle.load(pick)

    # print(model)
    

