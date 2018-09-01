## Changes password via SD card.

echo "GoPro Password Changer"
echo -ne "Your current password: "; read current_pwd
echo $current_pwd > gpauto
echo -ne "New Password: "; read -s new_pwd
echo
echo -ne "New Password (again): "; read -s new_pwd_2
echo
if [[ $new_pwd == $new_pwd_2 ]]
	then
		echo -ne "New Wifi SSID: "; read new_wifissid
		echo EVssidprimary,$new_wifissid >> gpauto
		echo EVpassphrase,$new_pwd >> gpauto
fi
