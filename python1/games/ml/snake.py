import numpy as np
import time
from game_logic import play_1


def check_if_same_cor(cor_X1Y1, cor_X2Y2):
    return cor_X1Y1[0] == cor_X2Y2[0] and cor_X1Y1[1] == cor_X2Y2[1]


class Grid:
    def __init__(self, width, height):
        self.width = int(width/2)*2
        self.height = int(height/2)*2
        self.x_axis = range(self.width)
        self.y_axis = range(self.height)
        self.space = np.zeros((self.height, self.width))

    def is_free_space(self, checked_cor, used_space):
        inside_grid_space = checked_cor[0] >= self.x_axis.start and checked_cor[
            0] < self.x_axis.stop and self.y_axis.start <= checked_cor[1] < self.y_axis.stop
        if (inside_grid_space):
            for cor in used_space:
                if check_if_same_cor(cor, checked_cor):
                    return False
            return True
        else:
            return False


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
        self.head = head_cor or np.array([0, 0])
        self.tail = SnakeTail(C) if C is not None else SnakeTail(np.array([]))
        self.direction = 'up'

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
            return self.head + [0, 1]
        elif direction == 'down':
            return self.head - [0, 1]
        elif direction == 'right':
            return self.head + [1, 0]
        elif direction == 'left':
            return self.head - [1, 0]

    def on_valid_move(self, new_head_cor, is_valid_eat):
        if (len(self.tail.parts) or is_valid_eat):
            self.tail.on_head_move(old_head_cor=self.head,
                                   is_valid_eat=is_valid_eat)
        self.head = new_head_cor


class Game:
    def __init__(self, grid_kwargs, snake_kwargs=None):
        self.grid = Grid(**grid_kwargs)
        self.snake = Snake(
            **snake_kwargs) if snake_kwargs is not None else Snake()
        self.apple = self.gen_apple()
        self.moves = 0
        self.level = 0
        self.level_steps = 0
        self.is_valid_eat = False
        self.status = 'PLAYING'

    @property
    def used_space(self):
        if (len(self.snake.tail.parts)):
            return np.array(
                [self.snake.head, *self.snake.tail.parts])
        else:
            return np.array(
                [self.snake.head])

    @property
    def space(self):
        space = self.grid.space.copy()
        for x, y in self.used_space:
            space[y, x] = 1
        x, y = self.apple
        space[y, x] = -1
        return space

    def __gen_apple_cor(self):
        x_axis = self.grid.x_axis
        y_axis = self.grid.y_axis
        return np.array([np.random.randint(low=x_axis.start, high=x_axis.stop), np.random.randint(low=y_axis.start, high=y_axis.stop)])

    def gen_apple(self):
        apple = self.__gen_apple_cor()
        while (not self.grid.is_free_space(apple, used_space=self.used_space)):
            apple = self.__gen_apple_cor()
        self.apple = apple
        return self.apple

    def check_valid_eat(self, new_head_cor):
        self.is_valid_eat = check_if_same_cor(self.apple, new_head_cor)
        return self.is_valid_eat

    def check_valid_move(self, direction):
        snake = self.snake
        grid = self.grid
        new_head_cor = snake.attempt_move(direction)
        # move to free space or end of tail
        end_of_tail_space = snake.tail.parts[-1] if snake.tail.parts.size > 0 else np.array([
        ])
        is_end_of_tail = end_of_tail_space.size > 0 and check_if_same_cor(
            new_head_cor, end_of_tail_space)
        if (grid.is_free_space(new_head_cor, self.used_space) or is_end_of_tail):
            return True, new_head_cor
        else:
            return False, None

    def snake_move(self, direction):
        # reset what is needed
        if (self.is_valid_eat):
            self.level_steps = 0
        is_valid, new_head_cor = self.check_valid_move(direction)
        if (is_valid):
            self.moves += 1
            self.level_steps += 1
            is_valid_eat = self.check_valid_eat(new_head_cor)
            self.snake.on_valid_move(
                new_head_cor, is_valid_eat)
            if (is_valid_eat):
                self.level += 1
                if(not self.check_if_won()):
                    self.gen_apple()
        else:
            self.status = 'LOST'

    def turn(self, direction):
        self.snake_move(self.snake.valid_direction(direction))

    def check_if_won(self):
        if self.level == (self.grid.width * self.grid.height) - 1:
            self.status = 'WON'
            return True
        return False


def render_game(game):
    head = game.snake.head
    apple = game.apple
    empty_rows = [' ' for x in game.grid.x_axis]
    empty_grid = [empty_rows.copy() for y in game.grid.y_axis]
    display = empty_grid
    # lines number (first) == y range

    # mark objects
    display[apple[1]][apple[0]] = 'O'
    display[head[1]][head[0]] = '@'
    for cor in game.snake.tail.parts:
        display[cor[1]][cor[0]] = '#'

    # paint screen
    print("*", *['-' for y in game.grid.x_axis], "*")
    for row in (display):
        print("|", *row, "|")
    print("*", *['-' for y in game.grid.x_axis], "*")


def new_game():
    game = Game(grid_kwargs={"width": 6, "height": 10})
    render_game(game)
    while (game.status == 'PLAYING' and game.moves < 100000):
        game = play_1(game)
        if (game.status != 'LOST'):
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
        if (game.status != 'LOST'):
            wins += 1
            print('WON', game.level, game.moves)
            time.sleep(15)


if __name__ == '__main__':
    main()
