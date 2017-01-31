import xbmcgui
import resources.lib.utils as utils
from resources.lib.cronclasses import CronSchedule, CustomPathFile
dialog = xbmcgui.Dialog()

#show the disclaimer - do this every time
dialog.ok(utils.getString(30031),"",utils.getString(30032),utils.getString(30033))

#show list of current paths
    #click to edit
    #add new

#select path to scan
#choose default or custom timer
#select time

#save

def selectPath():
    path = {'expression':'0 */2 * * *'}
    
    #select path to scan
    path['path'] = dialog.browse(0,'Browse for path','video')

    #create expression
    path['expression'] = dialog.input('Cron Expression',path['expression'])
    
    return path

def showMainScreen():
    exitCondition = ""
    customPaths = CustomPathFile()
    
    while(exitCondition != -1):
        #load the custom paths
        options = ['Add']
        
        for aPath in customPaths.getPaths():
            options.append(aPath['path'] + ' - ' + aPath['expression'])
            
        #show the gui
        exitCondition = dialog.select("Edit Custom Paths",options)
        
        if(exitCondition >= 0):
            if(exitCondition == 0):
                path = selectPath()

                customPaths.addPath(path)
            else:
                #delete?
                if(dialog.yesno(heading="Choose Action",line1="Delete this item?")):
                    #delete this path - subtract one because of "add" item
                    customPaths.deletePath(exitCondition -1)
            


showMainScreen()    
