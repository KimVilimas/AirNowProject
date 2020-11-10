### Follow Tutorial > https://www.dataquest.io/blog/python-api-tutorial/ ###
#Import needed libraries
import requests #this library is the main one for making API requests :)

#To make a GET request, we’ll use the requests.get() function
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

#The GET will output a response object, and can use this .status_code to check it
print(response.status_code)
#You will see down there in terminal that it returns a 404 because doesn't exist! :)

#Use the NASA API from the tutorial, note: no authentication needed 
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
#Gives a 200 which means success!

#So we have
    #request.get('url')
    #response.status_code
#Now, lets learn the method
    #response.json() (and can print it out to show it)

#To see the data we received back from the API:
print(response.json())  #even left it as an empty argument
#this gives you the actual information in json you wanted from the url

#*** JSON (JavaScript Object Notation) is the language of APIs ***#
import json #this is a standard python library, no pip needed

#basically if you want this output to be easier to read, you gotta use this
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)    #json.dump function
    print(text)

jprint(response.json()) #pass the response from your url to your now nice jprint obj

#Okay so now what if you needed to enter parameters to your api? (like in in airq)
#We can make a dictionary with these parameters, and then pass to the requests.get
parameters = {
    "lat": 40.71,
    "lon": -74
}

#Lets make another request where we reference the params we just defined
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
jprint(response.json()) #pretty jprint formatting still in effect

#Now to learn about something called "Pass Times"
pass_times = response.json()['response']    #make a new variable here
jprint(pass_times)
#notice this outputs the same as above, but just the under part with
#all the 'duration' and 'risetime' stuff, not the top lil paragraph of info

#Next we’ll use a loop to extract just the five risetime values: (Confused?)
risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)
#this singles out and lists just the risetimes

#These times are weird because they are that weird internet time that starts in 1970
#We can use datetime.fromtimestamp() to convert these to easier times to understand
from datetime import datetime   #need a certain library for this one

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)