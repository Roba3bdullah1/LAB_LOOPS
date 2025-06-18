
# Using range() to generate sequence form 45 to 210
numbers= range(45,210)

# Create for loop 
for num in numbers: 
    if num == 100:
        continue
    elif num == 205:
        break
    print(num)


print(" "*15)
print("Question 2 ")
print(" "*15)


# Using while loop 
while True:
    # Ask user
    result = int(input("what is the product of 7 * 24 ? "))
    # Cheak if answer is right or woring
    if result == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")