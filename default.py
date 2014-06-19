import xbmc,xbmcgui                                                                                                                                                                      
import subprocess,os
import stomp
import xbmcaddon

#Initialize ADDON
settings = xbmcaddon.Addon(id='freedomotic.addon')

#Initialize ADDON INFORMATION
serial				=  settings.getSetting( "serial" )
api_key				=  settings.getSetting( "api_key" )
periph_id			=  settings.getSetting( "periph_id" )

#Initialize value for ref.
menu = 0
video = 0
audio = 0
stopmenu = 0

class FreedomService(object):
		def __init__(self):
				# create stomp connexion here
				
		def sendMessage(queue, message):
		
		def createStompMsg(type, value):
			
class MyPlayer(xbmc.Player):                                                                                                                                                             
                                                                                                                                                                                       
        def __init__ (self):                                                                                                                                                             
                xbmc.Player.__init__(self)				
				freedomoticSrv = new FreedomoticService()
				
                if (str(settings.getSetting("xbmc_started")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=1' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=1' % (serial, periph_id, api_key))
                                                                                                                                                                                        
        def onPlayBackStarted(self):

                xbmc.sleep(200) # it may take some time for xbmc to read tag info after playback started
                if xbmc.Player().isPlayingVideo():
                        currentvideo = xbmc.Player().getVideoInfoTag().getTitle()
                        currentvideo = currentvideo.replace(' ', '_')
                        if (str(settings.getSetting("video_started")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=2' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=2' % (serial, periph_id, api_key))
                                                
                if xbmc.Player().isPlayingAudio() == True:
                        currentsong = xbmc.Player().getMusicInfoTag().getTitle()
                        currentsong = currentsong.replace(' ', '_')
                        if (str(settings.getSetting("audio_started")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=3' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=3' % (serial, periph_id, api_key))
                                     
        def onPlayBackEnded(self):                                                                                                                                                       
                if (VIDEO == 1):                                                                                                                                                         
                        if (str(settings.getSetting("video_ended")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=4' % (serial, periph_id, api_key)) 
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=4' % (serial, periph_id, api_key)) 
                        
                if (AUDIO == 1):
                        if (str(settings.getSetting("audio_ended")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=5' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=5' % (serial, periph_id, api_key))
                                                                                                                                                                                         
        def onPlayBackStopped(self):                                                                                                                                                     
                if (VIDEO == 1):                                                                                                                                                         
                        if (str(settings.getSetting("video_stopped")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=6' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=6' % (serial, periph_id, api_key))
   
                if (AUDIO == 1):
                        if (str(settings.getSetting("audio_stopped")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=7' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=7' % (serial, periph_id, api_key))
                                                                                                                                                                                          
        def onPlayBackPaused(self):                                                                                                                                                      
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        if (str(settings.getSetting("video_paused")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=8' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=8' % (serial, periph_id, api_key))
        
                if xbmc.Player().isPlayingAudio():
                        if (str(settings.getSetting("audio_paused")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=9' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=9' % (serial, periph_id, api_key))
                        
        def onPlayBackResumed(self):     
		
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        if (str(settings.getSetting("video_resumed")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=10' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=10' % (serial, periph_id, api_key))

                if xbmc.Player().isPlayingAudio():
                        if (str(settings.getSetting("audio_resumed")) == "Yes"):
                                urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=11' % (serial, periph_id, api_key))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=11' % (serial, periph_id, api_key))
         
		def sendMessage():
				
			
player=MyPlayer()                                                                                                                                                                        
                                                                                                                                                                                         
VIDEO = 0

while(not xbmc.abortRequested):

        win   = (xbmcgui.getCurrentWindowId())

        if xbmc.Player().isPlaying():
                stopmenu = 1
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        VIDEO = 1
                        AUDIO = 0
                else:                                                                                                                                                                    
                        VIDEO = 0
                        AUDIO = 1

        #Return to menu after playing
        if not xbmc.Player().isPlaying() and stopmenu != 0:
                menu = 0
                stopmenu = 0
                
                                                                                                                                                               
       
        if win == 10000 and menu != 10000:
                menu = 10000
                if (str(settings.getSetting("menu_home")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=12' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=12' % (serial, periph_id, api_key))
                                
        if win == 10001 and menu != 10001:
                menu = 10001
                if (str(settings.getSetting("menu_program")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=13' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=13' % (serial, periph_id, api_key))
        
        
        if win == 10002 and menu != 10002:
                menu = 10002
                if (str(settings.getSetting("menu_picture")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=14' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=14' % (serial, periph_id, api_key))
        
        
        if win == 10004 and menu != 10004:
                menu = 10004
                if (str(settings.getSetting("menu_setting")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=15' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=15' % (serial, periph_id, api_key))
                                

       #navigate video menu 
        if win == 10006 and menu != 10006:
                menu = 10006
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))

                       
        if win == 10024 and menu != 10024:
                menu = 10024
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))

        if win == 10025 and menu != 10025:
                menu = 10025
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))

                       
        if win == 10028 and menu != 10028:
                menu = 10028
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=16' % (serial, periph_id, api_key))


        #navigate audio menu                 
        if win == 10005 and menu != 10005:
                menu = 10005
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))


        if win == 10500 and menu != 10500:
                menu = 10500
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))


        if win == 10501 and menu != 10501:
                menu = 10501
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))


        if win == 10502 and menu != 10502:
                menu = 10502
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=17' % (serial, periph_id, api_key))



        if win == 12600 and menu != 12600:
                menu = 12600
                if (str(settings.getSetting("menu_weather")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=18' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=18' % (serial, periph_id, api_key))

    
        xbmc.sleep(1000)
if (str(settings.getSetting("xbmc_ended")) == "Yes"):
                        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=0' % (serial, periph_id, api_key))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?serial=%s&ep=%s&apiKey=%s&value1=0' % (serial, periph_id, api_key))
