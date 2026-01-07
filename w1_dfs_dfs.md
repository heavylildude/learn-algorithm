# 🌊 Digital Hide & Seek: DFS & BFS 🌊

Alright little groms! 🏄‍♂️  
Today we're shreddin' two legendary ways to explore a maze: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.  
Think of yourself as a tiny robot tryna find the shiny **EXIT** in a grid full of walls and open paths.

## The Maze Setup

Our maze is a simple **5×5 grid**:

- `0` = open path (soft sand, you can walk here)  
- `1` = wall (big fuck-off brick, can't go through)  
- `9` = the EXIT (treasure chest, jackpot!)

```
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
1 1 0 1 0
0 0 0 0 9
```

Start position: top-left → (0, 0)  
Goal: bottom-right → (4, 4) with the sweet 9

Allowed moves: up, down, left, right (no diagonals, keep it classic)

## Depth-First Search (DFS) – The YOLO Adventurer 🏄‍♂️💥

DFS is like ridin' one gnarly wave as deep as you can until you slam into the beach, then paddle back and try the next one.  
Chaotic energy, might find the exit fast or get cooked in a dead-end for ages.

### How DFS works (super simple breakdown)
- Uses a **stack** → like a tower of pancakes. Last pancake you add is the first you eat (LIFO = Last In First Out)  
- Keeps divin' deeper down one path before tryin' others  
- Backtracks when it hits a wall or dead end

```
def solve_dfs(start_pos):
    stack = [start_pos]               # start by putting (0,0) on the stack (our pancake tower)
    visited = set()                   # empty set to remember spots we've already checked (no duplicates)

    while stack:                      # keep going as long as there's stuff left on the stack
        x, y = stack.pop()            # pop() grabs the LAST thing you added (top of the tower)
        
        if (x, y) in visited:         # already checked this spot? skip it, don't waste time
            continue
        
        visited.add((x, y))           # mark this spot as visited (add to our sticker book)
        print(f"Checking square: ({x}, {y})")
        
        if maze[x][y] == 9:           # jackpot! we found the exit
            print("EXIT FOUND! W 🏁")
            return True
        
        # Check 4 directions: right, down, left, up
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx                   # new x coordinate
            ny = y + dy                   # new y coordinate
            # Make sure it's inside the maze and not a wall
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
                stack.append((nx, ny))    # add new spot to the TOP of the stack (dive deeper!)
    
    print("NO EXIT FOUND 😢")
    return False
```

## Breadth-First Search (BFS) – The Organized Wave 🌊📏

BFS is like droppin' a pebble in a puddle – ripples spread out evenly, checking every close spot first.  
Systematic as fuck, always finds the shortest path in this kind of maze.

### How BFS works (super simple breakdown)
- Uses a **queue** → like a line at the ice cream truck. First kid in line gets served first (FIFO = First In First Out)  
- Checks all neighbors at the current distance before moving farther out  
- Level by level, no rushin' deep into one path

```
def solve_bfs(start_pos):
    queue = [start_pos]               # start with (0,0) at the front of the line
    visited = set()

    while queue:                      # keep going as long as there's people in line
        x, y = queue.pop(0)           # pop(0) grabs the FIRST thing in line (oldest spot)
        
        if (x, y) in visited:         # already been here? skip
            continue
        
        visited.add((x, y))
        print(f"Checking square: ({x}, {y})")
        
        if maze[x][y] == 9:
            print("EXIT FOUND! W 🏁")
            return True
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
                queue.append((nx, ny))    # add to the BACK of the line (wait your turn!)
    
    print("NO EXIT FOUND 😢")
    return False
```

## The Legendary One-Line Hack 🤙

Want DFS to become BFS with almost zero effort?  
Just change how you grab the next spot:

```
# DFS (deep first):
x, y = stack.pop()          # grabs the most recent addition

# BFS (level by level):
x, y = queue.pop(0)         # grabs the oldest addition
```

Same code, different personality.  
DFS = chaotic fun, might get lucky or fucked  
BFS = safe, methodical, shortest path guaranteed

## Quick Summary – Choose Your Fighter

Feature              | DFS (YOLO)                     | BFS (Organized)                  
---------------------|--------------------------------|----------------------------------
Data Structure       | Stack (pancake tower)          | Queue (ice cream line)           
Order                | Last In, First Out             | First In, First Out              
Exploration Style    | Deep first, backtrack          | Level by level, ripples          
Shortest Path?       | Nope                           | Hell yeah (unweighted maze)      
Memory usage         | Usually lower                  | Usually higher                   
Vibe                 | "Fuck it, let's go this way"   | "Let's check everything nearby"  

Keep shreddin' those mazes, little grom!  
