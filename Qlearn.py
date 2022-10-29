# Q learning Algorithm
import numpy as np
from helpers import Helpers 

class QLearning():
  def __init__(self, env):
    # super(QLearning, self).__init__()
    # [list(env.transition[0].items())[i][0] for i in range(len(list(env.transition[0].items())))]
    self.stateTable = []
    self.qtable = []
    self.epsilon = 0.1
    self.alpha = 0.01
    self.gamma = 0.9
    self.timesteps = 1000
    self.env = env
    self.terminalState = '0,0,0,0,0,0,1,1,2,0,0,1,1,5,0,0,2,1,1,0,0,0,0,0,0'
    self.done = False
    self.isFirstIter = True
    self.oldTileUnderPlayerbefore = 1
    self.newTileUnderPlayerAfter = 0
    self.helper = Helpers(self.oldTileUnderPlayerbefore, self.newTileUnderPlayerAfter, self.isFirstIter)

  # Is the agent in terminal state
  def isTerminalState(self, currentState):
    if(currentState == self.terminalState):
      return True
    else:
      return False
  # get Q value 
  def getNewQ(self, oldQ, reward, maxQSprime):
    # print(maxQSprime, "is")
    return oldQ + self.alpha * (reward + self.gamma * (maxQSprime - oldQ))

  # get max Q using 1 step lookahead
  def getMaxQ(self, sPrime):
    indexOfSPrime = self.stateTable.index(sPrime)
    currentQ = self.qtable[indexOfSPrime]
    max_action = np.asarray(currentQ).max()
    # print("Th max action is", max_action)
    return max_action

    
  # Epsilon greedy action selection
  def epsilonGreedy(self, currentState):
    randomProb = np.random.random()
    stateIndex = self.stateTable.index(currentState)
    if (randomProb > self.epsilon):
      # print("exploring...")
      actions = [0,1,2,3]
      randomChoiceAction = np.random.choice(actions)
      return randomChoiceAction
    else:
      # print("Q table is", self.qtable[stateIndex])
      # print("exploiting.. Choosing best action from Qtable", np.argmax(self.stateTable[stateIndex]))
      return np.asarray(self.qtable[stateIndex]).argmax()
        
  # Learn function 
  def learn(self, timesteps):
    time = 0
    initialState = self.env.reset()
    
    for timestep in range(timesteps): 
      self.stringCurrentState = ','.join(map(str, initialState[0]))
      if(self.isTerminalState(self.stringCurrentState)):
        self.env.reset()
        self.done = True
      while (self.done == False):
        # Before taking action add currentState into stateTable[i] and initialize Qtable[i] for all actions
        if (self.stringCurrentState not in self.stateTable):
          self.stateTable.append(self.stringCurrentState)
          self.qtable.append([0.0,0.0,0.0,0.0])
          
          

        # print(self.qtable)
        # self.done = True # <---remove this after dev
        reward = 0
        action_selection_index = self.epsilonGreedy(self.stringCurrentState)
        indexOfS = self.stateTable.index(self.stringCurrentState)
        next_state , reward, dones,meta = self.env.step(3)
        # self.done = True # <---remove this after dev
        # Append next state and initialize Q values if next state is missing from qtable
        if(next_state not in self.stateTable):
          # print("Adding next for maxq")
          self.stateTable.append(next_state)
          self.qtable.append([0.0,0.0,0.0,0.0])
        print(self.qtable)
        maxQ = self.getMaxQ(next_state)
        Q_old = self.qtable[indexOfS][action_selection_index]
        print(Q_old)
        Q = self.getNewQ(Q_old, reward, maxQ)
        # print("New Q is", Q)
        # Update Q table with new values
        self.qtable[indexOfS][action_selection_index] = Q
        # print(self.qtable, self.stateTable)
    initialState = next_state




            

    def predict(self):
      pass
            


