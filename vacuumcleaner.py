environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Model (memory)
model = {
    "A": "Unknown",
    "B": "Unknown"
}

# Obstacles
obstacles = {
    "A": False,
    "B": False
}

location = "A"

for i in range(4):

    status = environment[location]

    # Perceive and update model
    model[location] = status

    print("Location:", location)
    print("Status:", status)

    # Decide action
    if status == "Dirty":
        action = "Suck"

    elif location == "A":
        if obstacles["B"]:
            action = "NoOp"
        else:
            action = "Move Right"

    elif location == "B":
        if obstacles["A"]:
            action = "NoOp"
        else:
            action = "Move Left"

    print("Action:", action)

    # Perform action
    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    print()