game = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]              #list

print('     a  b  c')

def game_board():
    for count, row in enumerate(game):
        print(count, row)
    # for item in row:
    #     print(item)
game[0][1] = 1

game_board()