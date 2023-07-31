class AppInfo(object):
    def __init__(self, appKey, appSecret):
        self.app_key = appKey
        self.app_secret = appSecret


def getDefaultAppInfo():
    pass


def setDefaultAppInfo(appKey, appSecret):
    default = AppInfo(appKey, appSecret)
    global getDefaultAppInfo
    getDefaultAppInfo = lambda: default