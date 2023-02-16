import art
import random
print(art.logo)
a = [10, 7, 5]
ptr = input("Enter Difficulty 'Easy', 'Medium', 'Hard' : ")


def easy(difficulty):
    count = difficulty
    num = random.randint(1, 100)
    for i in range(int(difficulty)):
        guess = int(input("Enter the number betwewen 1 to 100:"))
        print(f"Number of Guess left are {count}")
        if guess < num:
            print("Number is low😏😏")
        elif guess > num:
            print("Number is High😏😏")
        elif guess == num:
            print("You win😁😁")
            return
        count = count-1
    print(f"Number of Guess left are {count}")
    print("You loose😂😂")
    return


def mediem(difficulty):
    count = difficulty
    num = random.randint(1, 100)
    for i in range(int(difficulty)):
        guess = int(input("Enter the number betwewen 1 to 100:"))
        print(f"Number of Guess left are {count}")
        if guess < num:
            print("Number is low😏😏")
        elif guess > num:
            print("Number is High😏😏")
        elif guess == num:
            print("You win😁😁")
            return
        count = count-1
    print(f"Number of Guess left are {count}")
    print("You loose😂😂")
    return


def hard(difficulty):
    count = difficulty
    num = random.randint(1, 100)
    for i in range(int(difficulty)):
        guess = int(input("Enter the number betwewen 1 to 100:"))
        print(f"Number of Guess left are {count}")
        if guess < num:
            print("Number is low😏😏")
        elif guess > num:
            print("Number is High😏😏")
        elif guess == num:
            print("You win😁😁")
            return
        count = count-1
    print(f"Number of Guess left are {count}")
    print("You loose😂😂")
    return


if ptr == 'Easy':
    easy(a[0])
elif ptr == 'Medium':
    mediem(a[1])
elif ptr == 'Hard':
    hard(a[2])
