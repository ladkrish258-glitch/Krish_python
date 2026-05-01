def fact(num):
    if num==1:
        return 1
    else:
        fa=num*fact(num-1)
        return fa

    


num=int(input("Enter Number : "))
print(fact(num))
