

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    if shape == 'pyramid' or shape == 'square' or shape == 'triangle' or shape == 'diamond':
        return shape
    else:
        return get_shape()
    
# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = input("Height?: ")
    try:
        if int(height) <= 80:
            return int (height)
    except ValueError: 
        return get_height() 

# TODO: Step 2
def draw_pyramid(height, outline):
    if outline == True:
        x = 1
        y = height - 1
        while y >= 0:
            if y == height -1:
                print(" " * y + "*" * x)
                y -= 1
            elif y == 0:
                print(" " * y + "*" * (x +2))
                y -= 1
            else:
                print(" " * y + "*" + " " * x + "*")
                x += 2
                y -= 1
    elif outline == False:
        x = 1
        y = height -1
        while y >= 0:
            print(" " * y + "*" * x)
            x += 2
            y -= 1
        
# TODO: Step 3
def draw_square(height, outline):
    if outline == True:
        x = 1
        while x <= height:
            y = 1
            while y <= height:
                if x == 1 or x == height:
                    print('*' * height)
                    x += 1
                    y += 1
                else:
                    print('*' + ' '* (height -2) + '*')
                    y += 1
                    x += 1

    else:
        x = 1
        while x <= height:
            y = 1
            while y <= height:
                print('*'* height)
                y += 1
                x += 1

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == True:
        for x in range(height):
            for y in range(height):
                if y==0 or x==(height-1) or x==y:
                    print("*", end="")
                else:
                    print(end=" ")
            print()

    elif outline == False:
        i = 1 
        j = height - 1
        while j >= 0:
            print("*" * i)
            i += 1
            j -= 1

# TODO: Step 5
def draw_diamond(height, outline):
    if outline == True:
        for x in range(height):
            for y in range(height):
                if x+y == 2 or x-y==2 or y-x==2 or x+y==6:
                    print("*", end="")
                else:
                    print(end=" ")
            print()

    else:
        x = 1
        y = height -1
        while y > 0:
            print(" " * y + "*" * (x-4))
            x += 2
            y -= 1
        while  y <=height:
            print(" "* y + "*"* (x-4))
            x -=2
            y +=1
        


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    if shape == 'triangle':
        draw_triangle(height, outline)
    if shape == 'square':
        draw_square(height, outline)
    if shape == 'diamond':
        draw_diamond(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    user_outline = input("Outline only? (y/N):")
    if user_outline == 'y' or user_outline == 'Y':
        return True

    return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

