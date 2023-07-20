


from random import seed, randint
from graphics import *
from math import floor



MINE_IMAGE =  'images/mine.gif'
Tile = 'images/tile.gif'

#point=(100,200)
#y=Image(Point(100,200),MINE_IMAGE)
#y.draw(window)


LEFT_OFFSET = 100
RIGHT_OFFSET = 104
TOP_OFFSET = 120
BOTTOM_OFFSET = LEFT_OFFSET // 2
X_OFFSET = LEFT_OFFSET
Y_OFFSET = TOP_OFFSET
h_gap = 30
v_gap = 30



def create_2d_matrix(rows, columns):
    two_d = []  # create an empty list
    for i in range(rows):
        two_d.append([])  # append an empty list to two_d
        for j in range(columns):
            two_d[i].append(None)  # two_d[i] is the empty list that we just created.
            # here, we are adding elements to it.
    return two_d

def print_game_board(game_board_marker):
    for i in range(len(game_board_marker)):
        for j in range(len(game_board_marker[i])):
            matrix = str(game_board_marker[i][j]).rjust(5)
            print(matrix, end='')

        print()
def populate_with_mines(game_board_markers, number_of_mines):
    mine_board_game = []

    random_row= randint(0,len(game_board_markers)-1)
    random_colume = randint(0,len(game_board_markers[0])-1)
    for columm in range(number_of_mines):
        game_board_markers[random_row][random_colume] = 13

        random_row = randint(0, len(game_board_markers) - 1)
        random_colume=randint(0, len(game_board_markers[0]) - 1)#look back here why it was messedup
    mine_board_game.append(game_board_markers)
    return game_board_markers

def update_neighbor_count(row, column,grid):
    count = 0


    if row != 0 and column != 0:
        if grid[row - 1][column - 1] == 13 :
            count += 1
    if column != 0:
        if grid[row][column - 1] == 13:
            count += 1
    if row < len(grid) - 1 and column != 0:
        if grid[row + 1][column - 1] == 13:
            count += 1
    if row != 0:
        if grid[row - 1][column] == 13:
            count += 1
    if row < len(grid) - 1:
        if grid[row + 1][column] == 13:
            count += 1
    if row != 0 and column < len(grid[0]) - 1:
        if grid[row - 1][column + 1] == 13:
            count += 1
    if column < len(grid[0]) - 1:
        if grid[row][column + 1] == 13:
            count += 1
    if row < len(grid) - 1 and column < len(grid[0]) - 1:
        if grid[row + 1][column + 1] == 13:
            count += 1
    if grid[row][column] == 13:
        count = 13

    return count

def add_mine_counts(game_board_markers):
    new_matrix = create_2d_matrix(len(game_board_markers),len(game_board_markers[0]))

    for i in range(len(game_board_markers)):
        for j in range(len(game_board_markers[0])):
            new_matrix[i][j] = update_neighbor_count(i,j,game_board_markers)
    return new_matrix
#Draws the lines that are shown in Figure 1.
def draw_the_grid(rows,colloms,win):
    left_x = X_OFFSET
    left_y = Y_OFFSET
    right_x = left_x + colloms * h_gap
    right_y = left_y + rows * v_gap
    y = Y_OFFSET
    x = X_OFFSET

    for row_idx in range(rows + 1):
        left_end_point = Point(left_x,y)
        right_end_point = Point(right_x,y)
        line = Line(left_end_point, right_end_point)
        line.setFill('black')
        line.setWidth(1)
        line.draw(win)
        y += v_gap

    for collom_idx in range(colloms+1):
        left_end_point = Point(x, left_y)
        right_end_point = Point(x, right_y)
        line = Line(left_end_point, right_end_point)
        line.setFill('black')
        line.setWidth(1)
        line.draw(win)
        x += h_gap

