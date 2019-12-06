init -1002 python:
    class __7DL:

        def __init__(self):
            # Configuration
            self.version = (0, 0, 0) # (major, minor, patch)
            self.type = "nonsteam" # steam/nonsteam/mobile
            
            # Variables
            self.rootpath = 'mods/scenario_alt' if self.type == "nonsteam" else 'scenario_alt'

        def ambience(self, name):
            return "%s/Sound/ambience/ambience_%s_7dl.ogg" % (self.rootpath, name)

        def music(self, name):
            print("Getting music %s..." % name)
            return "%s/Sound/music/%s_7dl.ogg" % (self.rootpath, name)

        def sfx(self, name):
            return "%s/Sound/sfx/%s_7dl.ogg" % (self.rootpath, name)

    _7DL = __7DL()