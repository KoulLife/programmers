from sys import stdin

input = stdin.readline

N = int(input())
num_cards = list(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))

card_dict = {}

for card in num_cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for check in check_list:
    if check not in card_dict:
        print("0", end=" ")
    else:
        print(card_dict[check], end=" ")