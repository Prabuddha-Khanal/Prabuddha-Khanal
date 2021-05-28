import datetime

x = datetime.datetime.now()
query = (x.strftime("%A"))
h = int(datetime.datetime.now().hour)
m = int(datetime.datetime.now().minute)

if 'Sunday' in query:
    b=1

elif 'Monday' in query:
    b=2

elif 'Tuesday' in query:
    b=3

elif 'Wednesday' in query:
    b=4

elif 'Thursday' in query:
    b=5

elif 'Friday' in query:
    b=6

elif 'Saturday' in query:
    b=7

if b == 1 and h <= 9 and h >= 8:
    clas='have Science class'

elif b == 1 and h <= 10 and h >= 9 and m < 40:
    clas='have Social class'

elif b == 1 and h <= 11 and h >= 10 and m < 40:
    clas='have English class'

elif b == 1 and h <= 12 and h >= 11 and m < 15:
    clas='have Cmath class'

elif b == 1 and h <= 13 and h >= 12 and m < 15:
    clas='have Omath class'

elif b == 2 and h <= 9 and h >= 8:
    clas='have Computer class'

elif b == 2 and h <= 10 and h >= 9 and m < 40:
    clas='have Social class'

elif b == 2 and h <= 11 and h >= 10 and m < 40:
    clas='have Nepali class'

elif b == 2 and h <= 12 and h >= 11 and m < 15:
    clas='have Cmath class'

elif b == 2 and h <= 13 and h >= 12 and m < 15:
    clas='have Omath class'

elif b == 3 and h <= 9 and h >= 8:
    clas='have Social class'

elif b == 3 and h <= 10 and h >= 9 and m < 40:
    clas='have Science class'

elif b == 3 and h <= 11 and h >= 10 and m < 40:
    clas='have Nepali class'

elif b == 3 and h <= 12 and h >= 11 and m < 15:
    clas='have e,p,h class'

elif b == 3 and h <= 13 and h >= 12 and m < 15:
    clas='have Omath class'

elif b == 4 and h <= 9 and h >= 8:
    clas='have Computer class'

elif b == 4 and h <= 10 and h >= 9 and m < 40:
    clas='have Science class'

elif b == 4 and h <= 11 and h >= 10 and m < 40:
    clas='have e,p,h class'

elif b == 4 and h <= 12 and h >= 11 and m < 15:
    clas='have Cmath class'

elif b == 4 and h <= 13 and h >= 12 and m < 15:
    clas='have English class'

elif b == 5 and h <= 9 and h >= 8:
    clas='have Nepali class'

elif b == 5 and h <= 10 and h >= 9 and m < 40:
    clas='have Science class'

elif b == 5 and h <= 11 and h >= 10 and m < 40:
    clas='have Computer class'

elif b == 5 and h <= 12 and h >= 11 and m < 15:
    clas='have English class'

elif b == 5 and h <= 13 and h >= 12 and m < 15:
    clas='have Omath class'

elif b == 6 and h <= 9 and h >= 8:
    clas='have Social class'

elif b == 6 and h <= 10 and h >= 9 and m < 40:
    clas='have e,p,h class'

elif b == 6 and h <= 11 and h >= 10 and m < 40:
    clas='have Nepali class'

elif b == 6 and h <= 12 and h >= 11 and m < 15:
    clas='have Cmath class'

elif b == 6 and h <= 13 and h >= 12 and m < 15:
    clas='have English class'

elif b == 7:
    clas='have holiday'
else:
    clas='do not have class right now'