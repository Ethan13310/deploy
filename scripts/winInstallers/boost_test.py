import sys

try:
    import pkg_resources
    #maybe the version should be configured by makeWinInstaller
    pkg_resources.require("boost")[0].version == "1.44" 
    sys.exit(0)
except Exception, e:
    sys.exit(1)
