import os
import random

class DiceGame:
    def __init__(self):
        self.stages = 3
        self.current_stage = 1
        self.player_score = 0
        self.total_points = 0
        self.scores_file = 'data/scores.txt'
        self.scores = []

    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if os.path.exists(self.scores_file):
            with open(self.scores_file, 'r') as file:
                self.scores = [line.strip().split(',') for line in file]
                self.scores = [(name, int(score)) for name, score in self.scores]
        else:
            self.scores = []

    def save_scores(self, username, score):
        self.scores.append((username, score))
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:10]
        with open(self.scores_file, 'w') as file:
            for name, score in self.scores:
                file.write(f'{name},{score}\n')

    def roll_dice(self):
        return random.randint(1, 6)

    def play_game(self, username):
        self.player_score = 0
        self.total_points = 0
        self.current_stage = 1
        print("Welcome to the Dice Roll Game!")
        while self.current_stage <= self.stages:
            print(f"\nStage {self.current_stage}")
            player_roll = self.roll_dice()
            cpu_roll = self.roll_dice()
            print(f"Your roll: {player_roll}")
            print(f"CPU's roll: {cpu_roll}")
            if player_roll > cpu_roll:
                print("You win this round!")
                self.player_score += 1
                self.total_points += 1
                print(f"Total points earned: {self.total_points}")
                print(f"Stages won: {self.player_score}")
            elif player_roll < cpu_roll:
                print("You lose this round!")
                print("Game over. You didn’t win any stages.")
                self.save_scores(username, self.total_points)
                return
            else:
                print("It's a tie! Rolling again...")
                continue
            if self.player_score == self.current_stage:
                print("You win this stage!")
                self.total_points += 3
            choice = input("Do you want to proceed to the next stage? (1 to continue, 0 to stop): ")
            while choice not in ['0', '1']:
                choice = input("Invalid input. Please enter 1 to continue or 0 to stop: ")
            if choice == '0':
                print(f"Exiting the game. Goodbye!")
                self.save_scores(username, self.total_points)
                return
            self.current_stage += 1
        if self.current_stage > self.stages:
            print("Congratulations! You won all stages!")
            print(f"Total points earned: {self.total_points}")
            print(f"Total stages won: {self.player_score}")
        self.save_scores(username, self.total_points)

    def show_top_scores(self):
        self.load_scores()
        if not self.scores:
            print("No scores available yet.")
            return
        print("Top 10 Highest Scores:")
        for i, (name, score) in enumerate(self.scores, start=1):
            print(f"{i}. {name}: {score}")

    def logout(self):
        print("Logging out...")

    def menu(self, username):
        while True:
            print("\nUser Menu:")
            print("1. Start Game")
            print("2. Show Top Scores")
            print("3. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.play_game(username)  
            elif choice == '2':
                self.show_top_scores()  
            elif choice == '3':
                self.logout()  
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game = DiceGame()
    game.menu("zxcv")  