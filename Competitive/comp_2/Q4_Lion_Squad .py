def input_validation(message):
   while True:
      try:
         user_input = int(input(message))       
      except ValueError:
         print("Not an integer! Try again.")
         continue
      else:
         return user_input 

def shape(number):
   gap = number - 1

   for i in range(1, number + 1): # row traversal
      value = i
      
      for j in range(1, gap + 1): # print blank spaces
         print(" ", end = " ")
      gap = gap - 1
      
      for j in range(1, i +1): # printing until middle coloumn of triangle
         print(value % 10, end = " ")
         value = value + 1
      value = value - 2

      for j in range(1, i): # printing after middle coloumn of triangle
         print(value % 10, end = " ")
         value = value - 1
      print()

if __name__=="__main__":
    number = input_validation("Enter number:")
    shape(number)