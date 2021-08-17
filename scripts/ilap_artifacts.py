# To add a new artifact module, import it here as shown below:
#     from scripts.artifacts.fruitninja import get_fruitninja
# Also add the grep search for that module using the same name
# to the 'tosearch' data structure.

import traceback

from scripts.artifacts.accounts_ce import get_accounts_ce
from scripts.artifacts.accounts_ce_authtokens import get_accounts_ce_authtokens
from scripts.artifacts.accounts_de import get_accounts_de
from scripts.artifacts.adb_hosts import get_adb_hosts
from scripts.artifacts.appicons import get_appicons
from scripts.artifacts.appops import get_appops
from scripts.artifacts.appopSetupWiz import get_appopSetupWiz 
from scripts.artifacts.BashHistory import get_BashHistory
from scripts.artifacts.bluetoothConnections import get_bluetoothConnections
from scripts.artifacts.browserlocation import get_browserlocation
from scripts.artifacts.build import get_build
from scripts.artifacts.cachelocation import get_cachelocation
from scripts.artifacts.calllog import get_calllog
from scripts.artifacts.calllogs import get_calllogs
from scripts.artifacts.Cast import get_Cast
from scripts.artifacts.Cello import get_Cello
from scripts.artifacts.ChessWithFriends import get_ChessWithFriends
from scripts.artifacts.chrome import get_chrome
from scripts.artifacts.chromeAutofill import get_chromeAutofill
from scripts.artifacts.chromeBookmarks import get_chromeBookmarks
from scripts.artifacts.chromeCookies import get_chromeCookies
from scripts.artifacts.chromeDownloads import get_chromeDownloads
from scripts.artifacts.chromeLoginData import get_chromeLoginData
from scripts.artifacts.chromeMediaHistory import get_chromeMediaHistory
from scripts.artifacts.chromeNetworkActionPredictor import get_chromeNetworkActionPredictor
from scripts.artifacts.chromeOfflinePages import get_chromeOfflinePages
from scripts.artifacts.chromeSearchTerms import get_chromeSearchTerms
from scripts.artifacts.chromeTopSites import get_chromeTopSites
from scripts.artifacts.chromeWebsearch import get_chromeWebsearch
from scripts.artifacts.cmh import get_cmh
from scripts.artifacts.contacts import get_contacts
from scripts.artifacts.DocList import get_DocList
from scripts.artifacts.emulatedSmeta import get_emulatedSmeta
from scripts.artifacts.errp import get_errp
from scripts.artifacts.etc_hosts import get_etc_hosts
from scripts.artifacts.FacebookMessenger import get_FacebookMessenger
from scripts.artifacts.fitbitExercise import get_fitbitExercise
from scripts.artifacts.fitbitSleep import get_fitbitSleep
from scripts.artifacts.fitbitSocial import get_fitbitSocial
from scripts.artifacts.fitbitWalk import get_fitbitWalk
from scripts.artifacts.fitbitHeart import get_fitbitHeart
from scripts.artifacts.fitbitActivity import get_fitbitActivity
from scripts.artifacts.gboard import get_gboardCache
from scripts.artifacts.googleCallScreen import get_googleCallScreen
from scripts.artifacts.googleDuo import get_googleDuo
from scripts.artifacts.googleKeepNotes import get_googleKeepNotes
from scripts.artifacts.googlePhotos import get_googlePhotos
from scripts.artifacts.googlemaplocation import get_googlemaplocation
from scripts.artifacts.googleNowPlaying import get_googleNowPlaying
from scripts.artifacts.googlePlaySearches import get_googlePlaySearches
from scripts.artifacts.googleQuickSearchbox import get_quicksearch
from scripts.artifacts.googleQuickSearchboxRecent import get_quicksearch_recent
from scripts.artifacts.imo import get_imo
from scripts.artifacts.installedappsGass import get_installedappsGass
from scripts.artifacts.installedappsLibrary import get_installedappsLibrary
from scripts.artifacts.installedappsVending import get_installedappsVending 
from scripts.artifacts.kikReturns import get_kikReturns
from scripts.artifacts.pSettings import get_pSettings
from scripts.artifacts.packageGplinks import get_packageGplinks
from scripts.artifacts.packageInfo import get_package_info
from scripts.artifacts.permissions import get_permissions
from scripts.artifacts.recentactivity import get_recentactivity
from scripts.artifacts.lgRCS import get_lgRCS
from scripts.artifacts.line import get_line
from scripts.artifacts.Oruxmaps import get_Oruxmaps
from scripts.artifacts.roles import get_roles
from scripts.artifacts.runtimePerms import get_runtimePerms
from scripts.artifacts.scontextLog import get_scontextLog
from scripts.artifacts.setupWizardinfo import get_setupWizardinfo
from scripts.artifacts.setupWizardinfo import get_setupWizardinfo
from scripts.artifacts.shareit import get_shareit
from scripts.artifacts.siminfo import get_siminfo
from scripts.artifacts.skout import get_skout
from scripts.artifacts.skype import get_skype
from scripts.artifacts.smanagerCrash import get_smanagerCrash
from scripts.artifacts.smanagerLow import get_smanagerLow
from scripts.artifacts.smembersAppInv import get_smembersAppInv
from scripts.artifacts.smembersEvents import get_smembersEvents
from scripts.artifacts.smsmms import get_sms_mms
from scripts.artifacts.smyfilesRecents import get_smyfilesRecents
from scripts.artifacts.smyFiles import get_smyFiles
from scripts.artifacts.smyfilesStored import get_smyfilesStored
from scripts.artifacts.suggestions import get_suggestions
from scripts.artifacts.swellbeing import get_swellbeing
from scripts.artifacts.sWipehist import get_sWipehist
from scripts.artifacts.sRecoveryhist import get_sRecoveryhist
from scripts.artifacts.tangomessage import get_tangomessage
from scripts.artifacts.teams import get_teams
from scripts.artifacts.textnow import get_textnow
from scripts.artifacts.tikTok import get_tikTok
from scripts.artifacts.Turbo_Battery import get_Turbo_Battery
from scripts.artifacts.Turbo_AppUsage import get_Turbo_AppUsage
from scripts.artifacts.usageapps import get_usageapps
from scripts.artifacts.usagestats import get_usagestats
from scripts.artifacts.usagestatsVersion import get_usagestatsVersion
from scripts.artifacts.userDict import get_userDict
from scripts.artifacts.Viber import get_Viber
from scripts.artifacts.vlcMedia import get_vlcMedia
from scripts.artifacts.vlcThumbs import get_vlcThumbs
from scripts.artifacts.walStrings import get_walStrings
from scripts.artifacts.wellbeing import get_wellbeing
from scripts.artifacts.wellbeingURLs import get_wellbeingURLs
from scripts.artifacts.wellbeingaccount import get_wellbeingaccount
from scripts.artifacts.Whatsapp import get_Whatsapp
from scripts.artifacts.wifiHotspot import get_wifiHotspot
from scripts.artifacts.wifiProfiles import get_wifiProfiles
from scripts.artifacts.WordsWithFriends import get_WordsWithFriends
from scripts.artifacts.Xender import get_Xender
from scripts.artifacts.Zapya import get_Zapya

