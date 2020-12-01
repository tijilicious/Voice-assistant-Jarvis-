x=input("enter a string of numbers seperated by spaces")
lst=list()
lst=x.split()
print(lst)
dictionary={}
largest=max(lst)
for number in lst:
    dictionary[number]=dictionary.get(number,0)+1
    print(dictionary)
    for key,value in dictionary:
        print(counts.largest)
