# Volume control notifications for lxde+pulseaudio+xfce4-notifyd (lubuntu)
# requires notify-send (libnotify-bin)
# 
# You might want to force the display of notifications by adding the following
# snippet to the <applications> portion of "~/.config/openbox/*rc.xml":
# <!-- Force notifications position -->
# <application class="*notifyd">
#     <position force="yes">
#         <x>center</x>
#         <y>-50</y>
#     </position>
# </application>
# 
# Thomas Maurin, 2014

import sys, re
from subprocess import getoutput, call


incr = 6 # increment step

def volumeIcon(volume=0, muted=False):
    "Return appropriate icon given the new volume level"
    if volume == 0 or muted:
        return '--icon=audio-volume-muted'
    elif volume < 33:
        return '--icon=audio-volume-low'
    elif volume < 67:
        return '--icon=audio-volume-medium'
    else:
        return '--icon=audio-volume-high'


# Get current volume
output = getoutput('amixer -D pulse get Master')
volume = int(re.search(r'\[(\d+)%\]', output).group(1))
muted = True if re.search(r'\[(\w+)\]$', output).group(1) == 'off' else False

command = sys.argv[1]
if command == 'toggle-mute':
    # Set volume
    call(['amixer', '-D', 'pulse', 'set', 'Master', '1+', 'toggle'])
    
    # Display notification
    if muted:
        call(['notify-send', "Volume:", "<b>"+str(volume)+"%</b>",
              volumeIcon(volume=volume)])
    else:
        call(['notify-send', "Volume:", "<b>Muet</b>",
              volumeIcon(muted=True)])

elif command == 'raise':

    if volume != 100:
        # Set volume
        call(['amixer', '-D', 'pulse', 'set', 'Master', str(incr)+'%+', 'unmute'])
    
    # Display notification
    # volume = getStatus()['volume']
    volume = min(volume+incr, 100)
    call(['notify-send', "Volume:", "<b>"+str(volume)+"%</b>",
              volumeIcon(volume=volume)])

elif command == 'lower':
    
    if volume != 0:
        # Set volume
        call(['amixer', '-D', 'pulse', 'set', 'Master', str(incr)+'%-', 'unmute'])
    
    # Display notification
    volume = max(volume-incr, 0)
    if volume == 0:
        call(['notify-send', "Volume:", "<b>Muet</b>",
              volumeIcon(muted=True)])        
    else:
        call(['notify-send', "Volume:", "<b>"+str(volume)+"%</b>",
              volumeIcon(volume=volume)])