lst_command = ['left', 'right', 'forward', 'back','off', 'help', 'sprint']
direction = 1
x = 0
y = 0

def name_robot():
    """naming of the robot"""
    Name = input("What do you want to name your robot? ").upper()
    print(Name + ": Hello kiddo!")
    return Name

def get_command_input(name_robot):
    """prompts user"""
    prev_output = input(f"{name_robot}: What must I do next? ")
    output = prev_output.lower()
    cmd = output.split(' ')
    if cmd[0] not in lst_command:
        print(f"{name_robot}: Sorry, I did not understand '{prev_output}'.")
    return cmd

def handle_command(Name):
    global x,y
    global direction

    while True:
        output = get_command_input(Name)
        if len(output) == 2:
            steps = output[1]
        if output[0] == 'off':
            direction = 1
            x = 0
            y = 0
            print (f"{Name}: Shutting down..")
            return False
        elif output[0] == 'help':
            help_command()
        elif output[0] == 'left' or output[0] == 'right':
            set_direction(output, Name)
        elif output[0] == 'forward':
            forward_command(Name, output)
        elif output[0] == 'back':
            back_command(Name, output)
        elif output[0] == 'sprint':
            #steps = output[0]
            i = 0
            i = sprint_command(Name, steps, i)
            sprint(Name,i)
            
            #sprint_command(Name, output[1])
        

def help_command():
    print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands?\n""")
    
     
def forward_command(Name, output):
    global direction
    global x,y
    #temp = y
    steps = output[1]
    if (y + int(output[1]) >= -200 and y + int(output[1]) <= 200  and direction == 1):
        y += int(steps)
        print(f" > {Name} moved forward by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        #print('this ran', direction, 'for y')
    elif (x + int(output[1]) >= -100 and x + int(output[1]) <= 100  and direction == 2):
        x -= int(steps)
        print(f" > {Name} moved forward by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        #print('this ran', direction)
    elif (y + int(output[1]) >= -200 and y + int(output[1]) <= 200  and direction == 3):
        y -= int(steps)
        print(f" > {Name} moved forward by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        #print('this ran', direction, '3rd if')
    elif (x + int(output[1]) >= -100 and x + int(output[1]) <= 100  and direction == 4):
        x += int(steps)
        print(f" > {Name} moved forward by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        #print('this ran', direction, '4th')
    else:
        print(f"{Name}: Sorry, I cannot go outside my safe zone.")
        print(f" > {Name} now at position ({x},{y}).") 
        #print('this ran', direction, 'else')  


def back_command(Name, output):
    global direction
    global x,y
    steps = output[1]
    if (y + int(output[1]) >= -200 and y + int(output[1]) <= 200  and direction == 1):
        y -= int(steps)
        print(f" > {Name} moved back by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")   
    elif (x + int(output[1]) >= -100 and x + int(output[1]) <= 100  and direction == 2):
        x += int(steps)
        print(f" > {Name} moved back by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        # print('this ran', direction)
    elif (y + int(output[1]) >= -200 and y + int(output[1]) <= 200  and direction == 3):
        y += int(steps)
        print(f" > {Name} moved back by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        
    elif (x + int(output[1]) >= -100 and x + int(output[1]) <= 100  and direction == 4):
        x -= int(steps)
        print(f" > {Name} moved back by {output[1]} steps.")
        print(f" > {Name} now at position ({x},{y}).")
        
    else:
        print(f"{Name}: Sorry, I cannot go outside my safe zone.")
        print(f" > {Name} now at position ({x},{y}).")
        


def set_direction(command, Name):
    global direction
    #print(command[0], direction)
    if command[0] == 'left' and direction == 1:
         direction = 2
    elif command[0] == 'left' and direction == 2:
         direction = 3
    elif command[0] == 'left' and direction == 3:
         direction = 4
    elif command[0] == 'left' and direction == 4:
        direction = 1
    
    elif command[0] == 'right' and direction == 1:
        direction = 4
    elif command[0] == 'right' and direction == 2:
        direction = 1
    elif command[0] == 'right' and direction == 3:
        direction = 2
    elif command[0] == 'right' and direction == 4:
        direction = 3

    print(f" > {Name} turned {command[0]}.")
    print(f" > {Name} now at position ({x},{y}).")


def sprint_command(Name, steps, i):
    if steps == 0:
        return i
    else:
        i += int(steps)
        print(f" > {Name} moved forward by {steps} steps.")
        #print(f" > {Name} now at position ({x},{y}).")
    return sprint_command(Name, int(steps)- 1, i)


def sprint(Name, i):
    global x,y
    
    if (y + i >= -200 and y + i <= 200  and direction == 1):
        y += int(i)   
    elif (x + i >= -100 and x + i <= 100  and direction == 2):
        x += int(i)
    elif (y + i >= -200 and y + i <= 200  and direction == 3):
        y -= int(i)     
    elif (x + i >= -100 and x + i <= 100  and direction == 4):
        x -= int(i)
    print(f" > {Name} now at position ({x},{y}).")
        

def robot_start():
    Name = name_robot()
    handle_command(Name)
    

if __name__ == "__main__":
    robot_start()
