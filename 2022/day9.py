from sys import argv

with open(argv[1]) as f:
    instructions = [line.split(" ") for line in f.read().splitlines()]
  
def touch(node1, node2):
    if node1[0] == node2[0] and (node1[1]+1 == node2[1] or node1[1]-1 == node2[1]):
        return True
    elif node1[1] == node2[1] and (node1[0]+1 == node2[0] or node1[0]-1 == node2[0]):
        return True
    elif node1[0]+1 == node2[0] and node1[1]+1 == node2[1]:
        return True
    elif node1[0]-1 == node2[0] and node1[1]-1 == node2[1]:
        return True
    elif node1[0]-1 == node2[0] and node1[1]+1 == node2[1]:
        return True
    elif node1[0]+1 == node2[0] and node1[1]-1 == node2[1]:
        return True
    return False

def calc_distance(anz):
    anz += 1
    line = [[0,0] for _ in range(anz)]
    grid = [[['#']]]
    for instruction in instructions:
        match instruction[0]:
            case 'R':
                # Go right
                directionN = [0, 1]
            case 'L':
                # go left
                directionN = [0, -1]
            case 'U':
                # go up
                directionN = [-1, 0]
            case 'D':
                # go down
                directionN = [1, 0]
            case _:
                print("Invalid instruction")
                exit(1)
                
        for _ in range(int(instruction[1])):
            line[0][0] += directionN[0]
            line[0][1] += directionN[1]
            for j in range(1, anz):
                head = [line[j-1][0], line[j-1][1]]
                tail = [line[j][0], line[j][1]]
                if (head[0] == tail[0] and head[1] == tail[1]) or touch(head, tail):
                    break
                elif head[0] == tail[0]:
                    # Go horizontal
                    if touch(head, [tail[0], tail[1]+1]):
                        line[j][1] += 1
                    elif touch(head, [tail[0], tail[1]-1]):
                        line[j][1] -= 1
                elif head[1] == tail[1]:
                    # Go vertical
                    if touch(head, [tail[0]+1, tail[1]]):
                        line[j][0] += 1
                    elif touch(head, [tail[0]-1, tail[1]]):
                        line[j][0] -= 1
                elif not touch(head, tail):
                    # Go diagonal
                    if touch(head, [tail[0]+1, tail[1]+1]):
                        line[j][0] += 1
                        line[j][1] += 1
                    elif touch(head, [tail[0]-1, tail[1]-1]):
                        line[j][0] -= 1
                        line[j][1] -= 1
                    elif touch(head, [tail[0]-1, tail[1]+1]):
                        line[j][0] -= 1
                        line[j][1] += 1
                    elif touch(head, [tail[0]+1, tail[1]-1]):
                        line[j][0] += 1
                        line[j][1] -= 1
                
            # Grow the grid
            if line[-1][0] > len(grid)-1:
                grid.append([['.'] for _ in range(len(grid[0]))])
            if line[-1][1] > len(grid[0])-1:
                for row in grid:
                    row.append(['.'])
            if line[-1][0] < 0:
                grid.insert(0, [['.'] for _ in range(len(grid[0]))])
                for l in range(len(line)):
                    line[l][0] += 1 
            if line[-1][1] < 0:
                for row in grid:
                    row.insert(0, ['.'])
                for l in range(len(line)):
                    line[l][1] += 1
                    
            # Add the path to the grid
            grid[line[-1][0]][line[-1][1]] = ['#']
        
    # Count the number of intersections    
    count = 0
    for row in grid:
        count += row.count(['#'])
    return count

print(f"Part 1: {calc_distance(1)}")
print(f"Part 2: {calc_distance(9)}")