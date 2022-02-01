import sys


def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


N = int(sys.stdin.readline())
result = solve_n_queens(N)
print(len(result))

# 풀이 기법은 동일하나 시간을 줄이는데 애매함이 있어서
# 자바를 활용해 실제 문제풀이를 진행


