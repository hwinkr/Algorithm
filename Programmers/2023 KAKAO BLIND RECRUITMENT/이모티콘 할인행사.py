def sol(users: list, emoticons: list, tmp: list, rates: list) -> list:
    global total_member, total_money
    if len(tmp) == len(emoticons):
        member, money = 0, 0
        for user in users:
            is_member = False
            rate, limit = user
            curr = 0
            for i in range(len(emoticons)):
                if rate <= tmp[i]:
                    curr += emoticons[i] - (emoticons[i] // 100 * tmp[i])
                    if curr >= limit:
                        is_member = True
                        member += 1
                        break
            # ! 전체 사용자가 이모티콘에 사용하는 돈, 즉 이모티콘 할인 행사로 인해서 얻는 총 금액을 의미한다..
            if not is_member:
                money += curr

        if member > total_member:
            total_member = member
            total_money = money
        elif member == total_member and money > total_money:
            total_money = money

        return

    for i in range(4):
        tmp.append(rates[i])
        sol(users, emoticons, tmp, rates)
        tmp.pop()


total_member, total_money = -1, -1


def solution(users, emoticons) -> list:
    sol(users, emoticons, [], [10, 20, 30, 40])
    return [total_member, total_money]
