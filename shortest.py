from collections import deque


def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None


def main():
    print("========== SHORTEST PATH FINDER ==========")

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "G"],
        "E": ["B", "G"],
        "F": ["C", "G"],
        "G": ["D", "E", "F"]
    }

    print("\nLocations:")
    print("A, B, C, D, E, F, G")

    start = input("\nEnter starting location: ").upper()
    end = input("Enter destination: ").upper()

    if start not in graph or end not in graph:
        print("\nInvalid location!")
        return

    path = bfs(graph, start, end)

    if path:
        print("\n---------- RESULT ----------")
        print("Shortest Path:", " -> ".join(path))
        print("Number of steps:", len(path) - 1)
    else:
        print("\nNo path found.")


if __name__ == "__main__":
    main()