#  File: Nim.py
#  Description: Nim game strat
#  Student's Name: Thu Anh Le
#  Student's UT EID: tal864
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 09/04/2015
#  Date Last Modified: 09/09/2015

# Computes nim-sum of all the heaps from a data file
class gameNim:
 # gameNim constructor
 #
 # expects data file
 def __init__ (self, nim_file): 
  self.nim_file = nim_file 

 # Reads and inteprets the data file
 #
 # Returns a list of 3 counters in a heap
 def readHeap(self):
  num_list = list()
  line = self.nim_file.readline()
  num_line = int(line)

  for i in range(num_line):
   line_data = self.nim_file.readline()

   for s in line_data.split():
    if s.isdigit():
     s = int(s)
     num_list.append(s)

  return num_list
   
 # calculates each heap and prints the best move to win the game, if nimSum=0, then you'll lose
 def calcHeap(self):
  counter = gameNim.readHeap(self)

  for i in range (0, len(counter), 3):
   a = counter[i]
   b = counter[i + 1]
   c = counter[i + 2]
   nimSum = a ^ b ^ c
   p = a ^ nimSum
   q = b ^ nimSum
   r = c ^ nimSum

   if nimSum == 0:
    print('Heaps: ', a, b, c, ': You lose')
   else:
    if(p < a):
      p = a - p
      print('Heaps: ', a, b, c, ': remove', p, 'from Heap 1')
    elif(q < b):
      q = b - q
      print('Heaps: ', a, b, c, ': remove', q, 'from Heap 2')
    elif(r < c):
      r = c - r
      print('Heaps: ', a, b, c, ': remove', r, 'from Heap 3')


def main():

 nim_file = open('nim.txt','r')
 game = gameNim(nim_file)
 game.calcHeap()

main()
