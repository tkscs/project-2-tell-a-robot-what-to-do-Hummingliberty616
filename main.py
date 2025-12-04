from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
current_state = "idle" 

while True: 
    if current_state == "idle":
        current_input = input("What do you want to do?")

    if current_state == "idle":
        if current_input == "spin clockwise please":
            while True:
                robot.right(90)
                stop = input("Stop?")
                if stop == "Yes":
                    break
        if current_input == "spin clockwise":
            print("AH AH AH! YOU DIDN'T SAY THE MAGIC WORD!")
        if current_input == "spin counterclockwise":
            while True:
                #Do 
    
        if current_input == "Make animal sounds":
            animal = input("Which animal?")
            if animal == "dog":
                #Bark
            if animal == "cat":
                #meow
              

