import random
import time

print("Number guessing game")
again = True
numbs = []
wins = 0
high_score = 1000
for n in range(1, 101):
    numbs.append(n)

while again:
    chances = 0
    selected = False
    while selected == False:
      print("""
      1: easy = 10 chances
      2: medium = 5 chances
      3: hard = 3 chances""")

      dif = int(input('select dificulty numbet: '))

      if dif == 1:
          chances = 10
          print('easy mode')
          selected = True
      elif dif == 2:
          chances = 5
          print('medium mode')
          selected = True
      elif dif == 3:
          chances = 3
          print('hard mode')
          selected = True
      else:
           print('invalid')

    comp_choice = random.choice(numbs)
    print('choosing number...')
    time.sleep(1)
    atempts = 1

    while chances > 0:
        choice = int(input('guess the number: '))
        if choice == comp_choice:
            wins += 1
            print(f"""congratulations you won!!!
it only took {atempts} atempts""")
            if atempts < high_score:
                high_score = atempts
            print(f'highest score: {high_score}')
            break
        elif choice != comp_choice:
            atempts += 1
            chances -= 1
            print('wrong answer')
            if choice > comp_choice:
                print('your guess is greater than the number')
            elif choice < comp_choice:
                print('your guess is lower than the number')
    if chances == 0:
        print('game over')
        if wins > 0:
            print(f'highest score: {high_score}')

    print('want to play again?')
    p_again = int(input('1:yes\n0:no'))
    if p_again == 0:
        again = False