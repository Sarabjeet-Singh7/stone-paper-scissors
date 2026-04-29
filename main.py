from stone_paper import play_game

def game_start():
    while True:
        print("1. Play Stone Paper Scissors")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Thank You for Playing the Game")
            break
        else:
            print("Invalid choice! Try again.")

game_start()