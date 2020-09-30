# Seat Geek Ticket Price Checking Script

Straight forward script leveraging json libraries in python and Seat Geek API to achieve the following

1. Call Seat Geek API to retrieve full slate of information about event based on event ID
2. Slice the json to extract most relevant information (lowest base price, lowest price, median price, tickets available etc.)
3. Print the time at which the API call was made and a series of formatted print statements detailing the information around ticket prices for a given event
4. Write the timestamp and pricing info to a csv file for ML time series analysis to be carried out later on
5. Schedule the script to be run every hour using a cron job and configure to email the printed output with each run to update the user on when the best time to purchase a ticket is
