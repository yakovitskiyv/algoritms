def mapper(segment_num, data):
    map_seg =[]
    for i in data:
        segment = list(map(int, i.split()))
        if segment not in map_seg:
            map_seg.append(segment)


    left = 0
    right = 1          
    for left, right in map_seg:
        print(left, right)
        print(map_seg)
        for left_next, right_next in map_seg:

            if (left > left_next and right >= right_next):
                map_seg.append([left_next, right])
                map_seg.remove([left, right])
                map_seg.remove([left_next, right_next])
            
            
            #or (left == left_next and right < right_next):
                


        















def input_data(file_name):
    with open(file_name, 'r') as data:
        segment_num = int(data.readline().strip())
        data = data.read().splitlines()
        print(segment_num)  
        print(data)
        mapper(segment_num, data)
        
if __name__ == '__main__':
    input_data('input.txt')