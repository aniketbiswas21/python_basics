game = 'I just want to play the game'    
print(id(game))


def game_board(player=0, row=0, column=0, just_display= False):
   global game
   game = 'OK' 
   print(id(game))
   print(game)
   
# print(game)
game_board()