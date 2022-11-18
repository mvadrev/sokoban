# Q learning Algorithm
import numpy as np
from helpers import Helpers 
import pickle
import matplotlib.pyplot as plt


class QLearning():
  def __init__(self, env):
    # super(QLearning, self).__init__()
    # [list(env.transition[0].items())[i][0] for i in range(len(list(env.transition[0].items())))]
    self.stateTable = []
    self.qtable = []
    self.epsilon = 0.1
    self.alpha = 0.1
    self.gamma = 0.9
    self.timesteps = 1000
    self.env = env
    self.terminalState = [[0,0,0,0,0],
                          [0,3,5,1,0],
                          [0,1,1,1,0],
                          [0,1,1,1,0],
                          [0,0,0,0,0]]
    self.done = False
    self.isFirstIter = True
    self.oldTileUnderPlayerbefore = 1
    self.newTileUnderPlayerAfter = 0
    self.helper = Helpers(self.oldTileUnderPlayerbefore, self.newTileUnderPlayerAfter, self.isFirstIter)
    self.initialState = ""
    self.valueEvolution = []



  # Is the agent in terminal state
  def isTerminalState(self, currentState):
    if(currentState == self.terminalState):
      return True
    else:
      return False
      
  # get Q value 
  def getNewQ(self, oldQ, reward, maxQSprime):
    # print(maxQSprime, "is")
    return oldQ + self.alpha * (reward + (self.gamma * maxQSprime )- oldQ)

  # get max Q using 1 step lookahead
  def getMaxQ(self, sPrime):
    indexOfSPrime = self.stateTable.index(sPrime)
    currentQ = self.qtable[indexOfSPrime]
    max_action = np.asarray(currentQ).argmax()
    return currentQ[max_action]

    
  # Epsilon greedy action selection
  def epsilonGreedy(self, currentState):
    stateIndex = self.stateTable.index(currentState)
    if(np.random.random() < self.epsilon):
      print("exploring...")
      actions = [0,1,2,3]
      randomChoiceAction = np.random.choice(actions)
      return randomChoiceAction
    else:
      print("exploiting.. Choosing best action from Qtable", np.asarray(self.qtable[stateIndex]).argmax())
      print("The epsilon", self.qtable[stateIndex])
      max_action =  np.asarray(self.qtable[stateIndex]).argmax()
      return max_action
        
  # Learn function 
  def learn(self, timesteps):
    self.env.reset()
    
    for timestep in range(timesteps):
      done = False
      while (done == False):
        initialState = self.env.currentState
        
        if (initialState not in self.stateTable):
              self.stateTable.append(initialState)
              self.qtable.append([0.0,0.0,0.0,0.0])
        
        action_selection_index = self.epsilonGreedy(initialState)
        print("Action is", self.env.actionMap[action_selection_index], initialState)

        next_state2, reward, done, meta = self.env.step(action_selection_index)
        print("Next state is ", next_state2, reward)

        self.isFirstIter = False
        indexOfS = self.stateTable.index(initialState)
        if(next_state2 not in self.stateTable):
          self.stateTable.append(next_state2)
          self.qtable.append([0.0,0.0,0.0,0.0])
        maxQ = self.getMaxQ(next_state2)
        Q_old = self.qtable[indexOfS][action_selection_index]
        Q = self.getNewQ(Q_old, reward, maxQ)

       
        self.qtable[indexOfS][action_selection_index] = Q
        # print(self.qtable)
        if(self.isTerminalState(next_state2)):
          print("reached termainal ------------------------------------", self.qtable)
          print("reached termainal ------------------------------------", self.stateTable)

          done = True
          self.env.done = False
      acs = self.qtable[1]
      ind = np.argmax(acs)
      self.valueEvolution.append(self.qtable[1][ind])  
      print(self.valueEvolution)
    # # x axis is time steps    
    x = np.arange(0, timesteps).tolist()
    # y axis is evolution
    y = self.valueEvolution    
    plt.plot(x,y)
    plt.show()  

  def predict(self):
    self.env.reset()
    initialState = self.env.currentState
    print("-----------------------predict =============================")
    while(initialState is not self.isTerminalState(initialState)):  
      initialState = self.env.currentState
      stateIndex = self.stateTable.index(initialState)
      action_selection_index = max_action =  np.asarray(self.qtable[stateIndex]).argmax()
      next_state2, reward, done, meta = self.env.step(action_selection_index)
      print(initialState)
      print("Action is", action_selection_index, next_state2, )
      
      if(done == True):
        print("Reached terminal state",)
        


