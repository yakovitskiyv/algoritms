def input_data():
    seq = input()
    return is_correct_bracket_seq(seq)


def is_correct_bracket_seq(seq):
    stack =[]
    is_correct = True
    for char in seq:
        if char in '({[':
            stack.append(char)

        elif char in ')}]':
            if not stack:
                is_correct = False
                break
            open_char = stack.pop()
            if open_char == '(' and char == ')':
                continue
            if open_char == '{' and char == '}':
                continue
            if open_char == '[' and char == ']':
                continue
            is_correct = False
            break

    if is_correct and len(stack) == 0:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    input_data()
