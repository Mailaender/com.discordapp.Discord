#!/usr/bin/env python3
"""
Disable breaking updates which will prompt users to download a deb or tar file
and lock them out of Discord making the program unusable.

This will dramatically improve the experience :

 1) The maintainer doesn't need to be worried at all times of an update which will break Discord.
 2) People will not be locked out of the program while the maintainer runs to update it.

"""

import json
import os
from pathlib import Path

XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME")
if Path(f"{XDG_CONFIG_HOME}/discord/settings.json").is_file():
    with open(f"{XDG_CONFIG_HOME}/discord/settings.json", "r+") as settings_file:
        settings = json.load(settings_file)
        if settings.get("SKIP_HOST_UPDATE"):
            print("Disabling updates already done")
        else:
            skip_host_update = {"SKIP_HOST_UPDATE":True}
            settings.update(skip_host_update)
            settings_file.seek(0)
            json.dump(settings, settings_file, indent = 2)
            print("Disabled updates")
            
else:
    print("settings.json doesn't yet exist, can't disable it yet")
