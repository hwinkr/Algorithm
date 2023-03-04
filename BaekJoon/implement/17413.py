import sys

input = sys.stdin.readline


def reverse_item(sentence: str, start: int, end: int):
    sentence = list(sentence)
    tmp = sentence[start : end + 1]
    tmp.reverse()
    sentence[start : end + 1] = tmp
    return "".join(sentence)


def sol(sentence: str):
    is_tag = False
    end = -1
    tmp = ""
    for i in range(len(sentence)):
        if is_tag:
            if sentence[i] == ">":
                is_tag = False
            continue
        elif sentence[i] == "<":
            if tmp:
                sentence = reverse_item(sentence, end - (len(tmp) - 1), end)
                tmp = ""
            is_tag = True
            continue
        elif sentence[i] == " ":
            if tmp:
                sentence = reverse_item(sentence, end - (len(tmp) - 1), end)
                tmp = ""
            continue
        else:
            tmp += sentence[i]
            end = i

    if tmp:
        sentence = reverse_item(sentence, end - (len(tmp) - 1), end)
    return sentence


if __name__ == "__main__":
    sentence = input()
    sentence = sol(sentence[:-1])
    print(sentence)
