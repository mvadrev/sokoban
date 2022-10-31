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
    self.initialState = ""

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
      print("Q table is", self.qtable[stateIndex])
      # print("exploiting.. Choosing best action from Qtable", np.argmax(self.stateTable[stateIndex]))
      return np.asarray(self.qtable[stateIndex]).argmax()
        
  # Learn function 
  def learn(self, timesteps):
    for timestep in range(timesteps):
      while (self.done == False):
      # for i in range(2):
        stringCurrentState = ','.join(map(str, self.env.currentState[0]))
        if (stringCurrentState not in self.stateTable):
              self.stateTable.append(stringCurrentState)
              self.qtable.append([0.0,0.0,0.0,0.0])
        action_selection_index = self.epsilonGreedy(stringCurrentState)
        print("String current", stringCurrentState)
        print("Action is", self.env.actionMap[action_selection_index], action_selection_index)
        next_state, reward, done, meta = self.env.step(action_selection_index)
        # stringNext = ','.join(map(str, next))
        print("results", next_state, reward)

        # if(next_state not in self.stateTable):
        #       print("Adding next state")
        #       self.stateTable.append(next_state)
        #       self.qtable.append([0.0,0.0,0.0,0.0])
        # print(self.qtable)



    # for timestep in range(timesteps):
    #   # while (self.done == False):
    #     if (stringCurrentState not in self.stateTable):
    #       self.stateTable.append(stringCurrentState)
    #       self.qtable.append([0.0,0.0,0.0,0.0])
    #       print(self.stateTable, self.qtable)
    #     indexOfS = self.stateTable.index(stringCurrentState)
    #     action_selection_index = self.epsilonGreedy(stringCurrentState)
    #     print("action is", self.env.actionMap[action_selection_index])
    #     print("Current state is", stringCurrentState)
    #     next_state , reward, dones,meta = self.env.step(action_selection_index)
    #     print("Next state is", next_state)
    # initialState = self.env.currentState
    # stringCurrentState = ','.join(map(str, initialState[0])) 
    # for timestep in range(timesteps): 
      # print("doing")
    #   while (self.done == False):
    #     if (stringCurrentState not in self.stateTable):
    #       self.stateTable.append(stringCurrentState)
    #       self.qtable.append([0.0,0.0,0.0,0.0])
          
        # indexOfS = self.stateTable.index(stringCurrentState)
        # action_selection_index = self.epsilonGreedy(stringCurrentState)
        # print("action is", self.env.actionMap[action_selection_index])
        # print("Current state is", stringCurrentState)
        # next_state , reward, dones,meta = self.env.step(action_selection_index)
        # print("Next state is", next_state)
        # if(next_state not in self.stateTable):
        #   print("Adding next state")
        #   self.stateTable.append(next_state)
        #   self.qtable.append([0.0,0.0,0.0,0.0])
        #   print(self.stateTable)
        # stringCurrentState = next_state
       
            

    #     if (initialState not in self.stateTable):
    #       print("Adding")
    #       self.stateTable.append(self.initialState)
    #       # self.qtable.append([0.0,0.0,0.0,0.0])
    #     print("Initia state ", self.stateTable)
    #     break
   
        # print("next current state is", self.stringCurrentState)
        # Before taking action add currentState into stateTable[i] and initialize Qtable[i] for all actions
        # if (initialState not in self.stateTable):
        #   self.stateTable.append(self.initialState)
        #   self.qtable.append([0.0,0.0,0.0,0.0])
        #   print("Appended")
        
        # indexOfS = self.stateTable.index(initialState)
        # action_selection_index = self.epsilonGreedy(initialState)
        # next_state , reward, dones,meta = self.env.step(action_selection_index)
        # print(next_state , reward)

        # initialState =  np.array(list(map(int, next_state.split(',')))).reshape(1,25)

        # self.done = True # <---remove this after dev
        # print("Reward is",self.stringCurrentState, reward, next_state, self.env.actionMap[action_selection_index])
        # print("Next is ",next_state)
        # # Append next state and initialize Q values if next state is missing from qtable
        # if(next_state not in self.stateTable):
        #   print("Adding next state")
        #   self.stateTable.append(next_state)
        #   self.qtable.append([0.0,0.0,0.0,0.0])
        # # print(self.qtable, self.stateTable)
        # maxQ = self.getMaxQ(next_state)
        # Q_old = self.qtable[indexOfS][action_selection_index]
        # # print("Oldq",Q_old)
        # Q = self.getNewQ(Q_old, reward, maxQ)
        # # print("New Q is", Q)
        # # Update Q table with new values
        # self.qtable[indexOfS][action_selection_index] = Q
        
        # print("Initial state is now", self.qtable)
        # print(self.qtable, self.stateTable)
        # break
        
    




            

    # def predict(self):
    #   pass
            


