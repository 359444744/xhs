"""
@author:menglei
@group:公共API
@desc:获取地址信息
"""
from xhs.api.base import RestApi

class CommonGetNestZoneRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.getNestZone'