lxde-volumeControlOSD
=====================

Volume control + notifications for lxde+pulseaudio+xfce4-notifyd (lubuntu)


lubuntu/xfce4-power-manager workaround:
xfce4-power-manager handles brightness up/down keys and its respective OSD which position cannot be forced by openbox configuration. If you want to disable this OSD (courtesy of http://docs.xfce.org/xfce/xfce4-power-manager/preferences):
xfconf-query -c xfce4-power-manager -n -p "/xfce4-power-manager/show-brightness-popup" -t bool -s false