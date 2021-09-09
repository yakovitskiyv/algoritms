# ID: 52440569


from collections import Counter


def get_max_score():
    fingers = int(input()) * 2
    game_matrix = []
    for number in range(4):
        numbers = input()
        game_matrix += numbers
    max_score = sum(1 for key, value in Counter(
        game_matrix).items() if key.isdigit() and value <= fingers)
    return max_score


if __name__ == '__main__':
    print(get_max_score())
