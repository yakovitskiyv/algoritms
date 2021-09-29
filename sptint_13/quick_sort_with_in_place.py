# ID:53649807


def quick_sort(players, left, right):
    if left >= right:
        return
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
    quick_sort(players, left, j)
    quick_sort(players, i, right)


def input_data(file_name):
    with open(file_name, 'r') as data:
        player_num = int(data.readline().strip())
        players = []
        for _ in range(player_num):
            login, score, penalty = data.readline().split()
            players.append([int(score) * -1, int(penalty), login])
        quick_sort(players, 0, player_num - 1)
        for item in players:
            print(item[2])


if __name__ == '__main__':
    input_data('input.txt')
