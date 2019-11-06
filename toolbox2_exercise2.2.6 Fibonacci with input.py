# Import a module to perform more math
import math


# Request an input from the user, this can only be a number
number = int(input("Give a number for N: "))

# Root5 is often used, so it's put here as a variable
root5  = math.sqrt(5)

# Splitting up the Fibonacci formula into a, b and c
a = (1 + root5)**number
b = (1 - root5)**number
c = 2**number * root5

# Calculating the Fibonacci formula
answer = int((a-b)/c)

#Giving the answer
print("When N is", number, "the Fibonacci number is:", answer)
    
