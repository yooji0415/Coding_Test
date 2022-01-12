def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_zero = 0
    for i in range(0, len(lottos)):
        if lottos[i] == 0:
            cnt_zero += 1
            continue
        for j in range(0, len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
                break

    if cnt + cnt_zero == 6:
        answer.append(1)
    elif cnt + cnt_zero == 0:
        answer.append(6)
    else:
        answer.append(7 - cnt - cnt_zero)

    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7 - cnt)

    return answer


# 모범 답안
def best_solution(lottos, win_nums):
        
    # 등수와 맞은 개수의 합과 연관이 있다는 것은 확인했으나
    # 이렇게 리스트 구조로 작성시 인덱스와 연결할 수 있다는
    # 생각을 못했다.
    rank = [6, 6, 5, 4, 3, 2, 1]
        
    # 파이썬의 내장함수 count 를 이용하면 더 쉽게 할 수 있다.
    cnt_0 = lottos.count(0)
    ans = 0
        
    # 맞은 개수 또한 파이썬의 리스트 for 문 연산 방법을
    # 사용하면 더 쉽게 해결할 수 있다.
    for x in win_nums:
        if x in lottos:
            ans += 1
                
    # 리스트 변수를 이용한 return 이 아닌 개별 return 도
    # 리스트 구조로 전달이 되는 것을 알게 되었다.
    return rank[cnt_0 + ans], rank[ans]
