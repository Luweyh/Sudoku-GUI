import pygame  # Using pygame module
import random


class Sudoku:
    """ Represent the Sudoku game """

    def __init__(self):
        """ Initializing the game """

        self.x = 0              # represent the x position
        self.y = 0              # represent the y position
        self.ratio = 600 / 9    # used to find the position ratio on board
        self.font1 = pygame.font.SysFont("Aerial", 45)
        self.font2 = pygame.font.SysFont("Aerial", 22)

        # default table represent the Sudoku board
        self.table = [
            [None, 9, None, 7, None, None, 8, 6, None],
            [None, 3, 1, None, None, 5, None, 2, None],
            [8, None, 6, None, None, None, None, None, None],
            [None, None, 7, None, 5, None, None, None, 6],
            [None, None, None, 3, None, 7, None, None, None],
            [5, None, None, None, 1, None, 7, None, None],
            [None, None, None, None, None, None, 1, None, 9],
            [None, 2, None, 6, None, None, 3, 5, None],
            [None, 5, 4, None, None, 8, None, 7, None]
        ]

    def get_x(self):
        """ Gets x """
        return self.x

    def get_y(self):
        """ Gets y """
        return self.y

    def move_x(self, amount):
        """ Move x position """
        self.x += amount

    def move_y(self, amount):
        """ Move y position """
        self.y += amount

    def change_table(self, x, y, val):
        """ Changes a value on the table """
        self.table[x][y] = val

    def get_table(self):
        """ Gets the table """
        return self.table

    def default_table(self):
        """ Resets the table """
        self.table = [
            [None, 9, None, 7, None, None, 8, 6, None],
            [None, 3, 1, None, None, 5, None, 2, None],
            [8, None, 6, None, None, None, None, None, None],
            [None, None, 7, None, 5, None, None, None, 6],
            [None, None, None, 3, None, 7, None, None, None],
            [5, None, None, None, 1, None, 7, None, None],
            [None, None, None, None, None, None, 1, None, 9],
            [None, 2, None, 6, None, None, 3, 5, None],
            [None, 5, 4, None, None, 8, None, 7, None]
        ]
        self.update_table()     # need to update table after resetting

    def random_table(self):
        """ Creates a random board to be solved """

        table = [[None for _ in range(9)] for _ in range(9)]    # empty board
        self.table = table      # changing current board to empty

        for _ in range(35):             # for enough random numbers
            x = random.randint(0,8)     # represent random x position on board
            y = random.randint(0,8)     # represent random y position on board
            val = random.randint(1,9)   # represent random value on board

            # if random numbers are valid on board, add it to random bboard
            if self.valid_helper(table, x,y, val):
                table[x][y] = val

        table = self.table
        self.update_table()

    def move_piece(self):
        """ Represent the selected player's moving piece surrounded by a blue box """

        for i in range(2):
            x = self.x
            y = self.y
            ratio = self.ratio

            # drawing the lines around the piece
            pygame.draw.line(screen, (0, 0, 255), (x * ratio - 3, (y + i) * ratio),(x * ratio + ratio + 3, (y + i) * ratio), 7)
            pygame.draw.line(screen, (0, 0, 255), ((x + i) * ratio, y * ratio), ((x + i) * ratio, y * ratio + ratio), 7)

    def update_table(self):
        """ Updates the game table by inputting the numbers. Also
         colors the table and finish the outline"""

        table = self.table
        font1 = self.font1
        ratio = self.ratio

        # filling out the table and inputting color
        for row in range(9):
            for col in range(9):
                if table[row][col] != 0:
                    if table[row][col] is not None:
                        # Coloring filled squares gold
                        pygame.draw.rect(screen, (212, 175, 55), (row * ratio, col * ratio, ratio + 1, ratio + 1))

                        # filling the number
                        text1 = font1.render(str(table[row][col]), 1, (0, 0, 0))
                        screen.blit(text1, (row * ratio + 24, col * ratio + 20))


        # Outlines the board with the appropriate lines. Makes thicker lines for the 3x3 squares
        for row in range(10):
            if row % 3 == 0:
                line = 7
            else:
                line = 2
            pygame.draw.line(screen, (0, 0, 0), (0, row * ratio), (600, row * ratio), line)
            pygame.draw.line(screen, (0, 0, 0), (row * ratio, 0), (row * ratio, 600), line)


    def is_valid(self, num):
        """ Check to see if the move is valid"""

        # check row and column is valid
        for i in range(9):
            if self.table[self.x][i] == num or self.table[i][self.y] == num:
                return False

        # check 3x3 square is valid
        x = self.x // 3
        y = self.y // 3
        for x_pos in range(x * 3, x * 3 + 3):
            for y_pos in range(y * 3, y * 3 + 3):
                if self.table[x_pos][y_pos] == num:
                    return False

        return True

    def instructions(self):
        """ Displays the instructions """

        instruction_1 = self.font2.render("Press R to generate a random board", 1, (0, 0, 0))
        instruction_2 = self.font2.render("Press D to reset to default board", 1, (0, 0, 0))
        instruction_3 = self.font2.render("Press S to solve the board", 1, (0, 0, 0))
        screen.blit(instruction_1, (20, 610))
        screen.blit(instruction_2, (20, 630))
        screen.blit(instruction_3, (20, 650))


    def results(self, val):
        """ Displays the results of the table """

        if val == 1:    # it is solvable
            self.is_solvable()
        elif val == 2:  # it is not solvable
            self.not_solvable()


    def is_solvable(self):
        """ Displays whether it is solvable or not """
        text = self.font2.render("FINISHED! The puzzle is solved!", 1, (0,200,0))
        screen.blit(text, (20, 670))

    def not_solvable(self):
        """ Displays if the board is solvable """
        text = self.font2.render("The current puzzle is not solvable! Reset to a different table",1, (0,0,0))
        screen.blit(text, (20, 670))

    def is_finished(self):
        """ See if the game is manually finished"""

        # iterates through whole table to see if the whole table is filled
        for elem in self.table:
            for i in elem:
                if i is None:
                    return False

        return True

    def valid_helper(self, table, x, y, val):
        """ Used to help 'solve' the puzzle. Check to see if input is valid. """

        # checking the row and columns
        for i in range(9):
            if table[x][i] == val or table[i][y] == val:
                return False

        # to help find the 3x3 square
        x_pos = x // 3
        y_pos = y // 3

        # checks the 3x3 square
        for x in range(x_pos * 3, x_pos * 3 + 3):
            for y in range(y_pos * 3, y_pos * 3 + 3):
                if table[x][y] == val:
                    return False

        return True

    def solve(self, table, row, col):
        """ Used to solve the puzzle """

        while table[row][col] is not None:
            if row < 8:
                row += 1
            elif row == 8 and col < 8:
                row = 0
                col += 1
            elif row == 8 and col == 8:
                return True

        for i in range(1, 10):
            if self.valid_helper(table, row, col, i) == True:
                table[row][col] = i
                self.x = row
                self.y = col

                screen.fill((255, 255, 255))
                self.update_table()
                self.move_piece()
                pygame.display.update()

                if self.solve(table, row, col) == 1:
                    return True
                else:
                    table[row][col] = None

                screen.fill((255, 255, 255))

                self.update_table()
                self.move_piece()
                pygame.display.update()

        return False


