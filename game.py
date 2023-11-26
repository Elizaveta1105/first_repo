from random import randint

SIZE_X = randint(5, 10)
SIZE_Y = randint(5, 10)

x_coordinate = randint(0, SIZE_X - 1)
y_coordinate = randint(0, SIZE_Y - 1)
player_sign = "X|"

exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)
exit_sign = "O|"


def generate_map(x, y, x_exit, y_exit, x_side=SIZE_X, y_side=SIZE_Y, play_sign=player_sign, sign_exit=exit_sign):

    map_w = ""

    for i in range(y_side):
        ro = " |"
        for j in range(x_side):
            if i == y and j == x:
                ro += play_sign
            elif i == y_exit and j == x_exit:
                ro += sign_exit
            else:
                ro += " |"
        map_w += f"{ro}\n"

    return map_w


def move(act, x, y, x_side=SIZE_X, y_side=SIZE_Y):

    if act == "u" and y > 0:
        y -= 1
    elif act == "d" and y < y_side - 1:
        y += 1
    elif act == "l" and x > 0:
        x -= 1
    elif act == "r" and x < x_side - 1:
        x += 1

    return x, y


def go_to_next_level(x_side, y_side, x, y):
    x_side += 3
    y_side += 3
    x = x_side - 2
    y = y_side - 2

    return x_side, y_side, x, y


while True:

    world_map = generate_map(x_coordinate, y_coordinate, exit_x, exit_y, SIZE_X, SIZE_Y)
    print(world_map)

    if y_coordinate == exit_y and x_coordinate == exit_x:
        print("You won.")
        is_next_level = input("Input Y to move to the next level: ")
        if is_next_level == "Y":
            SIZE_X, SIZE_Y, x_coordinate, y_coordinate = go_to_next_level(SIZE_X, SIZE_Y, x_coordinate, y_coordinate)
        else:
            break
        continue

    action = input("Enter the action u / d / l / r: ")

    x_coordinate, y_coordinate = move(action, x_coordinate, y_coordinate, SIZE_X, SIZE_Y)
