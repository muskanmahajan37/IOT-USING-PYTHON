#!/usr/bin/python
import Netmaxiot
import json
import sys
import time
import datetime

import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 24

GDOCS_OAUTH_JSON       = 'rohit.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'myiot'

FREQUENCY_SECONDS      = 5


def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet

    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)


print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')

###############################
worksheet = None

######################

while True:
    # Login if necessary.
    read1 = Netmaxiot.analogRead(0)
    read2 = Netmaxiot.analogRead(1)
    voltage1=read1*4.88
    voltage2=read2*4.88
    light = voltage1/5000
    light = light*100
    print "the value of light = %0.2f " %light
    print "--------"
    tempx=voltage2/10
    print "--------"
    print "--------"
    print "the value of temp analog = %0.2f " %tempx
    tempp=round(tempx,1)
    lightx=round(light,1)
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

    # Skip to the next reading if a valid measurement couldn't be taken.
    # This might happen if the CPU is under a lot of load and the sensor
    # can't be reliably read (timing is critical to read the sensor).
    if humidity is None or temp is None:
        time.sleep(2)
        continue

    print "the temp is %0.2f" %temp
    print "the humidity is %0.2f"%humidity


    try:
        worksheet.append_row((datetime.datetime.now().isoformat(), temp, humidity,tempp,lightx))
    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue

    # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)
