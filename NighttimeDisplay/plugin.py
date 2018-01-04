from enigma import eDBoxLCD
from Plugins.Plugin import PluginDescriptor
from Components.config import config
import datetime
import threading

CHECK_INTERVAL_SECONDS = 60.0

FROM_HOUR   = 0
FROM_MINUTE = 20

TO_HOUR     = 0
TO_MINUTE   = 1

OFF_BRIGHTNESS = 0
ON_BRIGHTNESS  = 70

def isNightTime():
    now = datetime.datetime.now()
    return now.hour >= FROM_HOUR and now.minute >= FROM_MINUTE and 
           now.hour < TO_HOUR and now.minute < TO_MINUTE

def isInStandby():
    from Screens.Standby import inStandby
    return inStandby is not None

def tick():
    frontpanel = eDBoxLCD.getInstance()

    if isNightTime() and isInStandby():
        frontpanel.setLCDBrightness(OFF_BRIGHTNESS)
    else:
        frontpanel.setLCDBrightness(ON_BRIGHTNESS)

    threading.Timer(CHECK_INTERVAL_SECONDS, tick).start()

def main(session, **kwargs):
    tick()

def Plugins(**kwargs):
    return PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, fnc = main)
