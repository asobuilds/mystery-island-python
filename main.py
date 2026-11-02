from locations import show_status, search_scene
from commands import go, build_raft
from player import inventory, invalid_commands, has_torch, items, cave_searched, current_scene

print("Mystery Island — loading...")
print("Welcome to Mystery Island!")
print("You are stranded on a mysterious island.")
print("Collect wood, rope, and sail to build a raft and escape!")

while True:
    show_status(current_scene, inventory)
    command = input("> ").lower().strip()

    if command == "quit":
        print("Thanks for playing!")
        break
    elif command == "search":
        items, inventory, cave_searched = search_scene(current_scene, inventory, items, cave_searched, has_torch)
    elif command.startswith("go "):
        destination = command[3:].strip()
        current_scene, has_torch, game_over = go(destination, current_scene, inventory, has_torch)
        if game_over:
            break
    elif command == "inventory":
        print("Your inventory: " + (", ".join(inventory) if inventory else "empty"))
    elif command == "build":
        if build_raft(items):
            break
    else:
        invalid_commands += 1
        print("Unknown command. Try: search, go [scene], inventory, build, quit")
        if invalid_commands >= 3:
            print("You've used too many invalid commands. Game over!")
            break
