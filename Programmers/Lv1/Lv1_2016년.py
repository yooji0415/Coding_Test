def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    cnt = 0
    if a != 1:
        for i in range(a - 1):
            cnt += month[i]

    cnt += b
    answer = days[(cnt - 1) % 7]
    return answer


# 모범답안
# 아이디어는 동일하나 상당히 깔끔하게 정리된 코드이다
def best_solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
