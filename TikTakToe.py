#class oriented tik tak toe

import random

class TikTakToe:
    field = ["1", "2", "3",
            "4","5","6",
            "7", "8", "9"]
    moves = []
    status = -1
    move_command = 0
    winner = "Even"
        
    
    def __init__(self, player_one, player_two):
        random_start = random.randint(0,100)
        if random_start % 2 == 0:
            self.player_one = player_one
            self.player_two = player_two
        else:
            self.player_one = player_two
            self.player_two = player_one
        
        
    def __len__(self):
        return len(self.moves)
    
    
    def __getitem__(self, position):
        return self.moves[position]
    
    
    def __str__(self):
        return "{} | {} | {}\n- + - + -\n{} | {} | {}\n- + - + -\n{} | {} | {}\n".format(
            self.field[0], self.field[1], self.field[2], 
            self.field[3],self.field[4], self.field[5], 
            self.field[6],self.field[7], self.field[8])
    
    
    def check_input(self):
        try:
            self.move_command = int(self.move_command)
            if (self.move_command < 1) | (self.move_command > 9):
                self.move_command = None
        except:
            self.move_command = None
    
    
    def next_move(self):
        if self.move_command in self.moves:
            print("This field is already taken!")
        else:
            if self.get_turn() == self.player_one:
                self.field[self.move_command - 1] = "X"
                self.moves.append(self.move_command)
            else:
                self.field[self.move_command - 1] = "O"
                self.moves.append(self.move_command)
                
            
    def get_status(self):
        if(self.field[0] == self.field[1] == self.field[2]):
            self.status = self.field[0]   
        elif(self.field[3] == self.field[4] == self.field[5]):
            self.status = self.field[3] 
        elif(self.field[6] == self.field[7] == self.field[8]):
            self.status = self.field[6] 
        elif(self.field[0] == self.field[3] == self.field[6]):
            self.status = self.field[0]   
        elif(self.field[1] == self.field[4] == self.field[7]):
            self.status = self.field[1]   
        elif(self.field[2] == self.field[5] == self.field[8]):
            self.status = self.field[2]   
        elif(self.field[0] == self.field[4] == self.field[8]):
            self.status = self.field[0]   
        elif(self.field[2] == self.field[4] == self.field[6]):
            self.status = self.field[2]   
        else:
            self.status = -1
    
    
    def get_turn(self):
        if ((len(self) % 2) == 1 | (len(self) == 0)):
            return self.player_two
        else:
            return self.player_one
        
    
    def get_winner(self):
        if self.status != -1:
            if (len(self) - 1) % 2 == 0:
                self.winner = self.player_one   
            else:
                self.winner = self.player_two
            print("***The Winner is: {}!***".format(self.winner))
        else:
            self.winner = "Even"
            print("The game is even")
            
            
    def get_bot_move(self):
        options = []
        for position, value in enumerate(self.field):
            if(("X" not in self.field[position]) & ("O" not in self.field[position])):
                options.append(position + 1)
                
        options_length = len(options)
        if options_length > 1:
            self.move_command = options[random.randrange(0,options_length - 1)]
        else:
            self.move_command = options[0]
                    
   
    def get_move(self):
        if self.get_turn() != "Bot":
            self.move_command = input("{} please set your next move...: ".format(self.get_turn()))
            self.check_input()
        else:
            self.get_bot_move()
            print("The Bot takes {}".format(self.move_command))
         
            
    def make_move(self):
        if isinstance(self.move_command, int):
            if self.move_command not in self.moves:
                self.next_move()
                self.get_status()
                print(self)
            else:
                print("This move was already taken! ")
        else:
            print("Your Input must be an Integer between 1 and 9")
            
            
    def run_game(self):
        print(self)
        while self.status == -1:
            self.get_move()
            self.make_move()
                
        self.get_winner()
        

def main():
    game_runs = True
    inputs = True
    while game_runs:
        bot = input("Do you want to play against a bot?([y/n])")
        if bot == "n":
            while inputs:
                player_one = input("Please input your name Player One (X)...:")
                player_two = input("Please input your name Player Two (O)...:")
                inputs = False
        else:
            while inputs:
                player_one = input("Please input your name Player...:")
                player_two = "Bot"
                inputs = False
                
        new_game = TikTakToe(player_one, player_two)
        new_game.run_game()   
        game_runs = False
        
main()
    