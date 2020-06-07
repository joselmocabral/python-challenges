def walker(maze, i, j):
    if(i >= len(maze) or i < 0 or j >= len(maze) or j < 0):
        return False
    elif(maze[i][j] == 'W'):
        return False
    elif(i == (len(maze) - 1) and j == (len(maze) - 1)):
        return True
    else:
        maze[i][j] = 'W'
        return walker(maze, i-1, j) or walker(maze, i+1, j) or walker(maze, i, j+1) or walker(maze, i, j-1)
    

def path_finder(maze):
    maze = maze.split("\n")
    for i in range(0, len(maze)):
        maze[i] = [point for point in maze[i]]
    return walker(maze, 0, 0)