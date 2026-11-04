from commands import process_command
from locations import create_rooms, show_status
from player import Player


def play_game(name):
    player = Player(name)
    rooms = create_rooms()

    print(f"\nWelcome to Mystery Island, {name}!")
    print("Find the rope in the Jungle and the lantern in the Cave.")
    print("Reach the Lighthouse and light the beacon to escape.")
    print(f"Each move costs 1 energy. You start with {player.energy} energy.")

    while True:
        show_status(player, rooms)
        command = input("> ").strip().lower()
        result = process_command(command, player, rooms)

        if result == "quit":
            print("Thanks for playing!")
            return "quit"

        if result == "win":
            print(f"Congratulations, {player.name}! You escaped Mystery Island!")
            return "win"

        if result == "moved":
            player.energy -= 1
            if player.energy <= 0:
                player.energy = 0
                print("You are out of energy... Game over!")
                return "game_over"
            print(f"You have {player.energy} energy left.")


def main():
    print("Mystery Island — loading...")
    name = input("What is your name? ").strip() or "Explorer"

    while True:
        outcome = play_game(name)
        if outcome == "quit":
            break
        elif outcome in ("win", "game_over"):
            answer = input("Play again? (yes/no): ").strip().lower()
            if answer not in ("yes", "y"):
                print("Thanks for playing!")
                break
        else:
            break


if __name__ == "__main__":
    main()
