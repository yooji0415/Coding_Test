from collections import deque

def solution(order):
    answer = 0
    od = deque(order)
    dq = deque([x for x in range(1, len(order) + 1)])
    st = []
    
    while len(dq) >= 0 and len(od) > 0:
        if len(dq) == 0:
            while len(st) != 0 and od[0] == st[-1]:
                od.popleft()
                st.pop()
                answer += 1
            break
        
        if od[0] == dq[0]:
            od.popleft()
            dq.popleft()
            answer += 1
            continue
        if len(st) != 0 and od[0] == st[-1]:
            od.popleft()
            st.pop()
            answer += 1
            continue
        st.append(dq.popleft())   
        
    return answer