from scripts.ilapfuncs import *

# GREP searches for each module
# Format is Key='modulename', Value=Tuple('Module Pretty Name', 'regex_term')
#   regex_term can be a string or a list/tuple of strings
# Here modulename must match the get_xxxxxx function name for that module. 
# For example: If modulename='profit', function name must be get_profit(..)
# Don't forget to import the module above!!!!

tosearch = {
    'usagestatsVersion':('Usage Stats', ('*/system/usagestats/*/version', '*/system_ce/*/usagestats/version')),
    'kikReturns':('Kik Returns', ('*/logs/*.txt','*/content/*')),
}
'''
tosearch = {
    'build':('Device Info', '*/vendor/build.prop'),
    'accounts_ce': ('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'accounts_ce_authtokens':('Accounts_ce', '*/data/system_ce/*/accounts_ce.db'),
    'accounts_de': ('Accounts_de', '*/data/system_de/*/accounts_de.db'),
    'adb_hosts':('ADB Hosts', '*/data/misc/adb/adb_keys'),
    'appicons':('Installed Apps', '*/data/com.google.android.apps.nexuslauncher/databases/app_icons.db*'),
    'appops': ('Permissions', '*/data/system/appops.xml'),
    'appopSetupWiz': ('Wipe & Setup', '*/data/system/appops.xml'),
    'bluetoothConnections':('Bluetooth Connections', '*/data/misc/bluedroid/bt_config.conf'),
    'BashHistory':('Bash History', '**/.bash_history'),
    'browserlocation': ('GEO Location', ('**/com.android.browser/app_geolocation/CachedGeoposition.db')),
    'cachelocation': ('GEO Location', ('**/com.google.android.location/files/cache.cell/cache.cell', '**/com.google.android.location/files/cache.wifi/cache.wifi')),
    'calllog': ('Call Logs', '*/data/com.android.providers.contacts/databases/calllog.db'),
    'calllogs':('Call Logs', ('**/com.android.providers.contacts/databases/contact*', '**/com.sec.android.provider.logsprovider/databases/logs.db*')),
    'Cast':('Cast', '*/com.google.android.gms/databases/cast.db'),
    'Cello': ('Google Drive', ('*/com.google.android.apps.docs/app_cello/*/cello.db*', '*/com.google.android.apps.docs/files/shiny_blobs/blobs/*')),
    'ChessWithFriends':('Chats', ('*/data/data/com.zynga.chess.googleplay/databases/wf_database.sqlite', '*/data/data/com.zynga.chess.googleplay/db/wf_database.sqlite')),
    'chrome':('Chromium', ('*/data/data/*/app_chrome/Default/History*', '*/data/data/*/app_sbrowser/Default/History*', '*/data/data/*/app_opera/History*')),
    'chromeAutofill':('Chromium', ('*/data/data/*/app_chrome/Default/Web Data*', '*/data/data/*/app_sbrowser/Default/Web Data*', '*/data/data/*/app_opera/Web Data*')),
    'chromeBookmarks':('Chromium', ('*/data/data/*/app_chrome/Default/Bookmarks*', '*/data/data/*/app_sbrowser/Default/Bookmarks*', '*/data/data/*/app_opera/Bookmarks*')),
    'chromeCookies':('Chromium', ('*/data/data/*/app_chrome/Default/Cookies*', '*/data/data/*/app_sbrowser/Default/Cookies*', '*/data/data/*/app_opera/Cookies*')),
    'chromeDownloads':('Chromium', ('*/data/data/*/app_chrome/Default/History*', '*/data/data/*/app_sbrowser/Default/History*', '*/data/data/*/app_opera/History*')),
    'chromeLoginData':('Chromium', ('*/data/data/*/app_chrome/Default/Login Data*', '*/data/data/*/app_sbrowser/Default/Login Data*', '*/data/data/*/app_opera/Login Data*')),
    'chromeMediaHistory':('Chromium', ('*/data/data/*/app_chrome/Default/Media History*','*/data/data/*/app_sbrowser/Default/Media History*', '*/data/data/*/app_opera/Media History*')),
    'chromeNetworkActionPredictor':('Chromium', ('*/data/data/*/app_Chrome/Default/Network Action Predictor*','*/data/data/*/app_sbrowser/Default/Network Action Predictor*', '*/data/data/*/app_opera/Network Action Predicator*')),
    'chromeOfflinePages':('Chromium', ('*/data/data/*/app_chrome/Default/Offline Pages/metadata/OfflinePages.db*', '*/data/data/*/app_sbrowser/Default/Offline Pages/metadata/OfflinePages.db*')),
    'chromeSearchTerms':('Chromium', ('*/data/data/*/app_chrome/Default/History*', '*/data/data/*/app_sbrowser/Default/History*', '*/data/*/app_opera/History*')),
    'chromeTopSites':('Chromium', ('*/data/data/*/app_chrome/Default/Top Sites*', '*/data/data/*/app_sbrowser/Default/Top Sites*', '*/data/*/app_opera/Top Sites*')),
    'chromeWebsearch':('Chromium', ('*/data/data/*/app_chrome/Default/History*', '*/data/data/*/app_sbrowser/Default/History*', '*/data/data/*/app_opera/History*')),
    'cmh':('Samsung_CMH', '**/cmh.db'),
    'contacts':('Contacts', ('**/com.android.providers.contacts/databases/contact*', '**/com.sec.android.provider.logsprovider/databases/logs.db*')),
    'DocList':('Google Drive', '*/data/data/com.google.android.apps.docs/databases/DocList.db*'),
    'emulatedSmeta':('Emulated Storage Metadata', '*/data/data/com.google.android.providers.media.module/databases/external.db*'),
    'errp':('Wipe & Setup', '*/data/system/users/service/eRR.p'),
    'etc_hosts':('Etc Hosts', '*/system/etc/hosts'),
    'FacebookMessenger':('Facebook Messenger', '**/threads_db2*'),
    'fitbitExercise':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/exercise_db*'),
    'fitbitSleep':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/sleep*'),
    'fitbitSocial':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/social_db*'),
    'fitbitWalk':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/mobile_track_db*'),
    'fitbitHeart':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/heart_rate_db*'),
    'fitbitActivity':('Fitbit', '*/data/data/com.fitbit.FitbitMobile/databases/activity_db*'),
    'gboardCache':('Gboard Keyboard', '**/com.google.android.inputmethod.latin/databases/trainingcache*.db'),
    'googleCallScreen':('Google Call Screen', ('**/com.google.android.dialer/databases/callscreen_transcripts*','**/com.google.android.dialer/files/callscreenrecordings/*.*')),
    'googleDuo':('Google Duo', ('**/com.google.android.apps.tachyon/databases/tachyon.db*','**/com.google.android.apps.tachyon/files/media/*.*')),
    'googleKeepNotes':('Google Keep', "**/data/com.google.android.keep/databases/keep.db"),
    'googlemaplocation': ('GEO Location', ('**/com.google.android.apps.maps/databases/da_destination_history*')),
    'googleNowPlaying':('Now Playing', ('*/data/data/com.google.intelligence.sense/db/history_db*','*/data/data/com.google.android.as/databases/history_db*')),
    'googlePhotos':('Google Photos', ('*/data/data/com.google.android.apps.photos/databases/gphotos0.db*','*/data/data/com.google.android.apps.photos/databases/disk_cache*','*/data/data/com.google.android.apps.photos/cache/glide_cache/*','*/data/data/com.google.android.apps.photos/databases/local_trash.db*','*/data/data/com.google.android.apps.photos/files/trash_files/*')),
    'googlePlaySearches':('Google Play', '*/data/data/com.android.vending/databases/suggestions.db*'),
    'imo':('IMO', ('**/com.imo.android.imous/databases/*.db*')),
    'installedappsGass':('Installed Apps', ('*/data/data/com.google.android.gms/databases/gass.db*', '*/data/user/*/com.google.android.gms/databases/gass.db*' )),
    'installedappsLibrary': ('Installed Apps', '*/data/data/com.android.vending/databases/library.db'),
    'installedappsVending': ('Installed Apps', '*/data/data/com.android.vending/databases/localappstate.db'),
    'line': ('Line', '**/jp.naver.line.android/databases/**'),
    'pSettings':('Device Info', '*/data/data/com.google.android.gsf/databases/googlesettings.db*'),
    'package_info': ('Installed Apps', '*/system/packages.xml'),
    'packageGplinks': ('Installed Apps', '*/system/packages.list'),
    'quicksearch':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/app_session/*.binarypb'),
    'quicksearch_recent':('Google Now & QuickSearch', '*/com.google.android.googlequicksearchbox/files/recently/*'),
    'recentactivity':('Recent Activity', '*/data/system_ce/*'),
    'lgRCS':('RCS Chats', '*/mmssms.db*'),
    'Oruxmaps':('GEO Location', '**/oruxmaps/tracklogs/oruxmapstracks.db*'),
    'permissions':('Permissions', '*/system/packages.xml'),
    'roles':('App Roles',('*/system/users/*/roles.xml','*/misc_de/*/apexdata/com.android.permission/roles.xml')),
    'runtimePerms':('Permissions',('*/system/users/*/runtime-permissions.xml','*/misc_de/*/apexdata/com.android.permission/runtime-permissions.xml')),
    'scontextLog':('App Interaction', '*/com.samsung.android.providers.context/databases/ContextLog.db'),
    'settingsSecure':('Device Info', '*/system/users/*/settings_secure.xml'),
    'setupWizardinfo': ('Wipe & Setup', '*/data/com.google.android.settings.intelligence/shared_prefs/setup_wizard_info.xml'),
    'shareit':('File Transfer', '*/com.lenovo.anyshare.gps/databases/history.db*'),
    'siminfo':('Device Info', '*/user_de/*/com.android.providers.telephony/databases/telephony.db'),
    'skout':('Skout', '*/data/com.skout.android/databases/skoutDatabase*'),
    'skype': ('Skype', '**/com.skype.raider/databases/live*'),
    'smanagerCrash':('App Interaction', '*/com.samsung.android.sm/databases/sm.db'),
    'smanagerLow':('App Interaction', '*/com.samsung.android.sm/databases/lowpowercontext-system-db'),
    'smembersAppInv':('App Interaction', '*/com.samsung.oh/databases/com_pocketgeek_sdk_app_inventory.db'),
    'smembersEvents':('App Interaction', '*/com.samsung.oh/databases/com_pocketgeek_sdk.db'),
    'sms_mms':('SMS & MMS', '*/com.android.providers.telephony/databases/mmssms*'), # Get mmssms.db, mms-wal.db
    'smyfilesRecents':('Media Metadata', '*/com.sec.android.app.myfiles/databases/myfiles.db'),
    'smyFiles':('Media Metadata', '**/com.sec.android.app.myfiles/databases/MyFiles*.db*'),
    'smyfilesStored':('Media Metadata', '**/com.sec.android.app.myfiles/databases/FileCache.db'),
    'suggestions': ('Wipe & Setup', '*/data/com.google.android.settings.intelligence/shared_prefs/suggestions.xml'),
    'swellbeing': ('Wellbeing', '**/com.samsung.android.forest/databases/dwbCommon.db*'),
    'sWipehist': ('Wipe & Setup', '*/efs/recovery/history'),
    'sRecoveryhist': ('Wipe & Setup', '*/efs/recovery/history'),
    'tangomessage':('Tango', '**/com.sgiggle.production/files/tc.db*'),
    'teams':('Teams', '*/com.microsoft.teams/databases/SkypeTeams.db*'),
    'textnow': ('Text Now', '**/com.enflick.android.TextNow/databases/textnow_data.db*'),
    'tikTok': ('TikTok', ('*_im.db*', '*db_im_xx*')),
    'Turbo_Battery': ('Device Health Services', ('*/com.google.android.apps.turbo/databases/turbo.db*','*/com.google.android.apps.turbo/databases/bluetooth.db*',)),
    'Turbo_AppUsage': ('Device Health Services', '*/com.google.android.apps.turbo/shared_prefs/app_usage_stats.xml'),
    'usageapps': ('App Interaction', '**/com.google.android.as/databases/reflection_gel_events.db*'),
    'usagestats':('Usage Stats', ('*/system/usagestats/*', '**/system_ce/*/usagestats*')), # fs: matches only 1st level folders under usagestats/, tar/zip matches every single file recursively under usagestats/
    'usagestatsVersion':('Usage Stats', ('*/system/usagestats/*/version', '*/system_ce/*/usagestats/version')),
    'userDict':('User Dictionary', '**/com.android.providers.userdictionary/databases/user_dict.db*'),
    'Viber':('Viber', '**/com.viber.voip/databases/*'),
    'vlcMedia': ('VLC', '*vlc_media.db*'),
    'vlcThumbs': ('VLC', '*/org.videolan.vlc/files/medialib/*.jpg'),
    'walStrings':('SQLite Journaling', ('**/*-wal', '**/*-journal')),
    'wellbeing': ('Wellbeing', '**/com.google.android.apps.wellbeing/databases/app_usage*'),
    'wellbeingURLs': ('Wellbeing', '**/com.google.android.apps.wellbeing/databases/app_usage*'), # Get app_usage & app_usage-wal
    'wellbeingaccount': ('Wellbeing', '**/com.google.android.apps.wellbeing/files/AccountData.pb'),
    'Whatsapp':('Whatsapp', ('*/com.whatsapp/databases/*.db*','**/com.whatsapp/shared_prefs/com.whatsapp_preferences_light.xml')),
    'wifiHotspot':('WiFi Profiles', ('**/misc/wifi/softap.conf', '**/misc**/apexdata/com.android.wifi/WifiConfigStoreSoftAp.xml')),
    'wifiProfiles':('WiFi Profiles', ('**/misc/wifi/WifiConfigStore.xml', '**/misc**/apexdata/com.android.wifi/WifiConfigStore.xml')),
    'WordsWithFriends':('Chats', '**/com.zynga.words/db/wf_database.sqlite'),
    'Xender':('File Transfer', '**/cn.xender/databases/trans-history-db*'), # Get trans-history-db and trans-history-db-wal
    'Zapya':('File Transfer', '**/com.dewmobile.kuaiya.play/databases/transfer20.db*')
    }
'''
slash = '\\' if is_platform_windows() else '/'

