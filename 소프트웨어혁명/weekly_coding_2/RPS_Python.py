from random import randint

# You can view Swift Language Version at https://github.com/pookjw/univ_assignment/tree/master/소프트웨어혁명

class RPS:
    def __init__(self, count):
        self.count = count # Int
        self.player_won_count = 0
        self.computer_won_count = 0
        self.draw_count = 0
    
    def played_count(self): # Total
        return self.player_won_count + self.computer_won_count + self.draw_count

    def play(self, player_case): # player_case is Int (0, 1, 2) or String (Draw)
        if self.played_count() == self.count: # If played all games...
            print('Already played all games!')
        elif player_case != 0 and player_case != 1 and player_case != 2: # If user input is not 0 or 1 or 2...
            print('Invalid player case!')
        else:
            computer_case = randint(0, 2)
            case_array = [computer_case, player_case]
            case_array.sort()
            
            print('Player case is', end=" ")
            if player_case == 0:
                print('Rock.')
            if player_case == 1:
                print('Scissor.')
            if player_case == 2:
                print('Paper.')

            print('Computer case is', end=" ")
            if computer_case == 0:
                print('Rock.')
            if computer_case == 1:
                print('Scissor.')
            if computer_case == 2:
                print('Paper.')
            

            def result(win_case):
                if win_case == 'Draw':
                    print('Draw!')
                    self.draw_count += 1
                elif computer_case == win_case:
                    print('Computer win!')
                    self.computer_won_count += 1
                elif player_case == win_case:
                    print('Player win!')
                    self.player_won_count += 1
                
                print('### Total ###')
                print('Player won:', self.player_won_count)
                print('Computer won:', self.computer_won_count)
                print('Draw:', self.draw_count)
                print('#############')
                
                if self.played_count() == self.count:
                    if self.player_won_count > self.computer_won_count:
                        print('Game Over! Player win!')
                    elif self.computer_won_count > self.player_won_count:
                        print('Game Over! Computer win!')
                    else:
                        print('Game Over! Draw!')

            if case_array[0] == case_array[1]:
                result('Draw')
            elif case_array[0] == 0 and case_array[1] == 1:
                result(0)
            elif case_array[0] == 0 and case_array[1] == 2:
                result(2)
            elif case_array[0] == 1 and case_array[1] == 2:
                result(1)

try:
    count = input('[1] How many times do you want to play? --> ')
except KeyboardInterrupt: # Press Ctrl + C
    print('You cancelled the operation.')
else:
    rps = RPS(int(count))
    while True:
        print('(Rock: 0, Scissor: 1, Paper: 2)')
        try:
            case = input('[2] Enter case as integer. --> ')
        except KeyboardInterrupt: # Press Ctrl + C
            print('You cancelled the operation.')
            break

        rps.play(int(case))
        if rps.count == rps.played_count():
            try:
                answer = input('[3] Do you want to continue? (yes/no) --> ')
            except KeyboardInterrupt: # Press Ctrl + C
                print('You cancelled the operation.')
                break
            else:
                if answer.lower() == 'yes':
                    rps = RPS(int(count))
                else:
                    print('Bye!')
                    break
        
