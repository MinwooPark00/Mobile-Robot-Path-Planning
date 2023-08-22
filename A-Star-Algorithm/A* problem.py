# start: Tuple[int, int], end: Tuple[int, int], obstacles: List[Tuple[int, int]] -> shortest_path: List[Tuple[int, int]]
# Use Manhattan distance as the heuristic function
def find_shortest_path(start, end, obstacles):
    shortest_path = [start, end]
    return shortest_path

if __name__ == '__main__':
    start = (0, 0)
    end = (10, 10)
    obastacles = [(1, 1), (3, 4)]
    print(find_shortest_path(start, end, obastacles))