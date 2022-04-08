def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            bin_number = bin(number)[2:]
            reverse_bin_number = bin_number[::-1]
            index = bin_number.find('0')
            if index == -1:
                result = reverse_bin_number.replace('1', '10', 1)
                answer.append(int(result, 2))
            else:
                result = reverse_bin_number.replace('10', '01', 1)
                answer.append(int(result[::-1], 2))
    return answer
