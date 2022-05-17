def solution(genres, plays):
    answer = []
    genre_dict = {}
    play_dict = {}
    for i, g in enumerate(genres):
        if g not in genre_dict:
            genre_dict[g] = [[i, plays[i]]]
            play_dict[g] = plays[i]
        else:
            genre_dict[g].append([i, plays[i]])
            play_dict[g] += plays[i]

    sorted_play_dict = sorted(play_dict.items(), reverse=True, key=lambda item: item[1])
    # print(sorted_play_dict)

    for i in range(len(sorted_play_dict)):
        genre = genre_dict[sorted_play_dict[i][0]]
        # print(genre)
        if len(genre) == 1:
            answer.append(genre[0][0])
        else:
            sorted_genre = sorted(genre, reverse=True, key=lambda x: x[1])
            for j in range(2):
                answer.append(sorted_genre[j][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
