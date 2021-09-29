class Player:
    def __init__(self, login, score, penalty):
        self.login = login
        self.score = score
        self.penalty = - penalty

    def __str__(self):
        return self.login

def is_score_or_login_better(score_1, score_2, penalty_1, penalty_2, login_1, login_2):
    print('COMPARATOR',score_1, score_2, penalty_1, penalty_2, login_1, login_2)
    if (score_1 == score_2 and penalty_1 < penalty_2):
        print(score_1 == score_2 and penalty_1 < penalty_2)
        return True
    print(False)
    return False

def quick_sort(players, ordering, left,right, less):
    print(ordering)
    if left >= right:
        return
    mid = (left+right)//2
    sep = players[mid].ordering
    #print('pivot', players[mid].score)
    i = left
    j = right
    while True:
        while players[i].score < sep:
            i += 1
        while players[j].score > sep:
            j -= 1
        flag = less(players[i].score,players[j].score,players[i].penalty, players[j].penalty, players[i].login, players[j].login)
        if (i <= j):
            #print(i,j)
            #print(players[i].login, players[i].score, players[j].login, players[j].score)
            players[i], players[j] = players[j], players[i]
            #print(players[i].login, players[i].score, players[j].login, players[j].score)
            i += 1
            j -= 1
        if (i > j):
            break
    quick_sort(players, ordering, left, j, is_score_or_login_better)
    quick_sort(players, ordering, i, right, is_score_or_login_better)



def input_data(file_name):
    with open(file_name, 'r') as data:
        player_num = int(data.readline().strip())
        #data = data.read().splitlines()
        players = []

        for _ in range(player_num):
            login, score , penalty = data.readline().split()
            players.append(Player(login, int(score), int(penalty)))
            #print(players[_].login, players[_].score, players[_].penalty,)

        quick_sort(players, 'score', 0, player_num - 1, is_score_or_login_better)

        for i in reversed(players):
            print(i.login, i.score, i.penalty)
if __name__ == '__main__':
    input_data('input.txt')




#quick_sort(x, 0, len(x)-1)

#print(x)

