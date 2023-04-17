def solution(sequence, k):
    answer = []
    length = len(sequence)
    start = 0
    end = 0
    result = sequence[0]
    while end < len(sequence):
        if result == k and length > end - start:
            length = end - start
            if length == 0:
                return [start, end]
            answer = [start, end]
        
        if result < k:
            end += 1
            if len(sequence) == end:
                break
            result += sequence[end]
        else:
            result -= sequence[start]
            start += 1

    return answer