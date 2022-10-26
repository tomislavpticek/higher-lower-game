from replit import clear
import art, game_data, random

def reset_screen():
  clear()
  print(art.logo)

def get_data(compare, correct_choice):
  choices = []
  if(len(compare) == 2):
    choices.append(compare.pop(correct_choice))
    item = {}
    while True:
      item = game_data.data[random.randint(0, len(game_data.data)-1)]

      if(item["name"] != choices[0]["name"]):
        break
    choices.append(item)
    return choices
    
  else:
    item = {}
    while True:
      item = game_data.data[random.randint(0, len(game_data.data)-1)]
      if(len(choices) == 0):
        choices.append(item)
      elif(item["name"] != choices[0]["name"]):
        choices.append(item)
        break
    return choices
    

def game():
  reset_screen()

  compare = []
  alive = True
  count = 0
  correct_choice = 0
  while alive:
    
    compare = get_data(compare, correct_choice)
    print

    print(f"A: {compare[0]['name']}, {compare[0]['description']} from {compare[0]['country']}")
    print(art.vs)
    print(f"B: {compare[1]['name']}, {compare[1]['description']} from {compare[1]['country']}")

    guess = ""
    while guess not in ["A", "B"]:
      guess = input("\nWho has more followers? Type A or B for an answer: ")

    if(guess == "A"):
      if(compare[0]["follower_count"] >= compare[1]["follower_count"]):
        correct_choice = 0
        count +=1
        reset_screen()
      else:
        alive = False
    elif(guess == "B"):
      if(compare[0]["follower_count"] <=  compare[1]["follower_count"]):
        correct_choice = 1
        count +=1
        reset_screen()
      else:
        alive = False
       
  print(f"\nAh, that one was wrong but you still got the score of {count} and you should feel good about that.")
  
playing = True
while playing:
  game()
  response =""
  while response not in ["N", "Y"]:
    response = input("Would you like to play again? Enter 'Y' for yes and 'N' for no: ")
  if(response == "N"):
    playing = False
    print("Thank you for playing, goodbye.")


