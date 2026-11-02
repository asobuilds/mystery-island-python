def go(destination, current_scene, inventory, has_torch):
    if destination == current_scene:
        print("You are already at the " + destination + "!")
        return current_scene, has_torch, False

    if destination == "cave" and "torch" not in inventory:
        print("You enter the cave... but it is pitch black!")
        print("You trip and fall. Game over!")
        return current_scene, has_torch, True

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
    return current_scene, has_torch, False


def build_raft(items):
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
