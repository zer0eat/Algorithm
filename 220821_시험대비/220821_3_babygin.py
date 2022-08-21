card1 = [4,9,8,4,7,4]
card2 = [4,5,6,7,8,4]


def babygin(card):
    for i in range(len(card)):
        for j in range(len(card)-i):
            if card[i] > card[i+j]:
                card[i], card[i + j] = card[i+j], card[i]

    for i in range(2):
        for c in range(len(card)-3+1):
            if card[c] == card[c+1] == card[c+2]:
                del card[c+2]
                del card[c+1]
                del card[c]
                break
    for i in range(2):
        for c in range(len(card)-3+1):
            if card[c] + 2 == card[c+1] + 1 == card[c+2]:
                del card[c+2]
                del card[c+1]
                del card[c]
                break

    if card == []:
        return 'babygin!'
    else:
        return 'lose'

print(babygin(card1))

print(babygin(card2))