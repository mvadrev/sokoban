import numpy as np

class Helpers():
    def __init__(self, oldTileUnderPlayerbefore, newTileUnderPlayerAfter, isFirstIter ):
        self.oldTileUnderPlayerbefore = oldTileUnderPlayerbefore
        self.newTileUnderPlayerAfter = newTileUnderPlayerAfter
        self.isFirstIter = isFirstIter


    def checkBoxCollision(self,list_of_integers_s, position_of_player_sPrime_row, position_of_player_sPrime_col, action):
                        print("Agene sPrimepos is", position_of_player_sPrime_row, position_of_player_sPrime_col)
        # print("Integers are, list", list_of_integers_s)
                        if(action == 'right'):
                          boxRightWallCheck = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col + 1]
                          if(boxRightWallCheck == 0):
                              print("There is a wall right of box")
                              # Dont update y pos of player into currentState - box is beside wall
                              # Dont update Player position - box is beside wall
                              return list_of_integers_s
                        # Check wall beside box beside player for left case
                        if(action == 'left'):
                            boxLeftWallCheck = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col -1]
                            if(boxLeftWallCheck == 0):
                                print("There is a wall right of box")
                                return list_of_integers_s
                        if(action == 'up'):
                            boxUpWallCheck = list_of_integers_s[position_of_player_sPrime_row - 1][position_of_player_sPrime_col]
                            if(boxUpWallCheck == 0):
                                print("There is a wall up of box")
                                return list_of_integers_s
                        if(action == 'down'):
                            print("Action is down")
                            boxDownWallCheck = list_of_integers_s[position_of_player_sPrime_row + 1][position_of_player_sPrime_col]
                            print("checking boxwall",  list_of_integers_s, boxDownWallCheck)
                            if(boxDownWallCheck == 0):
                                # print("There is a wall up of box", boxDownWallCheck)
                                return list_of_integers_s

    def getNextStateDynamically(self, currentState, action):
      position_of_player_sPrime_row = 0
      position_of_player_sPrime_col = 0
      # print("current", currentState)
      list_of_integers_s = np.array(list(map(int, currentState.split(',')))).reshape(5,5)
      # print("List of intergrs is hee", list_of_integers_s)
      position_of_player_s = np.argwhere(np.array(list_of_integers_s == 5))
      print( "ps at s ofplayer",position_of_player_s, list)
      # This condition is true for 1st iter
      if(action == 'up'):
        position_of_player_sPrime_row = position_of_player_s[0][0] -1
        position_of_player_sPrime_col = position_of_player_s[0][1] 

      if(action == 'down'):
        position_of_player_sPrime_row = position_of_player_s[0][0] + 1
        position_of_player_sPrime_col = position_of_player_s[0][1] 
        print("Updating down", position_of_player_sPrime_row, position_of_player_sPrime_col)
      if(action == 'right'):
        position_of_player_sPrime_row = position_of_player_s[0][0] 
        position_of_player_sPrime_col = position_of_player_s[0][1] + 1
      if(action == 'left'):
        position_of_player_sPrime_row = position_of_player_s[0][0] 
        position_of_player_sPrime_col = position_of_player_s[0][1]  -1

      print("Checking for collosion with walls", )
      # print(list_of_integers_s)
      #Collision detection: Walls: is next state a wall?
      if(list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]) == 0:
        # Hit a wall so return the same state as agent does not moove
        print('Hit a wall', list_of_integers_s)
        return np.array(list(map(int, currentState.split(',')))).reshape(5,5)
      else:
        print("Freespace to move detected..")
        # In first Iter the player always stands on a floor tile with value 1
        if(self.isFirstIter == False): 
          self.oldTileUnderPlayerbefore = 1
          # print("Player next position", [position_of_player_sPrime_y],[position_of_player_sPrime_x])
          self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
          # Detect if player has collided with any box ---------------------------
          if(self.newTileUnderPlayerAfter == 3):
            print("Collided with box")
            return self.checkBoxCollision(list_of_integers_s, position_of_player_sPrime_row, position_of_player_sPrime_col, action)
           

          else:
            print("###### Producing Transition normally ########")
            self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
            # Update Player position 
            list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] = 5
            list_of_integers_s[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore
            self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter
            return list_of_integers_s
          
        else:
          # Do routine for first iteration as in first iteration agent is being provided wih same first state 
          print("First iteration")  
          self.oldTileUnderPlayerbefore = 1
          # print("first iter", [position_of_player_sPrime_y],[position_of_player_sPrime_x])
          self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
          # print("new tile after", self.newTileUnderPlayerAfter)
          if(self.newTileUnderPlayerAfter == 3): # Detect if next state is box
            # print("Here", list_of_integers_s) ->>>>>>>>> here
            # print("next state is a box..", list_of_integers_s)
            return self.checkBoxCollision(list_of_integers_s, position_of_player_sPrime_row, position_of_player_sPrime_col, action) # returns same player pos and box
            # list_of_integers_s, position_of_player_sPrime_x, position_of_player_sPrime_y, action
          else:
            self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
            # Update Player position 
            list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] = 5
            list_of_integers_s[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore
            self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter
            return list_of_integers_s