def process_artifact(files_found, artifact_func, artifact_name, seeker, report_folder_base, wrap_text):
    ''' Perform the common setup for each artifact, ie, 
        1. Create the report folder for it
        2. Fetch the method (function) and call it
        3. Wrap processing function in a try..except block

        Args:
            files_found: list of files that matched regex

            artifact_func: method to call

            artifact_name: Pretty name of artifact

            seeker: FileSeeker object to pass to method
            
            wrap_text: whether the text data will be wrapped or not using textwrap.  Useful for tools that want to parse the data.
    '''
    logfunc('{} [{}] artifact executing'.format(artifact_name, artifact_func))
    report_folder = os.path.join(report_folder_base, artifact_name) + slash
    try:
        if os.path.isdir(report_folder):
            pass
        else:
            os.makedirs(report_folder)
    except Exception as ex:
        logfunc('Error creating {} report directory at path {}'.format(artifact_name, report_folder))
        logfunc('Reading {} artifact failed!'.format(artifact_name))
        logfunc('Error was {}'.format(str(ex)))
        return
    try:
        method = globals()['get_' + artifact_func]
        method(files_found, report_folder, seeker, wrap_text)
    except Exception as ex:
        logfunc('Reading {} artifact had errors!'.format(artifact_name))
        logfunc('Error was {}'.format(str(ex)))
        logfunc('Exception Traceback: {}'.format(traceback.format_exc()))
        return

    logfunc('{} [{}] artifact completed'.format(artifact_name, artifact_func))
    