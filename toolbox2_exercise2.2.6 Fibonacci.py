import math


for reeks in range(11):
    n = reeks
    
    root5  = math.sqrt(5)
    a = (1 + root5)**n
    b = (1 - root5)**n
    c = 2**n * root5
    answer = int((a-b)/c)
    print("When n is", reeks, "the Fibonacci number is:", answer)
    
print("Done :)")