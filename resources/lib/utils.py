import xbmc
import xbmcaddon
    
__addon_id__= 'service.libraryautoupdate'
__Addon = xbmcaddon.Addon(__addon_id__)

def data_dir():
    return __Addon.getAddonInfo('profile')

def addon_dir():
    return __Addon.getAddonInfo('path')

def log(message,loglevel=xbmc.LOGNOTICE):
    xbmc.log(encode(__addon_id__ + ": " + message),level=loglevel)

def showNotification(title,message):
    xbmc.executebuiltin("Notification(" + encode(title) + "," + encode(message) + ",4000," + xbmc.translatePath(__Addon.getAddonInfo('path') + "/resources/images/clock.png") + ")")

def setSetting(name,value):
    __Addon.setSetting(name,value)

def getSetting(name):
    return __Addon.getSetting(name)
    
def getString(string_id):
    return __Addon.getLocalizedString(string_id)

def encode(string):
    return string.encode('UTF-8','replace')
