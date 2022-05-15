def solution(enroll, referral, seller, amount):
    graph = {x: "" for x in enroll}
    money = {x: 0 for x in enroll}
    # 본인 상위 노드를 연결
    for i, ref in enumerate(referral):
        if ref == "-":
            graph[enroll[i]] = "center"
        else:
            graph[enroll[i]] = ref

    # 판매 수익 분배
    for i, s in enumerate(seller):
        now = s
        total = amount[i] * 100
        # 우선 판매자 부터 수익 계산
        money[now] += total - total // 10
        total //= 10
        # 이후 상위 노드들 수익 분배
        while graph[now] != "center" and total != 0:
            now = graph[now]
            money[now] += total - total // 10
            total //= 10

    return list(money.values())
