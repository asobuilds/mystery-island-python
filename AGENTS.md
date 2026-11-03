# Mystery Island

## Project

Mystery Island — a modular text-based adventure game. Entry point: `main.py`.

## Run

```bash
python3 main.py
```

## File Structure

- `main.py` — Entry point and game loop; handles the player name, energy system, win/game-over results, and play-again flow.
- `player.py` — Player state: name, current location, inventory, and starting Energy.
- `locations.py` — Room definitions, connections, items, available actions, and status display.
- `commands.py` — Command parsing and action handling for movement, item pickup, inventory, beacon lighting, and quitting.
- `DESIGN.txt` — Project design document.

## Agent Rules

- Keep the game modular across the four Python files: `main.py`, `player.py`, `locations.py`, and `commands.py`.
- Ensure new commands update the command handling in `commands.py` and the room actions in `locations.py`.
- The player must always have a win condition (lighting the beacon with the rope and lantern) and a lose condition (reaching 0 Energy).
- Stick to standard Python; do not introduce external dependencies.
