n = int(input())
total = n 
bill = 0 
while total != 0: 
    if int(total/100) != 0:
        bill += int(total/100)
        total -= int(total/100)*100
    elif int(total/20) != 0:
        bill += int(total/20)
        total -= int(total/20)*20
    elif int(total/10) != 0:
        bill += int(total/10)
        total -= int(total/10)*10
    elif int(total/5) != 0:
        bill += int(total/5)
        total -= int(total/5)*5
    elif int(total/1) != 0:
        bill += int(total/1)
        total -= int(total/1)*1
print(bill)