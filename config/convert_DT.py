#!/usr/bin/env python3

# I found this here ---> https://stackoverflow.com/a/4771733
from datetime import datetime
from dateutil import tz
import re

def con_DT(x):

    xDT = re.sub(r"\..*$", "", x) # Used to remove micro second

    # METHOD 1: Hardcode zones:
    # from_zone = tz.gettz('UTC')
    # to_zone = tz.gettz('America/Chicago')

    # METHOD 2: Auto-detect zones:
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    # utc = datetime.utcnow()
    
    utc = datetime.strptime(xDT, '%Y-%m-%dT%H:%M:%S')

    # Tell the datetime object that it's in UTC time zone since 
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)

    # Convert time zone
    corrected_DT = utc.astimezone(to_zone)

    return (str(corrected_DT))