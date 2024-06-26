def move_forward():
    print("moving forward")

def turn(direction: str):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("starting engine")

def follow_roundabout(exit_number: int):
    print(f"taking exit number {exit_number} from roundabout")

def arrival(destination: str):
    print(f"We have arrived at {destination}")




def destination():
    destination = input("Where would you like to go?")

    start_engine()
    if destination in ["library", "tech part"]:
        
        if destination == "library":
            move_forward()
            turn("left")
            print("We have arrived at the library")
        elif destination == "tech park":
            move_forward()
            turn("right")
            print(f"We have arrived at {destination}")
    elif destination in ["hospital", "mall", "airport", "uninversity", "stadium"]:
        move_forward()
        print("entering roundabout")
        if destination == "hospital":
            follow_roundabout(1)
            arrival(destination)
        elif destination == "mall":
            follow_roundabout(2)
            move_forward()
            turn("right")
            arrival(destination)
        elif destination == "unniversity" or "stadium":
            follow_roundabout(4)
            if destination == "unniversity":
                turn("left")
                arrival(destination)
            else:
                turn("right")
                arrival(destination)
    else:
        print(f"Sorry I don't know where {destination} is")

destination()

