x = int(input())
k = 0
for i in range(1,x+1):
    if x%i == 0: k += 1
if k <= 2: print("Простое")
else: print("Составное")