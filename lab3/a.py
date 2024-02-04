import random

name = input("Hello! What is your name? \n")


def guess():
    x = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    b = False
    i = 0
    while (b == False):
        print("Take a guess.")
        i += 1
        if (x == i):
            print(f"Good job, KBTU! You guessed my number in {i} guesses!")
            b = True
        elif (x > i):
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")


guess()


# import random
# def guess(s):
#     r=random.randint(1,20)
#     print(f"\nWell, {s}, I am thinking of a number between 1 and 20.")
#     b=False
#     i=0
#     while(b==False):
#         i+=1
#         n=int(input("Take a guess\n"))
#         if(r==n):
#             print(f"\nGood job, {s}! You guessed my number in {i} guesses!")
#             b=True
#         elif(r>n):
#             print("\nYour guess is too low.")
#         else:
#             print("\nYour guess is too high.")
# guess(input("Hello! What is your name? \n"))
