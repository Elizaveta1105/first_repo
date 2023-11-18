from random import randint

SIZE_X = 5
SIZE_Y = 5
world_map = ""
x_coordinate = 0
y_coordinate = 2
exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)

while True:
    world_map = ""
    for i in range(SIZE_Y):
        row = " |"
        for j in range(SIZE_X):
            if i == y_coordinate and j == x_coordinate:
                row += "X|"
            elif i == exit_y and j == exit_x:
                row += "O|"
            else:
                row += " |"
        world_map += f"{row}\n"
    print(world_map)

    if y_coordinate == exit_y and x_coordinate == exit_x:
        print("You won.")
        desire = input("Input Yes to move to the next level: ")
        if desire == "Yes":
            SIZE_X += 3
            SIZE_Y += 3
            world_map = ""
            x_coordinate = SIZE_X - 2
            y_coordinate = SIZE_Y - 2
            exit_x = randint(0, SIZE_X - 1)
            exit_y = randint(0, SIZE_Y - 1)
        else:
            break
        continue

    action = input("Enter the action up, down, left, right: ")

    if action == "up" and y_coordinate > 0:
        y_coordinate -= 1
    elif action == "down" and y_coordinate < SIZE_Y:
        y_coordinate += 1
    elif action == "left" and x_coordinate > 0:
        x_coordinate -= 1
    elif action == "right" and x_coordinate < SIZE_X:
        x_coordinate += 1
    else:
        action = input("Enter the action up, down, left, right: ")
