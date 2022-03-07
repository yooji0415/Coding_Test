def solution(phone_book):
    p = sorted(phone_book)
    for i in range(len(p) - 1):
        if len(p[i]) <= len(p[i + 1]):
            if p[i] == p[i + 1][:len(p[i])]:
                return False

    return True
