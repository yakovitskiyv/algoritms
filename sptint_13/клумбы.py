def mapper(segment_num, data):
    map_seg =[]
    for i in data:
        segment = list(map(int, i.split()))
        #if segment not in map_seg:
        map_seg.append(segment)

    res_arr =[]

    map_seg =(sorted(map_seg))
    #print(map_seg)
    start = map_seg[0]

    for i in range(len(map_seg)):
        if map_seg[i][0] <= start[1]:
            start[1] = max(start[1], map_seg[i][1])

        else:
            res_arr.append(start)
            print(*start)
            start = map_seg[i]
            continue

    res_arr.append(start)
    print(*start)
    return res_arr



def input_data(file_name):
    with open(file_name, 'r') as data:
        segment_num = int(data.readline().strip())
        data = data.read().splitlines()
        res = (mapper(segment_num, data))

        
if __name__ == '__main__':
    input_data('input.txt')
