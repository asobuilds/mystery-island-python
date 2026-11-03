from locations import get_actions


def process_command(command, player, rooms):
    command = command.strip().lower()
    if not command:
        print("Please type a command.")
        return "continue"

    parts = command.split()
    verb = parts[0]

    if verb == "quit":
        return "quit"

    if verb == "inventory":
        inventory = ", ".join(player.inventory) if player.inventory else "empty"
        print("Your inventory: " + inventory)
        return "continue"

    if verb == "go":
        if len(parts) < 2:
            print("Go where? Try 'go jungle'.")
            return "continue"
        return _go(" ".join(parts[1:]), player, rooms)

    if verb == "take":
        if len(parts) < 2:
            print("Take what?")
            return "continue"
        return _take(" ".join(parts[1:]), player, rooms)

    if verb == "light":
        if len(parts) != 2 or parts[1] != "beacon":
            print("What do you want to light? Try 'light beacon'.")
            return "continue"
        return _light_beacon(player, rooms)

    actions = ", ".join(get_actions(player.current_scene, rooms))
    print("Unknown command. Actions here: " + actions)
    return "continue"


def _go(destination, player, rooms):
    destination = destination.strip().lower()
    room = rooms[player.current_scene]

    if destination not in room["connections"]:
        print(f"You can't go to {destination.title()} from here.")
        return "continue"

    player.current_scene = destination
    print(f"You travel to the {rooms[destination]['name']}.")
    return "moved"


def _take(item, player, rooms):
    item = item.strip().lower()
    room = rooms[player.current_scene]

    if item not in room["items"]:
        print(f"There is no {item} here to take.")
        return "continue"

    room["items"].remove(item)
    player.add_item(item)
    print(f"You take the {item}.")
    return "continue"


def _light_beacon(player, rooms):
    if player.current_scene != "lighthouse":
        print("There is no beacon here to light.")
        return "continue"

    missing = [item for item in ("rope", "lantern") if not player.has_item(item)]
    if missing:
        print("The beacon needs a rope and a lantern. Missing: " + ", ".join(missing) + ".")
        return "continue"

    print("You tie the rope, raise the lantern, and light the beacon!")
    print("Its light cuts through the darkness. A rescue ship is on its way!")
    return "win"
