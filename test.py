from helpers import Helpers 
from environment import Sokoban


a = Helpers(1,0, True)
env = Sokoban()

next, reward, meta, dones = env.step(3)
print(next, reward)

a.getNextStateDynamically('0,0,0,0,0,0,5,1,2,0,0,3,1,3,0,0,2,1,1,0,0,0,0,0,0',3 )

# print('0,0,0,0,0,0,1,1,2,0,0,5,1,3,0,0,2,1,1,0,0,0,0,0,0' in env.rewardMap[0])
# print('0,0,0,0,0,0,1,1,2,0,0,5,1,3,0,0,3,1,1,0,0,0,0,0,0' in env.rewardMap[0])
