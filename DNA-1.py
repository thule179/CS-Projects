#  File: DNA.py

#  Description: Find Longest Common Sequence between each pair of DNA strands

#  Student Name: Thu Anh Le

#  Student UT EID: tal864

#  Course Name: CS 303E

#  Unique Number: 51630

#  Date Created: 3/23/2015

#  Date Last Modified: 3/25/2015

def dna_common():
 global dna
 count=0

 
 for i in range(1, len(dna)-1, 2): #view 2 lines at a time
  first_dna = dna[i].upper() #first strand
  second_dna=dna[i+1].upper()#second strand
  count+=1  #pair number, each time the loop runs equals to the pair number
  print('Pair',count,': ',end='') 
  foundMatch=False
  window_size=min(len(first_dna),len(second_dna)) #start comparing from the shortest strand

  while(window_size!=0):
    comps=len(first_dna)-window_size+1 #number of computations to be done for each window size
    
    for index in range(0,comps): 
      window=first_dna[index:index+window_size] 
     
      result=second_dna.find(window)
      if(result!=-1): #if window value is found in result
       if(foundMatch==True): #foundMatch is True when more than one sequence is found, printing the next sequences
        print('        ',window)
        
       if(foundMatch==False): #printing the first similar sequence
        print(window)
        foundMatch=True
       
        
    if(foundMatch): #if foundMatch,then stop
     break
    window_size-=1 #if not, then keep decrement window size 
  if(not foundMatch): 
    print('No Common Sequence Found')
    
  print(' ') 
def main():
  global dna
  common_list=[]
  print('Longest Common Sequences')
  print(' ')
  dna=[i.rstrip('\n') for i in open('dna.txt')]
  dna_common()

  
  
  
  

 
  

  	
main()
