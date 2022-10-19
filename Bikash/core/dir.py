# Powered By BikashHalder Or Aditya Halder IF You Fresh Any Problem To Contact The BgtRobot Owner

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "resource" not in listdir():
        LOGGER(__name__).warning(
            f"📌 𝐀𝐬𝐬𝐞𝐭𝐬 𝐅𝐨𝐥𝐝𝐞𝐫 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝 ❌.\n\n 🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐂𝐥𝐨𝐧𝐞 𝐑𝐞𝐩𝐨 𝐀𝐠𝐚𝐢𝐧 🌺."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
