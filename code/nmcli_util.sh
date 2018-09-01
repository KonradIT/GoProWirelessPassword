
if [ ! -z "$1" ] ;then
nmcli --fields NAME con show | \
  grep "$@" | \
    while read name ;do 
      echo Removing SSID "$name"
      nmcli con delete "$name"
    done
fi
