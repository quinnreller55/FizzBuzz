#Defines FizzBuzz function.
def FizzBuzz():
  #Iterates through numbers 1 to 100, and checks if divisible by 3 and 5.
  for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
#Executes function
FizzBuzz()
