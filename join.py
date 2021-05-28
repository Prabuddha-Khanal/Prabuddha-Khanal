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
    c='https://us04web.zoom.us/j/8179631871?pwd=MFRsaDhKUXdialpxK2lhMEFlK2p4dz09'

elif b == 1 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/6932248639?pwd=bU1EY2JMcGR4cW0zeWt5SEhYK1gxZz09'

elif b == 1 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/9123083024?pwd=ZjVFZ0x6bFAyM1c1dVptQ0ZMYTBPdz09'

elif b == 1 and h <= 12 and h >= 11 and m < 15:
    c='have Cmath class'

elif b == 1 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/2665071459?pwd=TEJUTVdPTnFMRVJGU3dlN2xydTEwUT09'

elif b == 2 and h <= 9 and h >= 8:
    c='https://us04web.zoom.us/j/3327293188?pwd=Ymt0ZlZCeFNUN0pRNTVDRkltdUU0dz09'

elif b == 2 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/6932248639?pwd=bU1EY2JMcGR4cW0zeWt5SEhYK1gxZz09'

elif b == 2 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/7368450506?pwd=c1p1dy9nQi9VTnREM3pvWS9PRE13Zz09'

elif b == 2 and h <= 12 and h >= 11 and m < 15:
    c='have Cmath class'

elif b == 2 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/2665071459?pwd=TEJUTVdPTnFMRVJGU3dlN2xydTEwUT09'

elif b == 3 and h <= 9 and h >= 8:
    c='https://us04web.zoom.us/j/6932248639?pwd=bU1EY2JMcGR4cW0zeWt5SEhYK1gxZz09'

elif b == 3 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/8179631871?pwd=MFRsaDhKUXdialpxK2lhMEFlK2p4dz09'

elif b == 3 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/7368450506?pwd=c1p1dy9nQi9VTnREM3pvWS9PRE13Zz09'

elif b == 3 and h <= 12 and h >= 11 and m < 15:
    c='https://us04web.zoom.us/j/8835021339?pwd=YisrSTVKWFBsT0JUS1hqbEYrQktqQT09'

elif b == 3 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/2665071459?pwd=TEJUTVdPTnFMRVJGU3dlN2xydTEwUT09'

elif b == 4 and h <= 9 and h >= 8:
    c='https://us04web.zoom.us/j/3327293188?pwd=Ymt0ZlZCeFNUN0pRNTVDRkltdUU0dz09'

elif b == 4 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/8179631871?pwd=MFRsaDhKUXdialpxK2lhMEFlK2p4dz09'

elif b == 4 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/8835021339?pwd=YisrSTVKWFBsT0JUS1hqbEYrQktqQT09'

elif b == 4 and h <= 12 and h >= 11 and m < 15:
    c='have Cmath class'

elif b == 4 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/9123083024?pwd=ZjVFZ0x6bFAyM1c1dVptQ0ZMYTBPdz09'

elif b == 5 and h <= 9 and h >= 8:
    c='https://us04web.zoom.us/j/7368450506?pwd=c1p1dy9nQi9VTnREM3pvWS9PRE13Zz09'

elif b == 5 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/8179631871?pwd=MFRsaDhKUXdialpxK2lhMEFlK2p4dz09'

elif b == 5 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/3327293188?pwd=Ymt0ZlZCeFNUN0pRNTVDRkltdUU0dz09'

elif b == 5 and h <= 12 and h >= 11 and m < 15:
    c='https://us04web.zoom.us/j/9123083024?pwd=ZjVFZ0x6bFAyM1c1dVptQ0ZMYTBPdz09'

elif b == 5 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/2665071459?pwd=TEJUTVdPTnFMRVJGU3dlN2xydTEwUT09'

elif b == 6 and h <= 9 and h >= 8:
    c='https://us04web.zoom.us/j/6932248639?pwd=bU1EY2JMcGR4cW0zeWt5SEhYK1gxZz09'

elif b == 6 and h <= 10 and h >= 9 and m < 40:
    c='https://us04web.zoom.us/j/8835021339?pwd=YisrSTVKWFBsT0JUS1hqbEYrQktqQT09'

elif b == 6 and h <= 11 and h >= 10 and m < 40:
    c='https://us04web.zoom.us/j/7368450506?pwd=c1p1dy9nQi9VTnREM3pvWS9PRE13Zz09'

elif b == 6 and h <= 12 and h >= 11 and m < 15:
    c='have Cmath class'

elif b == 6 and h <= 13 and h >= 12 and m < 15:
    c='https://us04web.zoom.us/j/9123083024?pwd=ZjVFZ0x6bFAyM1c1dVptQ0ZMYTBPdz09'

elif b == 7:
    c='https://us04web.zoom.us/j/9123083024?pwd=ZjVFZ0x6bFAyM1c1dVptQ0ZMYTBPdz09'

else:
    c='youtube.com'