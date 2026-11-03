# Mystery Island

Mystery Island is a text-based adventure game built with standard Python. Stranded on a mysterious island, the player must explore five locations, collect the rope and lantern, and reach the Lighthouse to light its beacon and signal for rescue.

## How to Run

Requires Python 3.

```bash
python3 main.py
```

## Game Rules

- **Goal:** Collect the **rope** from the Jungle and the **lantern** from the Cave, travel to the Lighthouse, and type `light beacon` to win.
- **Energy:** You start with **5 Energy**. Moving to a new location costs **1 Energy**. If your Energy reaches **0**, the game ends in a Game Over.
- **Taking items:** Use `take [item]` to pick up an item available in the current room, such as `take rope` or `take lantern`.
- **Locations:** Beach (starting location), Jungle, Cave, Old Bridge, and Lighthouse.
- **Available actions:** Each room displays the actions you can take there, such as `[Jungle] Actions: quit, go beach, go cave, take rope`.
- **Quitting:** Type `quit` to end the current game.
- **Play again:** After a win, game over, or quit, type `yes` when prompted to start a new game.

### Winning Route

```text
go jungle
take rope
go cave
take lantern
go old bridge
go lighthouse
light beacon
```

## Project Structure

- `main.py` — Entry point and game controller. Handles the player name prompt, main game loop, energy costs, win/game-over results, and the play-again loop.
- `player.py` — Defines the `Player` class, including name, current location, inventory, and starting Energy.
- `locations.py` — Defines the five rooms, their connections, available items, room-specific actions, and status display.
- `commands.py` — Parses and processes player commands such as `go`, `take`, `inventory`, `light beacon`, and `quit`.
- `DESIGN.txt` — Project design document covering the game goal, modular architecture, state variables, and game loop.

The code is intentionally modular: game flow lives in `main.py`, player state in `player.py`, world data and presentation in `locations.py`, and input handling in `commands.py`.
