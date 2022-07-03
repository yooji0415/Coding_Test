import sys

string = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

cnt = 0
word_len = len(word)
start, end = 0, word_len
while end <= len(string):
    if string[start:end] == word:
        cnt += 1
        start += word_len
        end += word_len
    else:
        start += 1
        end += 1

print(cnt)
