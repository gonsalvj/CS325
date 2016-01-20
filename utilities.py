class utilities(object):

   def load():
      problems = []
      with open('MSS_Problems.txt') as f:
         for line in f:
            if line == '' or line[0] == '#' or line[0] == '\n':
               continue
            line = line.replace('[', '').replace(']', '').replace(' ', '')
            problems.append([int(num) for num in line.split(',') if num not in '\n'])
      return problems

   def printtofile(algorithmtype, array, total):
      heading = "\n========" + algorithmtype + "========\n"
      maxsum = "Max sum of array is " + str(total) + "\n"
      values = array
      with open("MSS_Results.txt", "a") as myfile:
         myfile.write(heading)
         myfile.write(maxsum)
         myfile.write("Sub Array Values: ")
         for val in array:
            myfile.write(str(val) + " ")
         
