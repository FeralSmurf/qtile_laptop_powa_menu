from libqtile.widget import base
import subprocess


class PowerMenuWidget(base._TextBox):
    def __init__(self, **config):
        base._TextBox.__init__(self, " ⚙️ ", **config)

    def button_press(self, x, y, button):
        if button == 1:
            self.run_script()

    def run_script(self):
        subprocess.run(["/home/feralsmurf/.config/qtile/powermenu.sh"])
