def solution(a):
    answer = 0
    # 일단 a의 길이가 1이나 2인 경우는 답이 명확하므로 
    # 먼저 처리를 해줄 것 같습니다.
    if len(a) <= 2: 
        return len(a)
    
    # 이 문제를 관통하는 아이디어는 현 인덱스 기준으로
    # 좌측의 가장 작은 수, 우측의 가장 작은 수를 찾고
    # 이를 비교해서 판별하는 것이 중요할 것 같습니다.
    
    rA = list(reversed(a))
    left = []
    right = []
    
    for i in range(len(a)):
        if i == 0:
            left.append(a[i])
            right.append(rA[i])
            continue
        
        left.append(a[i] if a[i] < left[-1] else left[-1])
        right.append(rA[i] if rA[i] < right[-1] else right[-1])
    
    right = list(reversed(right))
    
    for i in range(len(a)):
        if i == 0 or i == len(a) - 1:
            answer += 1
            continue
        
        if left[i - 1] < a[i] and right[i + 1] < a[i]:
            continue
        
        answer += 1
    # print(left)
    # print(right)
    
    return answer