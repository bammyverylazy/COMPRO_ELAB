times= int(input())
times+=1
row=times


for k in range(0,times+1):
    for i in range(1,k+1):
        if k==1:
            continue
        for j in range(i):
            print(" "*(row-i),end="")
            print("*"*((i*2)-1),end="")
            break
        print()
        
times-=1
print(" "*(times-1),"|")
print("="*(times)+"V"+"="*(times))
