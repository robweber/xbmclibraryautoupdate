# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased](https://github.com/robweber/xbmclibraryautoupdate/compare/matrix-1.2.4...robweber:matrix)

### Changed

- updated in app and addon.xml translations
- moved code checking workflows from Travis CI to GitHub Actions ([Kodi Addon Checker](https://github.com/xbmc/action-kodi-addon-checker) and Flake8 Python check)

### Fixed

- use www.google.com for the network connectivity check - thanks @afontenot

## [Version 1.2.4](https://github.com/robweber/xbmclibraryautoupdate/compare/matrix-1.2.3...robweber:matrix-1.2.4)

### Changed

- multiple language files updated through integration with [Weblate](https://kodi.weblate.cloud/projects/kodi-add-ons-services/service-xbmclibraryautoupdate/), thanks to @gade01 for helping to get it working.

### Fixed

- fixed travis CI link in README

## [Version 1.2.3](https://github.com/robweber/xbmclibraryautoupdate/compare/matrix-1.2.2...robweber:matrix-1.2.3)

### Fixed

- issue with hourly timer settings, new settings don't return index but value itself thanks @benyjr

## [Version 1.2.2](https://github.com/robweber/xbmclibraryautoupdate/compare/matrix-1.2.1...matrix-1.2.2) - 2021-3-29

### Added

- added support for levels (Basic, Standard, Advanced, Expert) when viewing settings

### Changed

- updated ```settings.xml``` format to the Kodi standard.


### Fixed

- ```xbmc.translatePath``` moved to ```xbmcvfs.translatePath```
- issue with ```xbmcgui.Dialog()``` class, only takes 2 args now

## [Version 1.2.1](https://github.com/robweber/xbmclibraryautoupdate/compare/matrix-1.2.0...robweber:matrix-1.2.1) - 2020-6-22

### Added

- added kodi addon submitter to travis build process

### Fixed

- fixed error in ```xbmcgui.Dialog()``` call. The line2 argument has been deprecated
- fixed warning related to ```xbmc.translatePath()``` function call. This has been moved to ```xbmcvfs```.

## [Version 1.2.0](https://github.com/robweber/xbmclibraryautoupdate/compare/leia-1.1.1...robweber:matrix-1.2.0) - 2020-3-22

### Added

- added dynamic kodi version badge using the shields endpoint api

### Changed

- use the travis CI badge from the shields.io site instead of linking directly to badge on travis site (loads faster)
- moved service.py class to resources.lib/ folder as Kodi won't cache files in the root folder
- updated supported versions to Matrix or above

### Removed

- removed provides element from addon extension in addon.xml file - this is now identitied by kodi-addon-checker v0.0.15

## [Version 1.1.1](https://github.com/robweber/xbmclibraryautoupdate/compare/leia-1.1.0...robweber:leia-1.1.1) - 2019-10-09

### Added

- added badges for license, kodi version and pep8
- added [flake8](https://github.com/pycqa/flake8/) for linting in Travis CI file

### Changed

- import unquote from future, this would have thrown an error when hit at runtime on Python 3 and "check paths" was turned on

### Added

- Updated Changelog format to the one suggested by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Version 1.1.0](https://github.com/robweber/xbmclibraryautoupdate/compare/krypton-1.0.4...robweber:leia-1.1.0) - 2019-09-03

### Added
- addon is Python 2/3 compatible
- updated for Leia Python additions
- added dep for script.module.dateutil

### Changed
- fix custom paths (thanks madsession)
- use waitForAbort()

## [Version 1.0.5](https://github.com/robweber/xbmclibraryautoupdate/compare/32c63bd...robweber:a24445c)

### Changed
- fixed issue where custom paths for music could not launch

## [Version 1.0.4](https://github.com/robweber/xbmclibraryautoupdate/compare/v1.0.3...robweber:krypton-1.0.4)

### Added
 - make next run times more readable (I think)
### Changed
 - make sure manual run always works
 - use showdialogs on JSON commands based on Show Notifications option
 - fix clean after update error

## Version 1.0.3

### Added
- catch cron syntax errors and inform the user
- added option to check sources before scan

### Changed
- gracefully cancel out of custom dialog box
- replace builtin with json commands

## Version 1.0.2

### Changed
- Issue with language/country codes in language files

## Version 1.0.1

### Added
- moved to po files for strings

### Changed
- updated the way custom paths are handled

## Version 1.0.0

### Changed
- fixed issue in settings.xml and cleaning cron schedules - thanks ac_car

### Removed
- support for kodi versions below jarvis

## Version 0.9.9

### Added
- added custom paths via file - potentially unlimited

### Changed
- name change - finally removed XBMC

## Version 0.9.8

### Added
- added prompt disable setting for manual run
- added better error checking for last_run.txt file

## Version 0.9.7

### Changed
- Fixed issue with stacked timers not executing

## Version 0.9.6

- updated language files from Transifex
- stop guisound from playing - thanks invisiblek

## Version 0.9.5

- minor fix to update notification - thanks tknorris

## Version 0.9.4

- new setting - run when idle. thanks zer04c

## Version 0.9.3

- updated xbmc python version

## Version 0.9.2

- Version bump for merge of master changes

## Version 0.9.1

- updated for Gotham python changes

## Version 0.9.0

- New Version for Gotham

## Version 0.8.4

- Fix for a very odd timing bug causing multiple scans - thanks tknorris

## Version 0.8.3

- separated notifications and setting strings for translators - thanks NEOhidra

## Version 0.8.2

- added version info to logs

## Version 0.8.1

- added license tag

## Version 0.8.0

- clean up monitor on exit
- updated language files from Transifex

## Version 0.7.9

- updated language files from Transifex

## Version 0.7.8

- efficiencies to evalSchedules trigger - thanks Martijn

## Version 0.7.7

- updated language files from Transifex

## Version 0.7.6

- make sure cleaning is selected by the user

- check for playing media before cleaning library after db update

## Version 0.7.5

- Added network check before running a scan, if it fails it will try again in 10 seconds

## Version 0.7.4

- removed common plugin cache dependency - was causing CPU issues

- use xbmc.Monitor to check for settings updates

- use xbmc.Monitor to monitor db updates

- added custom cleaning timers, thanks Ghostdivision

- use settings.xml to store last_run data

## Version 0.7.3

- added support for multipathed sources in verify sources

- updated xbmc python version

## Version 0.7.2

- Fixed error with cleaning library

## Version 0.7.1

- Started using utils.py as common framework for logging/notifications

- fixed unicode error in showing notifications - thanks koying!

- added storage server (common plugin cache) as a dep

## Version 0.7.0

- increment version to keep Eden branch separate

## Version 0.6.5

- added setting to prompt user before doing scheduled clean. Defaults to False.

- added ability to schedule cleaning separate

- additional translations

## Version 0.6.4

- added strings from notifications and logging into the strings.xml files

- strings reorganization (affected translations)

- updated to french translation file

## Version 0.6.3

- added French translation file, thanks to foX aCe

## Version 0.6.2

- needed a catch in case the last_run.txt file is blank, or has non-integer data. thanks to mmounirou for catching this

## Version 0.6.1

- added 2 more custom library path options

## Version 0.6.0

- added "Cleaning" category to schedule a clean operation of the music/video databases. This operation can happen immediately after a scan or once per day/week/month. Verifying source paths before a clean is also supported

## Version 0.5.9

- added a custom video path option to only scan a specific video path instead of the entire library

## Version 0.5.8

- added a 1 minute delay timer before running a scan if XBMC has just exited playback. This should help in scenerios where ending media viewing results in an immediate scan that the user didn't want.

## Version 0.5.7

- merged 'standard' and 'advanced' usage to follow more of the same codebase. Now the standard timer uses a cron expression as well and will start at the top of every hour

## Version 0.5.6

-updated the manual run interface to include information about when the updater will run again

## Version 0.5.5

-changed cron expression library. Croniter will allow iterating through the cron expressions and show the next update time

-added methods to display a "countdown" when the next update will occur, and settings to display notifications

## Version 0.5.4

- fixed issue with startup timer, thanks stevenD

## Version 0.5.2

- fixed os import error

## Version 0.5.1

- merged changes from pkscuot's branch.
- rounds last_run to top of the minute (timer executes at 00 not anywhere in minute)
- creates addon data directory if it doesn't exist

## Version 0.5.0

- major changes to settings, split them by General and Timer category
- Advanced timer functions now add the ability to do cron-like scheduling of the update process, thanks to pkscuot for the timer ideas
- option to skip during media playback or run the update anyway

## Version 0.4.1

- added extra setting for a "startup delay" timer. This will only affect the addon when xbmc starts.
- the last running time is now set to a variable so that manual updates will reset the timer, and system resets will start the service where it left off

## Version 0.4.0

- Had a user suggestion to allow for a manual launch of the process as well as the service. Since the service point will ALWAYS launch on startup the manual option will kick off the library update process.

## Version 0.3.9

- running video and music scans side by side never really worked. Now checks if scan is running and waits until complete before running the next scan.

## Version 0.3.5

- now runs as a service instead of needing the autoexec.py file
- removed sample autoexec.py

## Version 0.3.1

- fixed a really stupid indent error
- added cancelalarm call in case run more than once
