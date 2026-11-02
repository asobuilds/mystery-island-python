# Mystery Island — Learn2Earn Python Project

A text-based adventure game built in Python for the Learn2Earn Easy Challenge. The player is stranded on a mysterious island and must collect materials to build a raft and escape.

## How to Play

1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the game from your terminal:
   ```bash
   python main.py
Game Rules
Goal: Collect wood, rope, sail, and a torch to survive the cave and build your raft.

Commands: Type commands into the terminal and press Enter.

search — Look around the current scene for items.

go [scene] — Move to a new location (e.g., go jungle, go beach, go cave).

inventory — Check what items you are currently carrying.

build — Attempt to build the raft (requires wood, rope, and sail).

quit — Exit the game.

Lose Conditions: Entering the cave without a torch, or typing 3 invalid commands.

Project Structure
This project uses a modular file structure to separate concerns and keep the codebase readable:

main.py — The entry point containing the main game loop.

player.py — Manages the player's state, inventory, and variables.

locations.py — Contains the scene descriptions and search logic.

commands.py — Handles the logic for processing user inputs and player movement.

text

### Step 2: Commit and Push
Once you have pasted that and saved the file, go to your terminal and run:

```bash
git add README.md
