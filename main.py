from utils.user import User
from utils.dice_game import DiceGame
from utils.user_manager import UserManager
import os

def main():
    user_manager = UserManager()
    
    while True:
        print("Welcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            user_manager.register()
        elif choice == '2':
            user = user_manager.login()
            if user:
                from utils.dice_game import DiceGame
                game = DiceGame()
                game.menu(user)
        elif choice == '3':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()