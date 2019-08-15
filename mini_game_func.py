def path_choices():
    print("\n Which path should the king take?")
    print("type left(shortest path to king's room)")
    print("type right(Path leading to daughter's room)")
    print("type underground(Path leading to king's room)")

    path = input("> ")
    return path

def left_path():
    print("\n This path had too much spikes. After all Victor is human. He can't survive that much spikes.")
    print("\n GAME OVER!")

def right_path():
    print("\n This path consisted of poisonous gas trap. A human can't breathe in toxic atmosphere. King Victor died.")
    print("\n GAME OVER!")

def under_path():
    print("\n Okay so you are smart. King has safely reached his main room but has no weapons to face Camio. Now what?")

def plan_choices():
    print("\n How you want to progress further now?")
    print("Rush for the attack straight forward.(type rush)")
    print("Greed the Coral Leo.(type greed)")

    plan = input(">")

    return plan

def rush():
    print("\n You rushed in without a weapon. So, YOU DIED!")
    exit(0)

def greed_the_coral():
    print("\n Okay, you greeded coral and have got the weapon. Now you can attack Camio. Good CHOICE though!")

def camio_attacked():
    print("\n After that king headed to save his daughter. Victor finally killed Camio and saved his daughter.")

def the_end():
    print("\n \t\t\t----------------THANKYOU FOR PLAYING THE GAME--------------------")