def draw_board_numbers(game_board_markers, game_board_images, win):

    y = RIGHT_OFFSET+h_gap

    for row in range(len(game_board_markers)):
        x = LEFT_OFFSET+v_gap//2
        for collom in range(len(game_board_markers[row])):

            if int(game_board_markers[row][collom]) > -1:
                text = Text(Point(x, y), str(game_board_markers[row][collom]))
                text.draw(win)
                if (game_board_markers[row][collom]) == 13:
                    Mind_image = Image(Point(x,y),MINE_IMAGE)
                    Mind_image.draw(win)
                if (game_board_markers[row][collom]) == 0:
                    text.undraw()
            Tile_image = Image(Point(x, y), Tile)
            Tile_image.draw(win)
            game_board_images[row][collom] = Tile_image

            x +=h_gap
        y += v_gap
def is_click_point_in_grid(click_point, num_rows,num_columns):
    return not (click_point.getX()<X_OFFSET or
    click_point.getX()>X_OFFSET + num_columns * h_gap or
    click_point.getY()<Y_OFFSET or
    click_point.getY()> Y_OFFSET + num_rows*v_gap)

def undraw_at_click(row,collom ,image_grid):
    if image_grid[row][collom] is not None:
        image_grid[row][collom].undraw()
        #image_grid[row][collom]=None






def main():

    print('Beginner')
    print()
    print('Intermediate')
    print()
    print('Expert')
    print()
    Level = str(input('Choose a Level'))

    if Level == 'Beginner':
        window = GraphWin('Mindsweeper', 600, 600, autoflush=False)

        row = 9
        collom = 9
        num_mines = 10
        matrix = create_2d_matrix(row, collom)
        inside_matrix = create_2d_matrix(row,collom)
        mind_game_board = populate_with_mines(matrix, num_mines)
        count_matrix = add_mine_counts(mind_game_board)
        print_game_board(inside_matrix)
        print_game_board(count_matrix)



        draw_the_grid(row, collom, window)
        draw_board_numbers(count_matrix, inside_matrix, window)

        for i in range(10):
            click = window.getMouse()
            x_c_point = click.getX()
            y_c_point = click.getY()
            rows = floor(y_c_point - Y_OFFSET) // h_gap

            column = floor(x_c_point - X_OFFSET) // v_gap

            if not is_click_point_in_grid(click,row,collom):
                continue
            else:
                undraw_at_click(rows,column,inside_matrix)

        print(inside_matrix)
    if Level == 'Intermediate':
        window = GraphWin('Mindsweeper', 700, 700, autoflush=False)
        row = 16
        collom = row
        num_mines = 40
        matrix = create_2d_matrix(row, collom)
        inside_matrix = create_2d_matrix(row, collom)
        mind_game_board = populate_with_mines(matrix, num_mines)
        count_matrix = add_mine_counts(mind_game_board)
        print_game_board(inside_matrix)
        print_game_board(count_matrix)

        draw_the_grid(row, collom, window)
        draw_board_numbers(count_matrix, inside_matrix, window)

        for i in range(10):
            click = window.getMouse()
            x_c_point = click.getX()
            y_c_point = click.getY()
            rows = floor(y_c_point - Y_OFFSET) // h_gap

            column = floor(x_c_point - X_OFFSET) // v_gap

            if not is_click_point_in_grid(click, row, collom):
                continue
            else:
                undraw_at_click(rows, column, inside_matrix)
        print(inside_matrix)
    if Level =="Expert":
        window = GraphWin('Mindsweeper', 1100, 700, autoflush=False)
        row = 16
        collom = 30
        num_mines = 99
        matrix = create_2d_matrix(row, collom)
        inside_matrix = create_2d_matrix(row, collom)
        mind_game_board = populate_with_mines(matrix, num_mines)
        count_matrix = add_mine_counts(mind_game_board)
        print_game_board(inside_matrix)
        print_game_board(count_matrix)

        draw_the_grid(row, collom, window)
        draw_board_numbers(count_matrix, inside_matrix, window)

        for i in range(10):
            click = window.getMouse()
            x_c_point = click.getX()
            y_c_point = click.getY()
            rows = floor(y_c_point - Y_OFFSET) // h_gap

            column = floor(x_c_point - X_OFFSET) // v_gap

            if not is_click_point_in_grid(click, row, collom):
                continue
            else:
                undraw_at_click(rows, column, inside_matrix)
        print(inside_matrix)

    #window.getMouse()
    window.close()



main()