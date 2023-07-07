#Carlos Mendoza - CSCI 4452 Assignment 3 - End-to-end Weather Application with AWS

#Flask ensures that the app can be accessed through a web browser
from flask import Flask, render_template, request

#pymysql is how the app is able to connect and send data to the RDS aspect of my project
#from pymysql import connections

#boto3 is how the app is able to connect and send data to the S3 aspect of my project
#import boto3

#Info such as the username, password, and endpoint of my database are stored in a separate file naed config
#from config import *
  
#JSON allows for data to be retrieved from the openweathermap api link
import json
  
#Urllib also allows for data to be retrieved from the openweathermap api link by requesting for access from the link
import urllib.request

#Requests is used to download the image so that it may be placed in the S3 bucket
#import requests

#Start the web app
application = Flask(__name__)

#Info for the s3 bucket
bucket = 'a3weatherdata'
region = 'us-east-1'

#Connecting to the database, info for the database is in config.py
#db_conn = connections.Connection(
#    host=customhost,
#    port=3306,
#    user=customuser,
#    password=custompass,
#    db=customdb

#)

#There is only one page for this web app
@application.route('/', methods =['POST', 'GET'])
def weather():
    #The search is based on what city you type
    #NOTE: Only cities with one word can be searched for. However, this can be compromised by putting a "+" instead of a space between the the terms of a two-word city (e.g. "new+york")
    if request.method == 'POST':
        city = request.form['city']
    else:
        #Does marrero by default
        city = 'marrero'  
  
    #my OpenWeatherMap API
    api = '6006e5592d9338def87027bebee8ffb8'
  
    #API json data comes from this variable
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()
  
    #Converting JSON data to a dictionary
    list_of_data = json.loads(source)
    
    #The image is collected based on its url
    weatherimgid = list_of_data['weather'][0]['icon']
    weatherimgurl = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=weatherimgid)

    country_code = str(list_of_data['sys']['country'])
    coordinates = str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat'])
    #The temperature is orginally in Kelvin and as such is converted to Farenheit
    temperature = str(round((list_of_data['main']['temp']-273.15)*(9/5)+32))

    #Begin the RDS process
    #cursor = db_conn.cursor()

    #Attempting to get the entire database as a list to print in the html file under previous searches, unfortunately does not work
    #weathers = cursor.execute("SELECT * FROM a3weather")
    #db_conn.commit()

    #Preparing the query that inserts the current search result's data into the database
    #insertsql = "INSERT INTO a3weather VALUES (%s, %s, %s, %s)"

    #Data used for the index.html file
    data = {
        "countrycode": country_code,
        "coordinate": coordinates,
        "temp": temperature,
        #City is capitalized in case if the user doesn't when searching
        "cityname": city.capitalize(),
        "imgurl": weatherimgurl
    }
    print(data)

   
    #try:
        #Perform the insert query
        #cursor.execute(insertsql, (country_code, city.capitalize(), temperature, coordinates))
        #db_conn.commit()

        #Get the data for the image 
        #Not the file itself, though
        #imgdata = requests.get(weatherimgurl).content
                
        #Begin the s3 bucket process
        #Ensures that the image is saved in the s3 bucket as a png file and not any other file type
        #imagenameins3 = "weather" + str(city) + "_image_file.png"
        #s3 = boto3.resource('s3')

        #try:
            #print("Uploading image to s3...")
            #s3.Bucket(bucket).put_object(Key=imagenameins3, Body=imgdata)
            #bucketlocation = boto3.client('s3').get_bucket_location(Bucket=bucket)
            #s3location = (bucketlocation['LocationConstraint'])

            #if s3location is None:
                #s3location = ''
            #else:
                #s3location = '-' + s3location

        #except Exception as e:
            #return str(e)

    #finally:
        #cursor.close()
        
    #End of s3 and RDS process
    return render_template('index.html', data = data)
        
  
  

if __name__ == '__main__':
    application.run()
