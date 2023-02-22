import art
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_des}, from {account_country}"

def check_answers (guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"    
    else:
        return guess=="b"

print(art.logo)
score=0
game_should_countinue=True
account_b = random.choice(data)


while game_should_countinue:
    account_a = account_b
    account_b=random.choice(data)
    if (account_a == account_b):
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(account_b)}")

    guess=input("Who has more followers? Type 'A' or 'B':" ).lower()

    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correcct=check_answers(guess,a_follower_count,b_follower_count)
    if is_correcct:
        score+=1
        print(f"You're Right! Current Score {score}")
    else:
        game_should_countinue=False
        print(f"You're Wrong! Final Score is {score}")
