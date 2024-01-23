import random

options = ('piedra', 'papel', 'tigera')


rounds = 1

def choose_options():
  options = ('piedra', 'papel', 'tigera')
  user_option = input('Piedra, papel o tijera => ')
  user_option= user_option.lower()
  
  if not user_option in options:
    print('Opcion invalida')
    #continue
    return None, None
  
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer Options', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins ,computer_wins ):
  if (user_option == computer_option):
    print('Empate')
  elif (user_option =='piedra'):
    if (computer_option == 'tigera'):
      print('piedra gana a tijera')
      print('user gana')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano')
      computer_wins +=1
  elif (user_option == 'papel'):
    if computer_option =='piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano')
      computer_wins +=1
  elif (user_option == 'tijera'):
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computer_wins +=1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

while True:

  print('*'*10)
  print('ROUND', rounds)
  print('*'*10)

  print('vitorias usuario', user_wins)
  print('vitorias computer', computer_wins)
  rounds += 1

  user_option, computer_option = choose_options()
  user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
  
  

  if computer_wins ==2:
    print('El ganador definitivo es la computadora')
    break
  if user_wins ==2:
    print('El ganador definitivo es la usuario')
    break

run_game()