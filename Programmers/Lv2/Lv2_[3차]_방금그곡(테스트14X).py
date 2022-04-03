def solution(m, musicinfos):
    music_dict = {}
    for input_num, music in enumerate(musicinfos):
        music = music.split(',')
        start = list(map(int, music[0].split(':')))
        end = list(map(int, music[1].split(':')))
        name = music[2]

        time = 0
        if start[1] > end[1]:
            time = (end[0] - start[0] - 1) * 60 + end[1] - start[1]
        else:
            time = (end[0] - start[0]) * 60 + end[1] - start[1]

        melody = music[3]
        melody = melody.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'O').replace('A#', 'P')
        melody_list = list(melody)

        melody_list = melody_list * (time // len(melody_list)) + melody_list[:time % len(melody_list)]
        remake_melody = ''.join(melody_list)

        music_dict[name] = [time, remake_melody, input_num]

    m = m.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'O').replace('A#', 'P')
    m_list = list(m)

    remake_m = ''.join(m_list)
    # print(remake_m)
    # print(music_dict)
    can = []
    for name, value in music_dict.items():
        if remake_m in value[1]:
            can.append([name, value[0], value[2]])

    if not can:
        return "(None)"
    else:
        can.sort(key=lambda x: (x[1], -x[2]))
        # print(can)
        return can[-1][0]


print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
