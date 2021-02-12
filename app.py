import copy
import constants
import statistics
import sys
teams_copy = copy.deepcopy(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)

experienced_players = []
nonexperienced_players = []
guardians_list = []
panth_height = []
bandit_height = []
warriors_height = []
# turns height into an integer
def clean_height():
  for player in players_copy:
    height_int = player['height'][0:2]
    player['height'] = int(height_int)
  
# removes the and from the guardains and makes it a list
def clean_guardians():
  for player in players_copy:
    player['guardians'] = player['guardians'].split(' and ')  

  # turns experience into a boolean value and adds it to two lists
def clean_experience():
  for player in players_copy:
    if player['experience']== 'YES':
      player['experience']== True
      experienced_players.append(player)
    elif player['experience'] == 'NO':
      player['experience'] == False
      nonexperienced_players.append(player)

#gets average height for each team  
  
def avg_height_tool():
  

  for dictionary in Panthers:
    for key in dictionary:
      if key == 'height':
        panth_height.append(dictionary['height'])
        
  avg_panth = statistics.mean(panth_height)  
  
  
  for dictionary in Bandits:
    for key in dictionary:
      if key == 'height':
        bandit_height.append(dictionary['height'])
        
  avg_bandit = statistics.mean(bandit_height)
  
  
  for dictionary in Warriors:
    for key in dictionary:
      if key == 'height':
        warriors_height.append(dictionary['height'])
        
  avg_warriors = statistics.mean(warriors_height)

# start menu for program  
def start_menu():
  while True:
    
  
    print('BASKETBALL STATISTICS TOOL 5.0')
    print('\n')
    print('=====MENU========')
    print('\n')
    print('A: DISPLAY TEAM STATISTICS')
    print('B: QUIT PROGRAM')
    
    option_choice_one = input('Enter an option please:  ')
    
    while True:
      try: 
        if option_choice_one.upper() == 'A':
          print('\n')
          print('A. Panthers')
          print('\n')
          print('B. Bandits')
          print('\n')
          print('C. Warriors')
          break
        elif option_choice_one.upper() == 'B':
          print('GOODBYE')
          sys.exit()
      except ValueError:
        
        print('Please input a valid choice')
        continue
    
    print('\n')
    option_choice_two = input('Please Choose a team    ')
        
    while True:
      
      try:
        
        if option_choice_two.upper() == 'A':
          print('YOU HAVE CHOSEN THE PANTHERS!!')
          print('THERE ARE',num_of_panthers, 'PLAYERS')
          print('PLAYERS ON TEAM')
          for player in Panthers:
            print (player['name'], end=' , ')
          print('\n')  
          print('AVERAGE PLAYER HEIGHT')  
          print(avg_panth)
          print('\n')  
          print('GUARDIANS')
          for player in Panthers:
            print(player['guardians'], end = ' , ')
          break
        elif option_choice_two.upper() == 'B':
          print('YOU HAVE CHOSEN THE BANDITS!!')
          print('THERE ARE',num_of_bandits, 'PLAYERS')
          print('\n')  
          print('AVERAGE PLAYER HEIGHT')  
          print(avg_bandit)
          print('\n') 
          print('PLAYERS ON TEAM')
          for player in Bandits:
            print (player['name'], end=' , ')
          print('\n')   
          print('GUARDIANS')
          for player in Bandits:
            print(player['guardians'], end = ' , ')  
          
          # average height
          break
        elif option_choice_two.upper() == 'C':
          print('YOU HAVE CHOSEN THE WARRIORS!!')
          print('THERE ARE',num_of_warriors, 'PLAYERS')
          print('\n')  
          print('AVERAGE PLAYER HEIGHT')  
          print(avg_warriors)
          print('\n') 
          print('PLAYERS ON TEAM')
          for player in Warriors:
            print (player['name'], end=' , ')
          print('\n')   
          print('GUARDIANS')
          for player in Warriors:
            print(player['guardians'], end = ' , ')   
          
          break
      except ValueError:
        print('Please enter a valid option. Ex: A,B,C')
        continue
  
    print('\n')
    answerr = input(('Would you like to continue the program?    Y/N'))
    if answerr.upper() == 'Y':
      continue
    elif answerr.upper() == 'N':
      print('goodbye!')
      sys.exit()
        

      
      
      
      
      
      
#program starts here      
      
      
if __name__ == "__main__":
  
  clean_height()  
  clean_guardians()
  clean_experience()
  
  teams_copy[0] = experienced_players[0:3] + nonexperienced_players [0:3]
  
  teams_copy[1] = experienced_players[3:6] + nonexperienced_players [0:3]
  
  teams_copy[2] = experienced_players[6:9] + nonexperienced_players [0:3]
  
  #may have been an unnecesary step that complicates this a lot
  Panthers = teams_copy[0]
  Bandits  = teams_copy[1]
  Warriors = teams_copy[2]
   
  num_of_panthers = len(Panthers)
  num_of_bandits = len(Bandits)
  num_of_warriors = len(Warriors)
    
  

  for dictionary in Panthers:
    for key in dictionary:
      if key == 'height':
        panth_height.append(dictionary['height'])
        
  avg_panth = statistics.mean(panth_height)  
  
  
  for dictionary in Bandits:
    for key in dictionary:
      if key == 'height':
        bandit_height.append(dictionary['height'])
        
  avg_bandit = statistics.mean(bandit_height)
  
  
  for dictionary in Warriors:
    for key in dictionary:
      if key == 'height':
        warriors_height.append(dictionary['height'])
        
  avg_warriors = statistics.mean(warriors_height)
  
  start_menu() 