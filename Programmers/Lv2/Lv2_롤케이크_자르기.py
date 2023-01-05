def solution(topping):
    answer = 0
    setA, setB = set(), set()
    a, b = [], []
    tLen = len(topping)
    for i in range(tLen):
        setA.add(topping[i])
        if(i != 0):
            setB.add(topping[-i])
        a.append(len(setA))
        b.append(len(setB))
    
    b.reverse()
    for i in range(len(a)):
        if a[i] == b[i]:
            answer += 1
    return answer