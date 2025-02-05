### DEPENDENCIES ###

# 1 brightnessctl
# 2 alsa-utils
# 3 python-psutil
# 4 dbus-next
# 5 physlock

### DEPENDENCIES ###

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess

# from PowerMenuWidget import PowerMenuWidget # fancy power menu

# WAYLADND support
# use xorg-server-wayland


# Startup
@hook.subscribe.startup
def set_wallpaper():
    # Wallpaper (required swaybg)
    subprocess.Popen(["swaybg", "-i", "/home/feralsmurf/Downloads/wallpapers/star.jpg"])
    # Run the battery check script (required mako)
    subprocess.Popen(["mako"])
    subprocess.Popen(["/home/feralsmurf/check_bat_w.sh"])


# Catppuccin mocha color schme
colors = {
    "red": "#f38ba8",
    "orange": "#fab387",
    "green": "#a6e3a1",
    "yellow": "#f9e2af",
    "blue": "#89b4fa",
    "magenta": "#f5c2e7",
    "cyan": "#94e2d5",
    "white": "#cdd6f4",
    "black": "#1e1e2e",
    "mauve": "#cba6f7",
    "gray": "#7f849c",
}

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "p", lazy.spawn("bash /home/feralsmurf/.config/qtile/powermenu.sh")),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Alt+Tab:
    Key([mod], "Tab", lazy.screen.toggle_group(), desc="Toggle between windows"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using rofi"),
    Key([mod], "o", lazy.spawn("rofi -show window"), desc="Show all active windows"),
    #################
    # Custom keys:
    #################
    # physlock
    Key([mod], "l", lazy.spawn("physlock -p '>>> Machine is now locked. Unlock? <<<'")),
    # brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc="Lower Volume by 5%",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc="Raise Volume by 5%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer sset Master toggle"),
        desc="Toggle Mute",
    ),
    # lang
    Key([mod], "F1", lazy.spawn("setxkbmap us"), desc="Change to US layout"),
    Key([mod], "F2", lazy.spawn("setxkbmap ro std"), desc="Change to RO layout"),
    #
    Key(
        [mod],
        "d",
        lazy.spawn("rofi -show window"),
        desc="Show active windows using rofi",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

groups = [
    Group("1", label="α"),
    Group(
        "2",
        # spawn=["firefox"],
        spawn=["qutebrowser"],
        label="β",
    ),
    Group("3", label="γ", spawn=["alacritty -e fish -c 'wttr; exec fish'"]),
    Group("4", label="Δ"),
    Group("5", label="ε"),
    Group("6", label="ζ"),
    Group("7", label="η"),
    Group("8", label="θ"),
    Group("9", label="ι"),
]

layouts = [
    layout.Columns(
        border_focus=colors["green"],
        border_normal=colors["black"],
        border_width=2,
        name="",
        margin=8,  # gaps
    ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="DejaVu Sans Mono Bold",
    fontsize=16,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="block",
                    this_current_screen_border=colors["gray"],
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": (colors["red"], colors["white"]),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                # widget.Net(
                #     fmt="↕️ {} ",
                #     format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}",
                #     prefix="M",
                # ),
                widget.Wlan(fmt=" 🌐 {} ", format="{essid} {quality}/70"),
                # widget.Pomodoro(
                #     fmt="⏲️  {} ", prefix_inactive="Pomodoro"
                # ),
                # widget.Load(fmt="🛠️ {} ", format="{time}:{load:.2f}"),
                # widget.ThermalSensor(
                #     fmt="🔥 {} ",
                #     tag_sensor="Package id 0",
                #     update_interval=10,
                #     format="{temp:.0f}°C",
                # ),
                # widget.Memory(
                #     fmt="🐏 {} ",
                #     format="{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                #     measure_mem="G",
                # ),
                # widget.CPU(fmt="🧠 {} ", format="{load_percent:.0f}%", width=70),
                widget.DF(
                    partition="/",
                    format="{uf}{m} ",
                    fmt="🚧 🚧 🚧 root space warning {}",
                    visible_on_warn=True,
                    wrn_space=4,
                    measure="G",
                ),
                widget.DF(
                    partition="/home",
                    format="{uf}{m} ",
                    fmt="💽 {}",
                    visible_on_warn=False,
                ),
                widget.Backlight(fmt="🪔 {} ", backlight_name="intel_backlight"),
                widget.Volume(fmt="📢 {} "),
                widget.Battery(
                    fmt="⚡️ {} ",
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                ),
                widget.Clock(fmt="⏳️ {} ", format="%Y-%m-%d %a %H:%M"),
                # widget.KeyboardLayout(fmt="🎹 {} ", configured_keyboards=["us", "ro"]),
                # PowerMenuWidget(),
            ],
            24,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=colors["green"],
    border_normal=colors["black"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
