from libqtile.widget import base
import subprocess


class PowerMenuWidget(base._TextBox):
    def __init__(self, **config):
        # Initialize the widget with the power icon
        super().__init__(" 🌬️ ⏻ ", **config)
        # Add callback for left mouse button click
        self.add_callbacks({"Button1": self.run_power_menu})

    def run_power_menu(self):
        try:
            power_menu_script = "/home/feralsmurf/.config/qtile/powermenu.sh"
            # Use shell=True to execute the script through the shell
            subprocess.run(
                power_menu_script,
                shell=True,
                check=True,
                text=True,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            # Check if the error was due to the script being terminated by the user (e.g., pressing Escape)
            if (
                e.returncode == 1
            ):  # Assuming return code 1 indicates cancellation or similar non-error termination
                self.update("Powermenu cancelled, but still active ⏻ ")
            else:
                # Log the error along with stderr if the script fails for a different reason
                self.update(f"Script error: {e}; Stderr: {e.stderr}")
        except Exception as e:
            # Catch all other exceptions and log the error
            self.update(f"Unexpected error: {e}")

