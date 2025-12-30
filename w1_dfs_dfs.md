# 🌊 **W1: Digital Hide & Seek: DFS & BFS** 🌊

Alright, little groms! 🏄‍♂️ Today we're gonna learn about **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**—two super cool methods for finding stuff in a maze! Imagine you're a little robot trying to find the "Exit" in a simple grid. Let's dive in!

## **The Maze**

First, let's look at our maze. It's a simple grid where:

- `0` means you can walk on it.
- `1` means there's a wall, and you can't walk through it.
- `9` is the exit you're trying to find.

Here's what our maze looks like:

```
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
1 1 0 1 0
0 0 0 0 9
```

## **Depth-First Search (DFS)**

DFS is like exploring a maze by going as deep as you can before backtracking. Imagine you're in a maze, and you want to find the exit. You start at the beginning and keep moving forward until you hit a dead end. Then you backtrack and try a different path. This is what DFS does!

### **How DFS Works**

1. **The "To-Do" List**: The robot keeps track of places to check using a list called `stack`.
2. **The "Checked" List**: The robot keeps track of places it has already checked using a set called `visited`.
3. **Checking Squares**: The robot checks each square in the maze and prints where it's checking.
4. **Finding the Exit**: If the robot finds the exit (`9`), it prints "EXIT FOUND!" and we're done!

Here's a simple example of how DFS works:

```python
def solve_dfs(start_pos):
    stack = [start_pos]
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(f"Checking square: ({x}, {y})")
        if maze[x][y] == 9:
            print("EXIT FOUND! W 🏁")
            return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
                stack.append((nx, ny))
    print("NO EXIT FOUND 😢")
    return False
```

## **Breadth-First Search (BFS)**

BFS is like exploring a maze by checking all the neighbors at the current depth before moving on to the next depth. Imagine you're in a maze, and you want to find the exit. You start at the beginning and check all the neighbors before moving to the next level. This is what BFS does!

### **How BFS Works**

1. **The "To-Do" List**: The robot keeps track of places to check using a list called `queue`.
2. **The "Checked" List**: The robot keeps track of places it has already checked using a set called `visited`.
3. **Checking Squares**: The robot checks each square in the maze and prints where it's checking.
4. **Finding the Exit**: If the robot finds the exit (`9`), it prints "EXIT FOUND!" and we're done!

Here's a simple example of how BFS works:

```python
def solve_bfs(start_pos):
    queue = [start_pos]
    visited = set()

    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(f"Checking square: ({x}, {y})")
        if maze[x][y] == 9:
            print("EXIT FOUND! W 🏁")
            return True
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
                queue.append((nx, ny))
    print("NO EXIT FOUND 😢")
    return False
```

## **The Hack**

You can turn DFS into BFS by changing `stack.pop()` to `stack.pop(0)`. This changes the order in which the robot checks the squares. Observe how the "Checking square" order changes. Which one feels more 'organized'? BFS is the safe bet; DFS is the YOLO move. Choose your fighter!

## **Summary**

- **DFS**: Go as deep as you can before backtracking.
- **BFS**: Check all neighbors at the current depth before moving on.

Both methods are super cool, and they help us find stuff in a maze! Now you know how to use DFS and BFS to find the exit. Keep shredding, little groms! 🌊🏄‍♂️