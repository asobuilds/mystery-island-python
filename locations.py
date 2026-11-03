def create_rooms():
    return {
        "beach": {
            "name": "Beach",
            "description": "Waves crash against the shore. A jungle path waits to the north, and an old bridge stretches along the coast.",
            "connections": ["jungle", "old bridge"],
            "items": [],
        },
        "jungle": {
            "name": "Jungle",
            "description": "Thick vines hang overhead. Something moves in the undergrowth, and a dark cave mouth waits nearby.",
            "connections": ["beach", "cave"],
            "items": ["rope"],
        },
        "cave": {
            "name": "Cave",
            "description": "The cave is cool and damp. A faint glint catches your eye in the shadows.",
            "connections": ["jungle", "old bridge"],
            "items": ["lantern"],
        },
        "old bridge": {
            "name": "Old Bridge",
            "description": "The weathered bridge creaks underfoot. The lighthouse rises beyond it.",
            "connections": ["beach", "cave", "lighthouse"],
            "items": [],
        },
        "lighthouse": {
            "name": "Lighthouse",
            "description": "The lighthouse tower stands against the sky. Its unlit beacon waits at the top.",
            "connections": ["old bridge"],
            "items": [],
        },
    }


def get_actions(current_scene, rooms):
    actions = ["quit"]
    room = rooms[current_scene]
    actions.extend("go " + destination for destination in room["connections"])
    actions.extend("take " + item for item in room["items"])
    if current_scene == "lighthouse":
        actions.append("light beacon")
    return actions


def show_status(player, rooms):
    room = rooms[player.current_scene]
    inventory = ", ".join(player.inventory) if player.inventory else "empty"
    actions = ", ".join(get_actions(player.current_scene, rooms))

    print(f"\n[{room['name']}] {room['description']}")
    print(f"Energy: {player.energy} | Inventory: {inventory}")
    print(f"[{room['name']}] Actions: {actions}")
