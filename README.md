LXDE-VolumeControlOSD
=====================

Adds laptop media keys (volume +/-/mute) support and OSD for LXDE with pulseaudio and xfce4-notifyd (lubuntu 14.04 base setup). Tested on a ThinkPad X240.

##Installation
1. Install notify-send (libnotify-bin package in ubuntu/debian).

2. Move the `volumeControl.py` script to the user's `~/.config/openbox/` directory and modify the `*rc.xml` file within. Add to or update its `<keyboard>` section accordingly:

    ```xml
    <keyboard>
     ...
     <!-- Keybinding for Volume management -->
        <keybind key="XF86AudioRaiseVolume">
          <action name="Execute">
            <command>python3 ~/.config/openbox/volumeControl.py raise</command>
          </action>
        </keybind>
        <keybind key="XF86AudioLowerVolume">
          <action name="Execute">
            <command>python3 ~/.config/openbox/volumeControl.py lower</command>
          </action>
        </keybind>
        <keybind key="XF86AudioMute">
          <action name="Execute">
            <command>python3 ~/.config/openbox/volumeControl.py toggle-mute</command>
          </action>
        </keybind>
    ...
    </keyboard>
    ```

3. Then reload openbox by delogging/relogging or invoking `openbox --reconfigure` in a Terminal window.

##Notifications display
You might want to force the notifications to stack by adding the following snippet to the `<applications>` section of `*rc.xml`:

```xml
<!-- Force notifications position -->
<application class="*notifyd">
    <position force="yes">
        <x>center</x>
        <y>-50</y>
    </position>
</application>
```

###Customization
To customize the position of the OSD, change x and y values. Top (y) and left (x) borders of the screen are (+)0, right (x) and bottom (y) -0. E.g. A y value of -50 will make windows appear 50px away from the bottom of the screen.

##lubuntu/xfce4-power-manager OSD workaround:
xfce4-power-manager handles brightness +/- keys and its OSD which position cannot be forced by openbox `*rc.xml` configuration. If you want to disable this OSD (courtesy of [docs.xfce.org](http://docs.xfce.org/xfce/xfce4-power-manager/preferences)):
`xfconf-query -c xfce4-power-manager -n -p "/xfce4-power-manager/show-brightness-popup" -t bool -s false`