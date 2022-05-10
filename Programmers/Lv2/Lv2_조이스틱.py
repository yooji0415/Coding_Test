def solution(name):
    alpha_dict = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
        "L": 11, "M": 12, "N": 13, "O": 12, "P": 11, "Q": 10, "R": 9, "S": 8, "T": 7, "U": 6, "V": 5,
        "W": 4, "X": 3, "Y": 2, "Z": 1
    }

    move = len(name) - 1
    answer = 0
    for i, alpha in enumerate(name):
        answer += alpha_dict[alpha]
        next_ = i + 1
        while next_ < len(name) and name[next_] == 'A':
            next_ += 1

        move = min([move, 2 * i + len(name) - next_, i + 2 * (len(name) - next_)])

    answer += move
    return answer
