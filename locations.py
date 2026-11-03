import random


def show_status(current_scene, inventory):
    print(f"\n--- You are at the {current_scene} ---")
    print(f"Inventory: {inventory if inventory else 'empty'}")
    print("Available commands: search, go [scene], inventory, build, quit")
    print("Scenes you can go to: beach, jungle, cave")
    print("Note: you need a torch to survive the dark cave!")


def search_scene(current_scene, inventory, items, cave_searched, has_torch):
    if current_scene == "beach":
        found = random.choice(["wood", "sail"])
        if found in items and items[found]:
            print("You already collected the " + found + " earlier!")
        else:
            items[found] = True
            inventory.append(found)
            print("You found a " + found + "!")
    elif current_scene == "jungle":
        found_any = False
        for option in ["rope", "torch"]:
            if not (option in items and items[option]):
                items[option] = True
                inventory.append(option)
                print("You found a " + option + "!")
                found_any = True
        if found_any:
            print("The torch will light your way through the dark cave!")
        else:
            print("You already collected everything available in the jungle!")
    elif current_scene == "cave":
        if not has_torch:
            print("It is too dark! You need a torch to search the cave.")
        elif cave_searched:
            print("You already searched this cave!")
        else:
            cave_searched = True
            print("You explore the cave and find some interesting artifacts.")

    return items, inventory, cave_searched
