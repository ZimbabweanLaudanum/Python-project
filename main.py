a=str(input("Введите список"))
n=a.count(" ")+1
af=list(map(int, a.split()))
for i in range(n-1):
    for j in range(n-i-1):
        if af[j] > af[j+1]:
            af[j], af[j+1] = af[j+1], af[j]
print(af)