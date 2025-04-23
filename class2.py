# Nested if-elif statemenets:
marks = int(input("Enter your marks: "))
if marks >= 33:
    print("You passed the exam!")
    if marks >= 80:
        print("Grade: A+")
    elif marks >= 70:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("You failed the exam.")
    
'''output
Enter your marks:  67
You passed the exam!
Grade: B
'''    
#==========================================================
# List of fruits
fruits_list = ["Apple", "Banana", "Mango", "Orange"]

# For loop to print each fruit
for fruit in fruits_list:
    print("I like", fruit)

'''output
I like Apple
I like Banana
I like Mango
I like Orange
'''
#========================================================