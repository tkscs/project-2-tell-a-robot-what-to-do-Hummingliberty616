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
        if current_input == "Spin clockwise please":
            while True:
                robot.left_sonar
                robot.right_sonar
                if robot.left_sonar > 10:
                    if robot.right_sonar > 10:
                        robot.right(90)
                else: break
                stop = input("Stop?")
                if stop == "Yes":
                    break
        if current_input == "spin clockwise":
            pass
        
        if current_input == "Spin counterclockwise":
            while True: 
                robot.right(90)
                stop = input("Stop?")
                if stop == "Yes":
                    break

        if current_input == "spin counterclockwise":
            pass
    
        if current_input == "Make animal sounds please":
            animal = input("Which animal?")
            if animal == "dog":
                #Bark
            if animal == "cat":
                #meow
            if animal == "parrot":
                #Talk 

        if current_input == "Forward":
            robot.left_sonar
            robot.right_sonar
            if robot.left_sonar () > 50:
                if robot.right_sonar > 50:
                    robot.forward(50)
            else: 
                pass
        if current_input == "Sherbet lemon, please":
            robot.left_sonar
            robot.right_sonar
            if robot.left_sonar () > 50:
                if robot.right_sonar > 50:
                    for i in range (100):
                        robot.forward(1)
                        robot.backward(1)

        if current_input == "Sherbet lemon":
             
                    
       
            

        

        

        

        

              

