y = int(input())
if y%4 == 0 and y%100 != 0:
    print("yes")
elif y%400 == 0:
    print("yes")
else:
    print("no")
