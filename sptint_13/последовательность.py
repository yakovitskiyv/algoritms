def is_subseq(seq, sub_seq):


    start = -1
    for i in seq:
      start = sub_seq.find(i, start + 1)
      if start == -1:
        return False
    return True


def input_data(file_name):
    with open(file_name, 'r') as data:
        seq = data.readline().strip()
        sub_seq = data.readline().strip()
        res = (is_subseq(seq, sub_seq))
        print(res)

if __name__ == '__main__':
    input_data('input.txt')
