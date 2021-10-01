# ID: 53706986


from collections import namedtuple
from typing import List, NamedTuple


def partition(players: List[NamedTuple], left: int, right: int) -> int:
    mid = (left+right)//2
    sep = players[mid]
    i = left
    j = right
    while True:
        while players[i] < sep:
            i += 1
        while players[j] > sep:
            j -= 1
        if (i <= j):
            players[i], players[j] = players[j], players[i]
            i += 1
            j -= 1
        if (i > j):
            break
    return i, j


def quick_sort(players: List[NamedTuple], left: int, right: int) -> None:
    if left >= right:
        return
    new_left, new_right = partition(players, left, right)
    quick_sort(players, left, new_right)
    quick_sort(players, new_left, right)


def input_data(file_name: str):
    with open(file_name, 'r') as data:
        player_num = int(data.readline().strip())
        player = namedtuple('player', ['score', 'penalty', 'login'])
        players = []
        for _ in range(player_num):
            login, score, penalty = data.readline().split()
            players.append(player(int(score) * -1, int(penalty), login))
        quick_sort(players, 0, player_num - 1)

        for player in players:
            print(player.login)


if __name__ == '__main__':
    input_data('input.txt')
