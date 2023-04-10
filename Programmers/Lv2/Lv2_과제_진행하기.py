from collections import deque


def solution(plans):
    answer = []
    times = []
    stack = []
    for plan in plans:
        name, start, duration = plan
        hour, minute = map(int, start.split(":"))
        start_time = hour * 60 + minute
        end_time = start_time + int(duration)
        times.append((name, start_time, end_time))
    
    times.sort(key=lambda x:x[1])
    times = deque(times)
    time = times[0][1]
    while times:
        name, now_start, now_end = times.popleft()
        if not times:
            time = now_end
            answer.append(name)
            break
        
        next_start = times[0][1]
        if now_end > next_start:
            stack.append([name, now_end - next_start])
            time = next_start
            continue
            
        if now_end == next_start:
            time = next_start
            answer.append(name)
            continue
        
        time = now_end
        answer.append(name)
        while stack:
            if time + stack[-1][1] <= next_start:
                name, left = stack.pop()
                answer.append(name)
                time += left
            else:
                stack[-1][1] -= next_start - time
                break
        
    while stack:
        name, left = stack.pop()
        answer.append(name)
    
    return answer