
#!/bin/bash

chosen=$(printf '⏻  Power Off\n♻️ Restart\n🔒 Lock\n💤 Suspend' | rofi -dmenu -i)

# Take action based on the selected option
case "$chosen" in
    '⏻  Power Off')
        systemctl poweroff
        ;;
    '♻️ Restart')
        systemctl reboot
        ;;
    '🔒 Lock')
        slock
        ;;
    '💤 Suspend')
        systemctl suspend
        ;;
    *)
        exit 1
        ;;
esac

