import random

quess = random.randint(1, 20)

print("Hello! What is your name?")
in1 = input("")
print = in1

s1 = "Well, KBTU, I am thinking of a number between 1 and 20."
print(s1)
s2 = "Take a guess."
print(s2)

while True:
    i = 1
    n = int(input(""))
    if n == guess:
        print("Good job, KBTU! You guessed my number in  guesses!")
        break
    print("Take a guess.")
    i += 1
