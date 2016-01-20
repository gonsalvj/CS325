from array import *
from utilities import utilities

def simpleenumeration(numbers): 
   maxsum = 0  
   startsubindex = endsubindex =  0   
   length = len(numbers)
   if(length == 1):
      utilities.printtofile("Simple Enumeration", numbers, numbers[0])
      return
  
   for i in range(0, length):
      currentsum = numbers[i]
      for j in range(i+1, length):
         currentsum += numbers[j]
         if currentsum > maxsum:
            maxsum = currentsum
            startsubindex = i
            endsubindex = j   
   utilities.printtofile("Simple Enumeration", numbers[startsubindex: endsubindex + 1], maxsum)
  
 
def betterenumeration(numbers):
   maxsum = 0  
   startsubindex = endsubindex =  0  
   length = len(numbers)
   if(length == 1):
      utilities.printtofile("Better Enumeration", numbers, numbers[0])
      return  

   for i in range(0, length):
      lastsum = 0     
      for j in range(i, length):
            if lastsum == 0:
                cursum = numbers[j]         
            else:
                cursum = lastsum + numbers[j]     

        
            if cursum >= maxsum:
                maxsum = cursum
                startsubindex = i
                endsubindex = j 
            
            lastsum = cursum
   
   utilities.printtofile("Better Enumeration", numbers[startsubindex: endsubindex + 1], maxsum)

def main():
   results = utilities.load()
   for line in results:
     simpleenumeration(line)
     betterenumeration(line)
   #    print("--------------------")

main()

