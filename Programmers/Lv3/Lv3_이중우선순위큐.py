import heapq


def solution(operations):
    answer = []
    max_queue = []
    min_queue = []
    for op in operations:
        op_list = op.split()
        if op_list[0] == "I":
            heapq.heappush(min_queue, int(op_list[1]))
            heapq.heappush(max_queue, - int(op_list[1]))
        else:
            if not max_queue:
                continue

            if op_list[1] == "-1":
                temp = heapq.heappop(min_queue)
                max_queue.remove(-temp)
            else:
                temp = heapq.heappop(max_queue)
                min_queue.remove(-temp)

    if not max_queue:
        return [0, 0]

    return [-heapq.heappop(max_queue), heapq.heappop(min_queue)]
