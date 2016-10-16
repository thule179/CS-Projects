#  File: WordSearch.py

#  Description: find the location in the grid where the word can be found in a crossword

#  Student Name: Thu Anh Le

#  Student UT EID: tal864

#  Partner Name: My cat

#  Partner UT EID: My cat doesn't go to UT

#  Course Name: CS 303E 

#  Unique Number: 51630

#  Date Created: 4/13/2015

#  Date Last Modified: 4/15/2015

def word_search(num_line,num_char): #do the word search
 line=in_file.readline()
 
 row=[]

 for i in range(n_line):
  line=in_file.readline()
  line=line.split()
  row.append(line)
 
 

 line=in_file.readline() #empty string
 line=in_file.readline() #number of words to search
 n_word=int(line)


 #get a list of words need to search
 for i in range(n_word):
  line=in_file.readline()
  line=line.strip()
  match=True
  
#find words 
  for row_num in range(len(row)):
   s='' 
   c=''


   for col_num in range(len(row[row_num])):
    s+=row[row_num][col_num] #each row, left to right
    c+=row[col_num][row_num] #each column, downward

    s_left=s[::-1] #reverse row, right to left
    c_up=c[::-1] #reverse column, down to up
    
  
   result_row=s.find(line) #search each row, left to right
   result_lrow=s_left.find(line) #search each row, right to left
   result_col=c.find(line) #search each column, downward
   result_upcol=c_up.find(line) # search each column, upward
  
   
 

   if result_row!=-1:
    out_file.write('{:<12}  {:>12}  {:>12}'.format(line,row_num+1, result_row+1))
    out_file.write('\n')
    match=False

   if result_lrow!=-1:
    
    out_file.write('{:<12}  {:>12}  {:>12}'.format(line,row_num+1, len(s_left)-result_lrow))
    out_file.write('\n')
    match=False
  
  
   if result_col!=-1:
    out_file.write('{:<12}  {:>12}  {:>12}'.format(line,result_col+1, row_num+1))
    out_file.write('\n')
    match=False

   
   if result_upcol!=-1:
    out_file.write('{:<12}  {:>12}  {:>12}'.format(line,result_col+1, len(c_up)-result_upcol))
    out_file.write('\n')
    match=False

   
  if(match==True):
   out_file.write('{:<12}  {:>12}  {:>12}'.format(line,0,0))
   out_file.write('\n')
   
 
def main():
 global in_file
 in_file=open('hidden.txt','r')
 global line
 line=in_file.readline()
 line=line.strip()
 l=line.split()
 global n_line
 n_line=int(l[0])
 global n_char
 n_char=int(l[1])
 global out_file
 out_file=open('found.txt','w')
 word_search(n_line, n_char)
 in_file.close()
 out_file.close()
main()