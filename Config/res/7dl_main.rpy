init -1002 python:
    class _7DL:
        def __init__(self):
            raise Exception("Class _7DL mustn't create instances!")

        rootpath = 'mods/scenario_alt' if nonsteam_7dl else 'scenario_alt'

        @static
        def ambience(name):
            return "%s/Sound/ambience/ambience_%s" % (_7DL.rootpath, name)

        @static
        def music(name):
            return "%s/Sound/music/%s" % (_7DL.rootpath, name)

        @static
        def sfx(name):
            return "%s/Sound/sfx/%s" % (_7DL.rootpath, name)