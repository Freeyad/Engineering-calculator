def calculate_reactions(Load, load_location, Beam_length):
    reactionA = Load * load_location / Beam_length
    reactionB = Load - reactionA
    return reactionA, reactionB
def engineering_calculator():
    try:
        print("Engineering Calculator")
        print("1. Calculate beam analysis")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1" :
            Beam_length = float(input("What is the beam length in metres? "))
            Load = float(input("What is the load in newtons? "))
            load_location = float(input("What is the distance of load from left support in metres? "))

            if Beam_length <= 0 or Load <= 0:
                print("Invalid, measurements must be larger than 0")
            elif load_location > Beam_length:
                print("Invalid load position")
            elif load_location < 0:
                print("Invalid, load position must be positive")
            else:
                reactionA, reactionB = calculate_reactions(Load, load_location, Beam_length)

                print("Reaction at A is: ", reactionA)
                print("Reaction at B is: ", reactionB)
                shear_force_before_load = reactionA
                print("Shear force before load:", shear_force_before_load)
                maximum_bending_moment = reactionA * load_location
                print("Maximum bending moment: ", maximum_bending_moment)
        elif choice == "2" :
                print("Goodbye")
        else:
            print("Invalid choice")
    except ValueError:
        print("Please type numbers only")
engineering_calculator()




