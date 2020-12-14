maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x, y-1)
]


# 起点(x1, y1), 终点(x2, y2)
def maze_path(x1, y1, x2, y2):
    stack = [(x1, y1)]
    while len(stack) > 0:
        curnode = stack[-1]         # 当前节点
        if curnode[0] == x2 and curnode[1] == y2:
            for p in stack:
                print(p)
            return True

        # 四个方向，上(x-1,y), (x+1,y), (x,y+1), (x,y-1)
        for direction in dirs:
            nextnode = direction(curnode[0], curnode[1])
            if maze[nextnode[0]][nextnode[1]] == 0:
                stack.append(nextnode)
                maze[nextnode[0]][nextnode[1]] = 2          # 标记2为已经走过
                break
        else:
            maze[nextnode[0]][nextnode[1]] = 2
            stack.pop()
    else:
        print("No path")
        return False


# test
maze_path(1, 1, 8, 8)
