def solution(enroll, referral, seller, amount):
    node_dict = {enroll[i] : [referral[i], 0] for i in range(len(enroll))}
    for i in range(len(seller)):
        name = seller[i]
        money = amount[i] * 100
        share = int(money * 0.1)
        money -= share
        node_dict[name][1] += money
        parent = node_dict[name][0]
        while parent != "-":
            money = share
            share = int(money * 0.1)
            money -= share
            if money <= 0:
                break
            node_dict[parent][1] += money
            parent = node_dict[parent][0]
    answer = [node_dict[name][1] for name in enroll]
    return answer