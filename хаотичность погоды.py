days = input()
tempp= list(map(int, input().split()))

tempp=[min(tempp)-1]+tempp+[min(tempp)-1]
w_ch=len([n for n in range(1,len(tempp)) if tempp[n-1]<tempp[n] >tempp[n+1]])

print(w_ch)
