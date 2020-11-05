#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install plyer


# In[3]:


import time
import datetime  #For reading present date
import requests  #For retrieving coronavirus data from web
from plyer import notification  #For getting notification on your computer


# In[ ]:


covidData = None  # Initially assuming there is no data

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("Please! Check your internet connection")  # If there is network issue

# If we fetched the data

if covidData != None:
    data = covidData.json()['Success']  # Converting the data into json format

    while True:  # Repeating the loop for multiple times
        notification.notify(
            # giving the title of notification
            title=("Coronavirus Stats on {}".format(datetime.date.today())),
            # body of notification
            # the message which will be shown in the notification
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths : {todaydeaths}\nTotal "
                    "active : {active}".format(
                totalcases=data['cases'], todaycases=data['todayCases'], todaydeaths=data['todayDeaths'],
                active= data['active']),
            # Creating icon for notification
            app_icon="C:\\Users\\hp\\PycharmProjects\\Python Projects\\Desktop Notifier\\Paomedia-Small-N-Flat-Bell.ico",
            # Amount of time for which the notification will stay on the screen
            timeout=50
        )

        # Giving the sleep time for the notification, the notifiaction will repeat after the specific interval
        time.sleep(60 * 60 * 24)  # sleep for 24hrs


# # Running the Notifier in Background

# ## To make this Desktop Notifier run in background type the following command in your command prompt if you are using Windows

# *Note : Change the "file_name" with your file name*

# pythonw.exe .\file_name

# ### Welldone, now you will be receiving the notification in your given time interval

# *To check whether your application is running or not, you can open the task manager and check the ongoing tasks, you will notice that the Python program is ongoing there*
