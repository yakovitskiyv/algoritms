

def gen_binary(n, prefix, count0, count1):
    print('main:', 'n', n, 'prefix', prefix, count0, count1)
    if n == 0:
        print(prefix)
    else:

        print('bafore GEN', 'n',n, 'prefix',prefix, count, count1)
        gen_binary(n - 1, prefix + '0', count0, count1)
        count0 += 1
        print('AFTER 0'', n',n, 'prefix',prefix, count0, count1)
        count1+=1
        gen_binary(n - 1, prefix + '1', count0, count1)
        print('AFTER 1', 'n',n, 'prefix',prefix, count0, count1)

count=0
gen_binary(2, '', 0, 0)
