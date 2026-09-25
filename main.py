import random
from game_data import data
import art
print(art.logo)
first = random.choice(data)
data.remove(first)
second = random.choice(data)
data.remove(second)


print(f"Compare A: {first["name"]}, a {first["description"]}, from {first['country']}")
follower_A = first["follower_count"]

print(art.vs)
print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}")
follower_B = second["follower_count"]

score = 0
game_over = False

A_or_B = input("Who has more followers? Type 'A' or 'B'? ").upper()
if A_or_B == "A" and follower_A > follower_B:
    score += 1
elif A_or_B == "B" and follower_B > follower_A:
    score += 1
elif A_or_B == "A" and follower_A < follower_B:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = True
elif A_or_B == "B" and follower_B < follower_A:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = True
while not game_over:
    print(f"You're right! Current score: {score}")
    follower_A = follower_B
    follower_B = second["follower_count"]
    first = second
    second = random.choice(data)
    print(art.logo)
    print(f"Compare A: {first["name"]}, a {first["description"]}, from {first['country']}")
    print(art.vs)
    print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}")
    A_or_B = input("Who has more followers? Type 'A' or 'B'? ").upper()
    if A_or_B == "A" and follower_A > follower_B:
        score += 1
    elif A_or_B == "B" and follower_B > follower_A:
        score += 1
    else:
        print(f"Sorry, that's wrong. Your final score was: {score}")
        game_over = True