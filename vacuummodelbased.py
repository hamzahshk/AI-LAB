agent_model = {
    "A": "Unknown",
    "B": "Unknown"
}
agent_location = "A"

environment = {
    "A": "Dirty",
    "B": "Dirty"
}

def perceive(status):
    agent_model[agent_location] = status

def decide_action():
    if agent_model[agent_location] == "Dirty":
        return "Suck"
    elif agent_location == "A":
        return "Move Right"
    elif agent_location == "B":
        return "Move Left"
    return "NoOp"

def perform_action(action):
    global agent_location
    
    if action == "Suck":
        agent_model[agent_location] = "Clean"
    elif action == "Move Right":
        agent_location = "B"
    elif action == "Move Left":
        agent_location = "A"

for i in range(4):
    status = environment[agent_location]

    print("Location:", agent_location)
    print("Status:", status)

    perceive(status)
    action = decide_action()

    print("Action:", action)
    perform_action(action)

    if action == "Suck":
        environment[agent_location] = "Clean"

    print()