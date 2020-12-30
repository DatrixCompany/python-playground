import time
import math
# from objects import main


def play_1(game):
    # time.sleep(0.03)
    snake = game.snake

    head = snake.head
    tail = snake.tail
    direction = snake.direction

    grid = game.grid
    xAxis = grid.xAxis
    yAxis = grid.yAxis

    food = game.food

    top_dis = int(yAxis.stop - 1 - head.cor[1])
    bot_dis = int(head.cor[1] - yAxis.start)

    right_dis = int(xAxis.stop - 1 - head.cor[0])
    left_dis = int(head.cor[0] - xAxis.start)

    food_dest = get_destination(head.cor, food)
    # print(food_dest)

    dis = {"top": top_dis, "bot": bot_dis,
           "right": right_dis, "left": left_dis}

    # new_dir = get_food_shortest(food_dest, direction)
    # new_dir = change_direction_on_grid_limit(dis, direction)
    new_dir = fill_box_move(dis, direction)

    game.turn(new_dir)
    return game


def pick_direction_on_axis_limit(limit_axis, dis):
    return ('up' if dis["top"] > dis["bot"] else 'down') if limit_axis == 'y' else ('right' if dis["right"] > dis["left"] else 'left')


def change_direction_on_grid_limit(dis, direction):
    if ((dis["right"] == 0 or dis["left"] == 0) and (direction == 'right' or direction == 'left')):
        return pick_direction_on_axis_limit('y', dis)
    elif ((dis["top"] == 0 or dis["bot"] == 0) and (direction == 'up' or direction == 'down')):
        return pick_direction_on_axis_limit('x', dis)
    else:
        return direction


def get_food_shortest(food_dest, direction): return move_closer_to_dest(
    food_dest, direction)


def move_closer_to_dest(dest, direction):
    cur_dir_type = 'vertical' if direction == 'up' or direction == 'down' else 'horizontal'
    ops_dir_type = oposite_dir_type(cur_dir_type)
    if (dest[cur_dir_type] > 0):
        wanted_dir = get_dir_by_dest_and_dir_type(dest, cur_dir_type)
        return wanted_dir if wanted_dir == direction else get_dir_by_dest_and_dir_type(dest, ops_dir_type)
    else:
        wanted_dir = get_dir_by_dest_and_dir_type(dest, ops_dir_type)
        return wanted_dir if wanted_dir == direction else get_dir_by_dest_and_dir_type(dest, ops_dir_type)


def get_destination(cor1, cor2):
    vertical = int(cor2[1] - cor1[1])
    horizontal = int(cor2[0] - cor1[0])
    shortest = math.sqrt(vertical ** 2 + horizontal ** 2)
    min_steps = abs(vertical) + abs(horizontal)
    return {
        "vertical": vertical, "horizontal": horizontal, "shortest": shortest, "min_steps": min_steps}


def oposite_dir_type(
    dir_type): return 'vertical' if dir_type == 'horizontal' else 'horizontal'


def get_dir_by_dest_and_dir_type(dest, dir_type):
    if dir_type == "vertical" and dest[dir_type] > 0:
        return 'up'
    elif (dir_type == "vertical" and dest[dir_type] < 0):
        return 'down'
    elif (dir_type == "horizontal" and dest[dir_type] > 0):
        return 'right'
    elif (dir_type == "horizontal" and dest[dir_type] < 0):
        return 'left'

# if __name__ == '__main__':
#     main()


def fill_box_move2(dis, direction):
    # move horizontaly, 1 block margin on the right
    cur_dir_type = 'vertical' if direction == 'up' or direction == 'down' else 'horizontal'
    # ops_dir_type = oposite_dir_type(cur_dir_type)
    if ((dis["right"] == 1 or dis["left"] == 0) and (cur_dir_type == 'horizontal')):
        return "up" if dis["top"] != 0 else 'down'
    elif ((dis["top"] == 0 or dis["bot"] == 0) and (cur_dir_type == 'vertical')):
        return "right" if dis["right"] != 1 else 'left'
    else:
        return "up" if dis["top"] != 0 else 'down'
        # return "right" if dis["right"] != 1 else 'left'


def fill_box_move(dis, direction):
    # move horizontally, 1 block margin on the right
    cur_dir_type = 'vertical' if direction == 'up' or direction == 'down' else 'horizontal'
    # ops_dir_type = oposite_dir_type(cur_dir_type)
    if ((dis["right"] == 0)):
        return "down" if dis["bot"] != 0 else 'left'
    if ((dis["right"] == 1) and (cur_dir_type == 'horizontal')) and (dis["bot"] == 0):
        return "left"
    if ((dis["right"] == 1) and (cur_dir_type == 'horizontal')):
        return "up" if dis["top"] != 0 else 'right'
    elif ((dis["left"] == 0) and (cur_dir_type == 'horizontal')):
        return "up" if dis["top"] != 0 else 'right'
    elif ((dis["left"] == 0) and (cur_dir_type == 'vertical')):
        return "right" if dis["right"] != 0 else 'left'
    elif (dis["right"] == 1) and (cur_dir_type == 'vertical'):
        return "left" if dis["left"] != 0 else 'right'
    else:
        return direction
        # return "right" if dis["right"] != 1 else 'left'
