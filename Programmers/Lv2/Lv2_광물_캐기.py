answer = int(1e9)


def solution(picks, minerals):
    dia, iron, stone = picks

    def dfs(start_point, result, dia, iron, stone):
        global answer
        if start_point == len(minerals) or dia + iron + stone == 0:
            answer = min(answer, result)
            return

        if dia > 0:
            idx = start_point
            new_result = result
            for mineral in minerals[start_point: start_point + 5]:
                idx += 1
                new_result += 1
            dfs(idx, new_result, dia - 1, iron, stone)

        if iron > 0:
            idx = start_point
            new_result = result
            for mineral in minerals[start_point: start_point + 5]:
                idx += 1
                if mineral == "diamond":
                    new_result += 5
                else:
                    new_result += 1
            dfs(idx, new_result, dia, iron - 1, stone)

        if stone > 0:
            idx = start_point
            new_result = result
            for mineral in minerals[start_point: start_point + 5]:
                idx += 1
                if mineral == "diamond":
                    new_result += 25
                elif mineral == "iron":
                    new_result += 5
                else:
                    new_result += 1
            dfs(idx, new_result, dia, iron, stone - 1)

    dfs(0, 0, dia, iron, stone)
    return answer