if __name__ == "__main__":

    pygame.font.init()

    # screen size
    screen = pygame.display.set_mode((600, 700))

    # Title
    pygame.display.set_caption("Sudoku")

    s = Sudoku()

    is_solve = 0

    running = True
    while running:

        screen.fill((250, 250, 250))  # background color

        for event in pygame.event.get():
            # Quit the game window
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # updating the moves
                if event.key == pygame.K_LEFT:      # move left
                    s.move_x(-1)
                    flag1 = 1
                elif event.key == pygame.K_RIGHT:   # move right
                    s.move_x(1)
                    flag1 = 1
                elif event.key == pygame.K_UP:      # move up
                    s.move_y(-1)
                    flag1 = 1
                elif event.key == pygame.K_DOWN:    # move down
                    s.move_y(1)
                    flag1 = 1

                s.move_piece()  # move the piece

                # updating the numbers
                num = None

                if event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9


                if num is not None:

                    # erases current square if select already filled square
                    table = s.get_table()
                    if table[s.get_x()][s.get_y()] is not None:
                        s.change_table(s.get_x(), s.get_y(), None)

                    # check to see if move is valid
                    elif s.is_valid(num):
                        s.change_table(s.get_x(), s.get_y(), num)

                    s.update_table()

                # reset to default board
                if event.key == pygame.K_d:
                    s.default_table()
                    is_solve = 0

                # reset to random board
                if event.key == pygame.K_r:
                    s.random_table()
                    is_solve = 0


                is_solve = 0

                # solve the table
                if event.key == pygame.K_s:
                    if s.solve(s.get_table(), 0, 0):
                        is_solve = 1
                    else:
                        is_solve = 2

        s.update_table()            # update table
        s.move_piece()              # update piece
        s.instructions()            # display instructions

        # check to see if it is manually finished
        if s.is_finished():
            is_solve = 1

        s.results(is_solve)         # display results

        pygame.display.update()     # display pygame updates
