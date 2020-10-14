from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HeroSerializer, SolarSerializer
from .models import Hero, Solar
from django.shortcuts import render
import http.client
import json
from django.http import HttpResponse


relay = [0,0,0,0,0,0,0,0]

relay_status = ["off","off","off","off","off","off","off","off"]

conn = http.client.HTTPSConnection('api.pipedream.com')
conn.request("GET", '/v1/sources/dc_XaubLb/event_summaries?limit=1', '', {
    'Authorization': 'Bearer b6283d5b52f9bc13ac965d5c8282ad60',
})
def bufferStatus():

    try:
        res = conn.getresponse()
        data = res.read()
        json_data = json.loads(data)
        events=(json_data['data'][0]['event'])
        events = events.split(",")
        
        for i in range(0,8):
            if (events[i].find("off") > 0):
                relay_status[i] = "off"
            else:
                relay_status[i] = "on"
    except:
        pass

def main(request):

    bufferStatus()

    


    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }

    return render(request, 'index.html', stuff_for_frontend)
    
def relay1(request):
    bufferStatus()
    if (relay[0] == 0):
        relay_status[0]="on"
        relay[0] = 1
    else:
        relay_status[0] = "off"
        relay[0] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)
    

def relay2(request):
    bufferStatus()
    if (relay[1] == 0):
        relay_status[1]="on"
        relay[1] = 1
    else:
        relay_status[1] = "off"
        relay[1] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })
    
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }

    return render(request, 'index.html', stuff_for_frontend)
    

def relay3(request):
    bufferStatus()
    if (relay[2] == 0):
        relay_status[2]="on"
        relay[2] = 1
    else:
        relay_status[2] = "off"
        relay[2] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }

    return render(request, 'index.html', stuff_for_frontend)
    

def relay4(request):
    bufferStatus()
    if (relay[3] == 0):
        relay_status[3]="on"
        relay[3] = 1
    else:
        relay_status[3] = "off"
        relay[3] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)
    

def relay5(request):
    bufferStatus()
    if (relay[4] == 0):
        relay_status[4]="on"
        relay[4] = 1
    else:
        relay_status[4] = "off"
        relay[4] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))



    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }

    return render(request, 'index.html', stuff_for_frontend)
    

def relay6(request):
    bufferStatus()
    if (relay[5] == 0):
        relay_status[5]="on"
        relay[5] = 1
    else:
        relay_status[5] = "off"
        relay[5] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))



    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)
    

def relay7(request):
    bufferStatus()
    if (relay[6] == 0):
        relay_status[6]="on"
        relay[6] = 1
    else:
        relay_status[6] = "off"
        relay[6] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }

    return render(request, 'index.html', stuff_for_frontend)
    

def relay8(request):
    bufferStatus()
    if (relay[7] == 0):
        relay_status[7]="on"
        relay[7] = 1
    else:
        relay_status[7] = "off"
        relay[7] = 0;
    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)

def all_on(request):
    bufferStatus()
    for i in range(0,8):
        relay_status[i]="on"
        relay[i] = 1

        

    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)
    
def all_off(request):
    bufferStatus()
    for i in range(0,8):
        relay_status[i]="off"
        relay[i] = 0

        

    
    conn = http.client.HTTPSConnection('e97f01afd43e278d075a8da01a05083a.m.pipedream.net')
    conn.request("POST", '/', '{"relay1":"'+relay_status[0]+'"},\
    {"relay2":"'+relay_status[1]+'"},\
    {"relay3":"'+relay_status[2]+'"},\
    {"relay4":"'+relay_status[3]+'"},\
    {"relay5":"'+relay_status[4]+'"},\
    {"relay6":"'+relay_status[5]+'"},\
    {"relay7":"'+relay_status[6]+'"},\
    {"relay8":"'+relay_status[7]+'"},\
    ', {
      'Content-Type': 'application/json',
    })

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))




    stuff_for_frontend = {
    'relay1': relay_status[0],
    'relay2': relay_status[1],
    'relay3': relay_status[2],
    'relay4': relay_status[3],
    'relay5': relay_status[4],
    'relay6': relay_status[5],
    'relay7': relay_status[6],
    'relay8': relay_status[7],
    }


    return render(request, 'index.html', stuff_for_frontend)
    
    


