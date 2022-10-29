import gym
from gym import spaces
import numpy as np
from transition import reward 
import helpers

class Sokoban(gym.Env):
  def __init__(self):
    self.map = [0,0,0,0,0,0,5,1,2,0,0,3,1,3,0,0,2,1,1,0,0,0,0,0,0]
    self.currentState = np.array(self.map, dtype='int').reshape(1,25)

    self.done = False
    self.rewardMap = reward

    self.action_space = spaces.Discrete(4)
    self.actionMap = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
    self.observation_space = spaces.Box(0, 5, shape=(1,25), dtype='int')
    self.oldTileUnderPlayerbefore = 1
    self.newTileUnderPlayerAfter = 0
    self.isFirstIter = True
    self.episodeLength = 10
    self.reward = 0
    self.stringNextState = ""
    self.stringNextState = ""

    self.h = helpers.Helpers(self.oldTileUnderPlayerbefore, self.newTileUnderPlayerAfter, self.isFirstIter)

    super(Sokoban, self).__init__()

  def reset(self):
    self.currentState = np.array(self.map, dtype='int').reshape(1,25)
    self.done = False
    return self.currentState

  def step(self, action): 

      print("Current in main--------------------------------------")
      ac = self.actionMap[action]
      stringCurrentState = ','.join(map(str, self.currentState[0]))  
      self.stringCurrentState = stringCurrentState
          
      if (self.episodeLength > 10):
        self.done = True
      else:
        # print("state", state)
        next_state_integers = self.h.getNextStateDynamically(self.stringCurrentState, ac).reshape(1,25)
        # print(self.h.getNextStateDynamically(stringCurrentState, ac))
        self.stringNextState = ','.join(map(str, next_state_integers[0]))
        # print("next string state is", stringNextState)
        self.episodeLength += 1
        reward = 0
        if(self.stringNextState.strip() in self.rewardMap[0]):
          self.reward = self.rewardMap[0][self.stringNextState]
          # print("Found a reward", reward)
        else: 
          # print("Reward not found", -1)
          self.reward = -1
      return self.stringNextState, self.reward, self.done, {}

