# Prompts the user for a positive integer
n = int(input("Enter a positive integer: "))

# Cheak if the number is positive integer
if n >= 0 :
    # create virable 
    sum:int=0
    # using range() 
    evenNum = range(1,n+1)
    # using for loop to sum postive integer in sequence
    for i in evenNum:
        if i % 2 == 0:
            sum += i 
# print The result
print("The sum of even numbers between 1 to",n,"is",sum,".")

