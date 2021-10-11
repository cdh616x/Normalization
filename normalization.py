mylist = []
num = 0
num_flo = int(input("How many numbers would you like to see in the output?:\n"))
while len(mylist) < num_flo:
    i = float(input())
    mylist.append(i)
    if len(mylist) == num_flo:
        break
maxnum = max(mylist)
for i in mylist:
    print(f"{i / maxnum:.2f}")
