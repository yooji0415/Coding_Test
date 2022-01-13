word_list = []
insert_items = []
cycle = int(input())
for i in range(cycle):
    word = input()
    if word not in insert_items:
        word_len = len(word)
        word_list.append([word_len, word])
        insert_items.append(word)

word_list.sort(key=lambda x: (x[0], x[1]))

for j in range(len(word_list)):
    print(word_list[j][1])