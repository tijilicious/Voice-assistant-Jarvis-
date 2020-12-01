

import numpy as np
from scipy.spatial.distance import cdist
import datetime
import geocoder # process of converting addresses (like a street address) into 
                #geographic coordinates (like latitude and longitude), 
                #which you can use to place markers on a map, or position the map



def location():
    ipadd = geocoder.ip('me')
    return ipadd.latlng




def hotel_owner_interface():
    data = []
    hotel_name = input("Enter the hotel name : ") 
    vacant_room = input("Vacant rooms are :" )
    avalaibilty_status=int(input("hotel available for maximum days"))
    Record = {hotel_name:(vacant_room, location())}
    data.append(Record)
    return Record
    

    

#now=datetime.date.today()
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


def user_interface():
    name = input("Enter name :  " )
    use_position=location()

hotel_owner_interface()

for location() in Record:
    distance = np.min(cdist(user_position, hotel_position))
    list1=lst.append(distance)
    print(list1)







