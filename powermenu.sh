#! /bin/sh

chosen=$(printf "⏻  Power Off\n♻️ Restart\n🔒 Lock\n💤 Suspend" | rofi -dmenu -i)

case "$chosen" in 
	"Power Off") poweroff ;;
	"Restart") reboot ;;
	"Lock") slock ;;
	"Suspend") systemctl suspend ;;
	*) exit 1 ;;
esac
