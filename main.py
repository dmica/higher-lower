# Import logo and vs
from art import logo, vs
# Import game data
from game_data import data
# Import random
import random
# Import clear
from replit import clear


def random_data():
  """Get random account from data"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account['name']
  description = account['description']
  country = account['country']

  return f"{name}, a {description}, from {country}"

def check_answer(a_account, b_account, guess):
  """Checks for correct answer.""" 
  if a_account > b_account:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_data()
  account_b = random_data()

  while game_should_continue:
    account_a = account_b
    account_b = random_data()

    while account_a == account_b:
      account_b = random_data()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(a_follower_count, b_follower_count, guess)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
