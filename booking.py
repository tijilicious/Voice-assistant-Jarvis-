import datetime
now=datetime.date.today()
#print(now)
def booking():
    n=int(input("enter the number of days of stay: "))
    if n==1:
        today=datetime.date.today()
        dt=datetime.timedelta(1)
        tomorrow=today+dt
        print("booking valid from 12 PM",today )
        print("booking valid till 11 AM",tomorrow)
    else:
        today=datetime.date.today()
        dt=datetime.timedelta(n)
        day=today+dt
        print("booking valid from 12 PM",today )
        print("booking valid till 11 AM",day)


booking() 