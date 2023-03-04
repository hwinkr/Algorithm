def solution(today: str, terms: list, privacies: list) -> list:
    answer = []
    day_per_month = 28
    year, month, day = map(int, today.split("."))
    today_number = (year * 12 * day_per_month) + (month * day_per_month) + day

    terms_dict = dict()
    for data in terms:
        types, length = data.split(" ")
        terms_dict[types] = int(length)

    for i in range(len(privacies)):
        start, types = privacies[i].split(" ")
        year, month, day = map(int, start.split("."))
        tmp_number = (
            (year * 12 * day_per_month)
            + (month * day_per_month)
            + day
            + terms_dict[types] * day_per_month
        )
        if today_number >= tmp_number:
            answer.append(i + 1)

    return answer
