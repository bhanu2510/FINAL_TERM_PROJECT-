import rubik_cube
from rubik_cube import *
import time
from collections import deque


from collections import deque

def shortest_path(start_state, end_state):
    visited = {}
    visited[start_state] = (start_state, -1)
    queue = deque([start_state])

    while queue:
        current_state = queue.popleft()

        if current_state == end_state:
            break

        for twist in rubik_cube.quarter_twists:
            next_state = rubik_cube.perm_apply(current_state, twist)

            if next_state not in visited:
                visited[next_state] = (current_state, rubik_cube.quarter_twists_names[twist])
                queue.append(next_state)

    if len(visited) == 1:
        return []

    if end_state in visited:
        path = []
        current_node = end_state

        while current_node != start_state:
            prev_node, current_twist = visited[current_node]
            path.append(current_twist)
            current_node = prev_node

        return list(reversed(path))

    else:
        return None

def shortest_path_optimized (start_state, end_state):
    if start_state == end_state:
        return []

    start_parent = {}
    end_parent = {}
    visited_start = set()
    visited_end = set()
    start_queue = deque()
    start_queue.append(start_state)
    end_queue = deque()
    end_queue.append(end_state)
    start_dist = {start_state: 0}
    end_dist = {end_state: 0}
    found = False

    while start_queue or end_queue:
        if start_queue:
            current_state = start_queue.popleft()

            for action in rubik_cube.quarter_twists:
                neighbor_state = rubik_cube.perm_apply(action, current_state)
                if neighbor_state in start_dist.keys():
                    if start_dist[neighbor_state] > start_dist[current_state] + 1:
                        start_dist[neighbor_state] = start_dist[current_state] + 1
                        start_parent[neighbor_state] = (current_state, action)
                        start_queue.append(neighbor_state)
                else:
                    start_dist[neighbor_state] = start_dist[current_state] + 1
                    start_parent[neighbor_state] = (current_state, action)
                    start_queue.append(neighbor_state)

            visited_start.add(current_state)

        if current_state in visited_end and current_state in visited_start:
            found = True
            break

        if end_queue:
            current_state = end_queue.popleft()

            for action in rubik_cube.quarter_twists:
                neighbor_state = rubik_cube.perm_apply(action, current_state)
                if neighbor_state in end_dist.keys():
                    if end_dist[neighbor_state] > end_dist[current_state] + 1:
                        end_dist[neighbor_state] = end_dist[current_state] + 1
                        end_parent[neighbor_state] = (current_state, action)
                        end_queue.append(neighbor_state)
                else:
                    end_dist[neighbor_state] = end_dist[current_state] + 1
                    end_parent[neighbor_state] = (current_state, action)
                    end_queue.append(neighbor_state)

            visited_end.add(current_state)

        if current_state in visited_start and current_state in visited_end:
            found = True
            break

    if found:
        inverse_twists = {F: Fi, L: Li, U: Ui, Fi: F, Li: L, Ui: U}
        moves_to_start = [rubik_cube.quarter_twists_names[start_parent[current_state][1]]]
        parent = start_parent[current_state][0]

        while parent != start_state:
            moves_to_start.append(rubik_cube.quarter_twists_names[start_parent[parent][1]])
            parent = start_parent[parent][0]

        moves_to_end = []

        if current_state != end_state:
            moves_to_end = [rubik_cube.quarter_twists_names[inverse_twists[end_parent[current_state][1]]]]
            parent = end_parent[current_state][0]

            while parent != end_state:
                moves_to_end.append(rubik_cube.quarter_twists_names[inverse_twists[end_parent[parent][1]]])
                parent = end_parent[parent][0]

        return moves_to_start[::-1] + moves_to_end

    else:
        return None


start = time.time()
path = shortest_path(
                     (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                    #  (23,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
                    #(19, 2, 9, 6, 16, 17, 3, 13, 12, 23, 20, 14, 5, 1, 22, 7, 0, 10, 18, 11, 21, 4, 8, 15), 
                     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end = time.time()

print("PATH found by normal bfs:" + str(path))
print("time in secs by normal bfs:" + str(end - start))


start = time.time()
path = shortest_path_optimized(
                    (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                    #  (3, 4, 5,6, 7, 8, 20, 18, 19,  16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                    #  (23,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
                     #(20, 18, 19,6, 7, 8, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end = time.time()

print("PATH found by bidirectional bfs:" + str(path))
print("time in secs by bidirectional bfs:" + str(end - start))