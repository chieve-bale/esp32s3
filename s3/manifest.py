#include("$(PORT_DIR)/boards/manifest.py")
freeze("modules")

###########下面重写"$(PORT_DIR)/boards/manifest.py"的内容
##freeze("$(PORT_DIR)/modules")#此行替换如下
module("_boot.py", base_path="$(PORT_DIR)/modules")
#module("apa106.py", base_path="$(PORT_DIR)/modules")
#module("espnow.py", base_path="$(PORT_DIR)/modules")
module("flashbdev.py", base_path="$(PORT_DIR)/modules")
module("inisetup.py", base_path="$(PORT_DIR)/modules")

include("$(MPY_DIR)/extmod/asyncio")

# Useful networking-related packages.
require("bundle-networking")

# Require some micropython-lib modules.
#require("aioespnow")
#require("dht")
#require("ds18x20")
#require("neopixel")
#require("onewire")
require("umqtt.robust")
require("umqtt.simple")
#require("upysh")

###an example###
#module("dotstar.py", base_path="$(PORT_DIR)/boards/UM_TINYPICO/modules", opt=3)

