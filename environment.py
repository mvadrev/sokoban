import gym
from gym import spaces
import numpy as np
from transition import reward 
import helpers
import pickle
import copy


class Sokoban(gym.Env):
  def __init__(self):
    # self.randomSpawnStates = [[0,0,0,0,0,0,2,3,1,0,0,1,1,1,0,0,1,1,5,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,1,0,0,1,1,1,0,0,1,5,1,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,1,0,0,1,1,1,0,0,5,1,1,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,1,0,0,5,1,1,0,0,1,1,1,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,1,0,0,1,5,1,0,0,1,1,1,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,1,0,0,1,1,5,0,0,1,1,1,0,0,0,0,0,0],
    #                          [0,0,0,0,0,0,2,3,5,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0]]
    self.map = [[0,0,0,0,0],
                [0,2,3,1,0], 
                [0,3,1,1,0],
                [0,1,1,5,0],
                [0,0,0,0,0]]

    self.currentState = self.map
    self.done = False
    self.rewardMap = [[[0,0,0,0,0],
                      [0,3,5,1,0],
                      [0,1,1,1,0],
                      [0,1,1,1,0],
                      [0,0,0,0,0]]]
    self.rewards = [5]
    self.episodeLength = 0
    self.action_space = spaces.Discrete(4)
    self.actionMap = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
    self.observation_space = spaces.Box(0, 5, shape=(1,25), dtype='int')
    self.oldTileUnderPlayerbefore = 1
    self.newTileUnderPlayerAfter = 0
    self.isFirstIter = True
    self.episodeLength = 0
    self.reward = 0
    self.stringNextState = ""
    self.stringNextState = ""

    self.h = helpers.Helpers(self.oldTileUnderPlayerbefore, self.newTileUnderPlayerAfter, self.isFirstIter)

    super(Sokoban, self).__init__()

  def reset(self):
    # COde to randomize player spawn position
    # self.episodeLength = 0
    # rando_int = np.random.randint(0, high=6, size=1)
    # print(rando_int)
    # print("random spwan state is", self.randomSpawnStates[rando_int[0]])
    # self.currentState = np.array(self.randomSpawnStates[rando_int[0]], dtype='int').reshape(1,25).tolist()[0]
    # self.done = False
    # return self.currentState
    
    self.episodeLength = 0
    self.currentState = np.array(self.map, dtype='int').tolist()
    self.done = False
    return self.currentState

  def step(self, action): 
      self.episodeLength = self.episodeLength + 1
      if(self.episodeLength == 35):
        print("Completed 10 timesteps so resetting game ..")
        state_copy = self.reset()
        
        return state_copy, -10, True, {}
      else:
       while (self.done == False):
          self.isFirstIter = False
          ac = self.actionMap[action]

          next_state_integers = self.h.getNextStateDynamically(np.array(self.currentState), ac).tolist()

          self.currentState = next_state_integers
          
          # reward = 0

          if(np.array(next_state_integers) == np.array(self.rewardMap)).all():
            index = self.rewardMap.index(next_state_integers)
            reward = self.rewards[index]
            return next_state_integers, reward, self.done, {}

          else:           
            return next_state_integers, -1, self.done, {}

        

