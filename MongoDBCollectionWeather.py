#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests # add to requirements.txt
import pymongo # add to requirements.txt
import datetime 
import csv


# In[2]:


# trying out the Weather API!
url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"X-RapidAPI-Key": "439c18c987msh14797ced597464ap1a2b93jsncfca5dab2679",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# Extract relevant weather data from API response
weather_data = response.json()["current"]
temperature_celsius = weather_data["temp_c"]
condition_text = weather_data["condition"]["text"]


# In[3]:


'''
# see if it's working correctly
print(condition_text,temperature_celsius)
'''


# In[4]:


# Connect to MongoDB

# Open the CSV file
with open('Top100-US.csv', 'r') as file:
    # Parse the CSV file
    reader = csv.DictReader(file, delimiter=';')

    try:
        #create a credentials.txt file in this folder:
        #user  (not account username)
        #pass 
        #third line: Databse url with port (you can find it in the cloud dashboard)
        #fourth lin: Database name
        if 'conn' in globals():
            conn.close()
            print("Closing")

        with open("credentials.txt", 'r') as f:
            [name,password,url,dbname]=f.read().splitlines()
        conn=pymongo.MongoClient("mongodb+srv://{}:{}@{}".format(name,password,url))
        print ("Connected successfully!!!")

    except pymongo.errors.ConnectionFailure as e:
        print ("Could not connect to MongoDB: %s" % e) 
    conn
    db = conn[dbname]
    collection = db['city_weather']
    
    # Loop through each row in the CSV and add a new document to the MongoDB collection
    for row in reader:
        # Get the weather for the city
        city_name = row['City']
        response = requests.request("GET", "https://weatherapi-com.p.rapidapi.com/current.json", headers=headers, params=querystring)
        weather = response.json()["current"]
        print(city_name,weather_data)
        
        # Create the document
        document = {
            'zip': row['Zip'],
            'city': city_name,
            'created_at': datetime.datetime.now(),
            'weather': weather

        }

        # Insert the document into the collection
        collection.insert_one(document)


# In[8]:


'''
# checking if the info was uploaded correctly
documents = collection.find()
for doc in documents:
    print(doc)
'''


# This code reads the CSV file, iterates through each row, and adds a new document to the MongoDB collection for each row in the CSV file. Therefore, running the code 10 times with the same CSV file would create 1000 entries in the MongoDB collection.

# In[10]:


if db.list_collection_names() is not None:
     print('Weather information collected',db.city_weather.count_documents({}))

