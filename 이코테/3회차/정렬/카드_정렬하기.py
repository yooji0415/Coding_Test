from heapq import heappush, heappop


def solution(N, cards):
        q = []
        for card in cards:
            heappush(q, card)
        answer = 0
        while len(q) > 1:
            num1 = heappop(q)
            num2 = heappop(q)
            answer += num1 + num2
            heappush(q, num1 + num2)
        return answer


print(solution(3, [10, 20, 40]))
