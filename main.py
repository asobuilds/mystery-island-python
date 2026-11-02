import random

print("Mystery Island — loading...")


def show_status():
    print(f"\n--- You are at the {current_scene} ---")
    print(f"Inventory: {inventory if inventory else 'empty'}")
    print("Available commands: search, go [scene], inventory, build, quit")
    print("Scenes you can go to: beach, jungle, cave")


def search_scene():
    if current_scene == "beach":
        found = random.choice(["wood", "sail"])
        if found in items and items[found]:
            print("You already collected the " + found + " earlier!")
        else:
            items[found] = True
            inventory.append(found)
            print("You found a " + found + "!")
    elif current_scene == "jungle":
        if "rope" in items and items["rope"]:
            print("You already collected the rope earlier!")
        else:
            items["rope"] = True
            inventory.append("rope")
            print("You found a rope!")
    elif current_scene == "cave":
        if not has_torch:
            print("It is too dark! You need a torch to search the cave.")
        elif "torch" in inventory:
            print("You already searched this cave!")
        else:
            print("You find nothing of use here.")


def go(destination):
    global current_scene, has_torch
    if destination == current_scene:
        print("You are already at the " + destination + "!")
        return

    if destination == "cave" and not has_torch:
        print("You enter the cave... but it is pitch black!")
        print("You trip and fall. Game over!")
        return True

    if destination == "cave":
        has_torch_found = False
        if "torch" in inventory and not has_torch:
            has_torch = True
            has_torch_found = True

        if has_torch_found:
            print("You enter the cave with your torch. It is illuminated!")
        else:
            print("You enter the cave with your torch.")

    current_scene = destination
    print("You went to the " + current_scene + ".")


def build_raft():
    if items["wood"] and items["rope"] and items["sail"]:
        print("\nYou build a raft with all the materials!")
        print("You sail away from the island. You escaped!")
        print("Congratulations — you win!")
        return True
    else:
        missing = []
        if not items["wood"]:
            missing.append("wood")
        if not items["rope"]:
            missing.append("rope")
        if not items["sail"]:
            missing.append("sail")
        print("You need: " + ", ".join(missing) + " to build a raft!")
        return False


# Game state
current_scene = "beach"
inventory = []
invalid_commands = 0
has_torch = False
items = {"wood": False, "rope": False, "sail": False}

print("Welcome to Mystery Island!")
print("You are stranded on a mysterious island.")
print("Collect wood, rope, and sail to build a raft and escape!")

while True:
    show_status()
    command = input("> ").lower().strip()

    if command == "quit":
        print("Thanks for playing!")
        break
    elif command == "search":
        search_scene()
    elif command.startswith("go "):
        destination = command[3:].strip()
        if go(destination):
            break
    elif command == "inventory":
        print("Your inventory: " + (", ".join(inventory) if inventory else "empty"))
    elif command == "build":
        if build_raft():
            break
    else:
        invalid_commands += 1
        print("Unknown command. Try: search, go [scene], inventory, build, quit")
        if invalid_commands >= 3:
            print("You've used too many invalid commands. Game over!")
            break
