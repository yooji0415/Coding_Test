def solution(key, lock):
    # 접근 아이디어
    # 1. 일단 lock 사이즈의 3배 크기의 배열을 만들고 해당 배열의 가운데에 lock 정보를 옮긴다.
    # 2. key를 회전시킨 정보를 미리 다 만들어둔다.
    # 3. 해당 key들을 하나씩 새로운 배열의 0,0 부터 마지막 위치까지 한칸씩 대입한다.
    # 4. 이후 겹치는 부분과 비어있는 위치 유무를 확인한다.

    # 1
    key_len = len(key)
    lock_len = len(lock)
    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    for x in range(lock_len, lock_len * 2):
        for y in range(lock_len, lock_len * 2):
            new_lock[x][y] = lock[x - lock_len][y - lock_len]

    # 2
    new_keys = []

    def rotate(graph):
        row = len(graph)
        col = len(graph[0])
        new_graph = [[0] * row for _ in range(col)]
        for x in range(row):
            for y in range(col):
                new_graph[y][row - x - 1] = graph[x][y]
        return new_graph

    new_keys.append(key)
    for i in range(3):
        new_key = rotate(new_keys[-1])
        new_keys.append(new_key)

    # 4
    def check(lock):
        for tx in range(lock_len, lock_len * 2):
            for ty in range(lock_len, lock_len * 2):
                if lock[tx][ty] != 1:
                    return False
        return True

    # 3
    for x in range(1, lock_len * 3 - key_len):
        for y in range(1, lock_len * 3 - key_len):
            for i in range(4):
                new_key = new_keys[i]
                for dx in range(len(key)):
                    for dy in range(len(key)):
                        new_lock[x + dx][y + dy] += new_key[dx][dy]
                if check(new_lock):
                    return True
                for dx in range(len(key)):
                    for dy in range(len(key)):
                        new_lock[x + dx][y + dy] -= new_key[dx][dy]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
