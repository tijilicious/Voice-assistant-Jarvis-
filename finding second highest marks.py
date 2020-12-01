n=input()
a=input()
lst=list()
for x in a:
    lst=x.split()
lst.sort()
print(lst)
for number in lst:
    while True:
        number[n-1]>=number[n-2]
        n-=1
        break
        print(number)