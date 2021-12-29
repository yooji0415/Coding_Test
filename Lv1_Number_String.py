def solution(s):
    answer = ''
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    eng = ''
    for elem in s:
        if elem.isdigit():
            answer = answer + elem
        else:
            eng = eng + elem
            if eng in number_dict.keys():
                answer = answer + str(number_dict[eng])
                eng = ''

    return int(answer)


# 모범답안
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def solution(s):
    answer = s
    # key 값을 찾았을 때 바로 value 로 바꿔버린다.
    # replace 함수에 대한 이해와 센스가 중요했다.
    for key, value in num_dic.items():
        answer = answer.replace(key, value)

    return int(answer)
