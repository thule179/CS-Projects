
#  To use this program, create an input file name 'jugdata.txt' with the format below:
#  Sample 'jugdata.txt' file:
# 	8 7 3
# 	1 4
# where the first line is the capacity of the jugs respectively [8,7,3]. The first number of the second line indicates the position of the jug you want and the second number indicates how many liters you want to be in that jug

#  Date Created: 10/05/2015
#  Date Last Modified: 10/07/2015


# Creates a class that will process all the possible states
class State:
  def __init__ (self, jugfile, jugs = [] , steps = 0, history = None, capacity_list = [], jug_pos = 0, litter = 0):
   self.jugfile = jugfile # data file
   self.jugs = jugs # list of jugs in the data file
   self.steps = steps # list of steps to fill in the jugs until desired state is reached
   self.history = history # current list of best moves
   self.capacity_list = capacity_list # list of capacity each jug has
   self.jug_pos = jug_pos # position of desired jug
   self.litter = litter # desired amount of water in desired jug
  
  # Process data file to get needed numbers
  def readJug(self):
   capacity_list = []
   jug_goal = []
   jug = 0 # jug goal
   litter = 0 # number of litters to obtain in desired jug
   count_jug = 0

  # Process the first line in jugdata.txt
   line = self.jugfile.readline()
   line = line.split() # get rid of spaces

   for num in line:
    num = int(num)
    capacity_list.append(num)
    count_jug += 1

  # Process the second line in jugdata.txt
   line = self.jugfile.readline()
   line = line.split()

   for n in line:
    n = int(n)
    jug_goal.append(n)
  
   jug = jug_goal[0]
   litter = jug_goal [1]
   self.capacity_list = capacity_list
   self.jug_pos = jug
   self.litter = litter
   self.jugs = [0] * count_jug
  
  # Return all the states that a list of jugs can go through
  def successors(self, state):
   state_list = []
   # fill up all the jugs until full
   for jug in range(len(self.capacity_list)):

    if state[jug] != self.capacity_list[jug]:
     # copy the list of jugs to not overwrite on previous states made
      new_list = list(state)
     # fill up the jug if it's not full
      new_list[jug] = self.capacity_list[jug]
      state_list.append(new_list)

   # empty jug
   for jug1 in range(len(self.capacity_list)):

    if state[jug1] != 0:
      # copy the list of jugs
      new_list1 = list(state)
      # empty jug
      new_list1[jug1] = 0
      state_list.append(new_list1) 
   
   # transfer from one jug to another
   for jug2 in range(len(self.capacity_list)):

    if state[jug2] != 0:
      # current_jug is jug to pour into
      for current_jug in range(len(state)):
        # if current_jug is pointing to itself, or the jug to pour into is at max capacity, then don't pour
       if current_jug != jug2 and state[current_jug] != self.capacity_list[current_jug]:
        new_list2 = list(state)
        # to prevent overflow of water
        min_fill = min(state[jug2] + state[current_jug], self.capacity_list[current_jug])
        # amount of water to pour
        difference = min_fill - state[current_jug]
        new_list2[current_jug] = min_fill
        # pour water
        new_list2[jug2] = state[jug2] - difference
        state_list.append(new_list2)   

   return state_list 

  def is_goal(self, state):
    # if current state matches desired state, then return True
    return state[self.jug_pos - 1] == self.litter

  def fillJug(self, state_list, new_history = []):
   # Create an empty list with large enough size to push states in
   if len(new_history) == 0:
    new_history.append(list(self.jugs)) 
    
   state_list = self.successors(new_history[-1])

   for state in state_list:
    temp_history = list(new_history) # gets size for temporary history to hold the states
    temp_history.append(state) 
    # first base case, if reaches goal then return current list of states
    if self.is_goal(state):
      
      if self.history == None: # if there's nothing yet in history, then replace with temporary history - considered as best possible moves 
        self.history = temp_history  
      
      if(len(self.history) > len(temp_history)):
        # replace current best possible moves with better possible moves (fewer steps)
        self.history = temp_history

      return self.history

    # second base case, if the number of states exceeds 50, terminate  
    if len(temp_history) > 50:
      break 
    # if already found, stop searching and return the possible states since the number of steps will only be increasing
    elif self.history != None and len(temp_history) > len(self.history): 
      return self.history

    # third base case, if state has already occured, go back to the beginning of the loop 
    if state in new_history:
      continue

    self.fillJug(state_list, temp_history) # call the function recursively until base case is reached or limit is reached

def main():
  jug_file = open('jugdata.txt', 'r')
  # Create jug object
  jug = State(jug_file)
  jug.readJug()
  state_list = []
  history = []
  jug.fillJug(state_list, history)
  answer_list = jug.history
  if answer_list != None:
   for state in answer_list:
    print(state)
  else: # if exceeds 50 states
   print('Too many states.')
main()
