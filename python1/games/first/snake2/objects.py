from gameLogic import play_1
import numpy as np
import time


def check_if_same_cor(cor_X1Y1, cor_X2Y2):
    return cor_X1Y1[0] == cor_X2Y2[0] and cor_X1Y1[1] == cor_X2Y2[1]


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Grid:
    def __init__(self, width, height):
        self.width = int(width/2)*2
        self.height = int(height/2)*2
        self.xAxis = range(self.width)
        self.yAxis = range(self.height)

    def is_free_space(self, checked_cor, used_space):
        inside_grid_space = checked_cor[0] >= self.xAxis.start and checked_cor[
            0] < self.xAxis.stop and self.yAxis.start <= checked_cor[1] < self.yAxis.stop
        if (inside_grid_space):
            for cor in used_space:
                if check_if_same_cor(cor, checked_cor):
                    return False
            return True
        else:
            return False


class ScreenDot:
    def __init__(self, cor):
        self.cor = cor


class SnakeHead(ScreenDot):
    def __init__(self, cor):
        super().__init__(cor)


class SnakeTail:
    def __init__(self, C):
        self.parts = C

    def on_head_move(self, old_head_cor, is_valid_eat=False):
        # 1) remove last arr / tailpart 2) add old_head_cor to first arr
        self.parts = np.insert(self.parts, 0, old_head_cor, axis=0) if len(
            self.parts) else np.array([old_head_cor])
        if len(self.parts) and not is_valid_eat:
            self.parts = np.delete(self.parts, -1,  axis=0)


class Snake:
    def __init__(self, head_cor=None, C=None):
        self.head = SnakeHead(
            head_cor) if head_cor is not None else SnakeHead(np.array([0, 0]))
        self.tail = SnakeTail(C) if C is not None else SnakeTail(np.array([]))
        self.direction = 'left'

    def valid_direction(self, wanted_direction=None):
        cur_direction = self.direction
        if ((wanted_direction == 'up' and cur_direction != 'down') or
            (wanted_direction == 'down' and cur_direction != 'up') or
            (wanted_direction == 'right' and cur_direction != 'left') or
                (wanted_direction == 'left' and cur_direction != 'right')):
            self.direction = wanted_direction
        return self.direction

    def attempt_move(self, direction):
        if direction == 'up':
            return self.head.cor + [0, 1]
        elif direction == 'down':
            return self.head.cor - [0, 1]
        elif direction == 'right':
            return self.head.cor + [1, 0]
        elif direction == 'left':
            return self.head.cor - [1, 0]

    def on_valid_move(self, new_head_cor, is_valid_eat):
        if (len(self.tail.parts) or is_valid_eat):
            self.tail.on_head_move(old_head_cor=self.head.cor,
                                   is_valid_eat=is_valid_eat)
        self.head.cor = new_head_cor


class Game:
    def __init__(self, grid_kwargs, snake_kwargs=None):
        self.grid = Grid(**grid_kwargs)
        self.snake = Snake(
            **snake_kwargs) if snake_kwargs is not None else Snake()
        self.food = self.gen_food()
        self.moves = 0
        self.score = 0
        self.state = 'PLAYING'

    @property
    def used_space(self):
        if (len(self.snake.tail.parts)):
            return np.array(
                [self.snake.head.cor, *self.snake.tail.parts])
        else:
            return np.array(
                [self.snake.head.cor])

    def __gen_food_cor(self):
        xAxis = self.grid.xAxis
        yAxis = self.grid.yAxis
        return np.array([np.random.randint(low=xAxis.start, high=xAxis.stop), np.random.randint(low=yAxis.start, high=yAxis.stop)])

    def gen_food(self):
        food = self.__gen_food_cor()
        while (not self.grid.is_free_space(food, used_space=self.used_space)):
            food = self.__gen_food_cor()
        self.food = food
        return self.food

    def check_valid_eat(self, new_head_cor):
        return check_if_same_cor(self.food, new_head_cor)

    def check_valid_move(self, direction):
        snake = self.snake
        grid = self.grid
        new_head_cor = snake.attempt_move(direction)
        # move to free space or end of tail
        if (grid.is_free_space(new_head_cor, self.used_space) or check_if_same_cor(new_head_cor, snake.tail.parts[-1])):
            return [True, new_head_cor]
        else:
            return [False, None]

    def snake_move(self, direction):
        is_valid, new_head_cor = self.check_valid_move(direction)
        if (is_valid):
            self.moves += 1
            is_valid_eat = self.check_valid_eat(new_head_cor)
            # print('Valid Eat', new_head_cor)
            self.snake.on_valid_move(
                new_head_cor, is_valid_eat)
            if (is_valid_eat):
                self.score += 1
                if(not self.check_if_won()):
                    self.gen_food()
        else:
            self.state = 'LOST'
            # print('Lose')

    def turn(self, direction):
        self.snake_move(self.snake.valid_direction(direction))

    def check_if_won(self):
        if self.score == (self.grid.width * self.grid.height) - 1:
            self.state = 'WON'
            return True
        return False


def render_game(game):
    head = game.snake.head
    food = game.food
    empty_rows = [' ' for x in game.grid.xAxis]
    empty_grid = [empty_rows.copy() for y in game.grid.yAxis]
    display = empty_grid
    # lines number (first) == y range

    # mark objects
    display[food[1]][food[0]] = 'O'
    display[head.cor[1]][head.cor[0]] = '@'
    for cor in game.snake.tail.parts:
        display[cor[1]][cor[0]] = '#'

    # paint screen
    print("*", *['-' for y in game.grid.xAxis], "*")
    for row in reversed(display):
        print("|", *row, "|")
    print("*", *['-' for y in game.grid.xAxis], "*")


def new_game():
    game = Game(grid_kwargs={"width": 12, "height": 24},
                # snake_kwargs={"C": np.array(([1, 0], [2, 0], [3, 0], [4, 0], [5, 0]))}
                )
    render_game(game)
    while (game.state == 'PLAYING' and game.moves < 100000):
        game = play_1(game)
        if (game.state != 'LOST'):
            render_game(game)
        else:
            print('LOST')
            time.sleep(2)
    return game


def main():
    games = 0
    wins = 0
    while (games < 10000 and wins < 10):
        games += 1
        game = new_game()
        if (game.state != 'LOST'):
            wins += 1
            print('WON', game.score, game.moves)
            time.sleep(15)


def main2():
    game = Game(grid_kwargs={"width": 12, "height": 24}, snake_kwargs={
        "C": np.array(([1, 0], [2, 0], [3, 0], [4, 0], [5, 0]))})
    render_game(game)


if __name__ == '__main__':
    main()
