from life import LifeGrid

INIT_CONFIG=[(1,2),(2,1),(2,2),(2,3)]

GRID_WIDTH= 5
GRID_HEIGHT= 5

NUM_GENS=8

def main():
    grid = LifeGrid(GRID_WIDTH,GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

#Generates the next generation of organism
def evolve(grid):
    #list for storing the live cells of the next generation
    liveCells = list()

    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            #Determine the number of live neighbors for this cells
            neighbors = grid.numLiveNeighbors(i,j)
            #Add the (i,j) tuple to liveCells if this cell contians a
            #live organism for the next generation
            print("neighbors : {}".format(neighbors))
            if (neighbors == 2 and grid.isLiveCell(i,j)) or (neighbors ==3):
                liveCells.append((i,j))
    #Reconfigure the grid using the liveCells coord list

    grid.configure(liveCells)

def draw(grid):
    textBasedGrid=""
    for i in range(0,grid.numRows()):
        for j in range(0, grid.numCols()):
            if grid.isLiveCell(i,j):
                textBasedGrid+="1"
            else:
                textBasedGrid+="0"
        textBasedGrid+="\n"
    print (textBasedGrid)
main()
