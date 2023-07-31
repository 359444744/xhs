"""
@author:menglei
@group:公共API
@desc:cc资质检查
"""
from xhs.api.base import RestApi

class CommonCcCheckRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.ccCheck'