def solution(m, musicinfos):
    answer = None
    m = m.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'O').replace('A#', 'P')

    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")

        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start

        code = code.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'O').replace('A#', 'P')
        code *= ((duration // len(code)) + 1)
        code = code[:duration]

        if m not in code:
            continue

        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
            answer = (duration, start, title)

    if answer:
        return answer[-1]

    return "(None)"

