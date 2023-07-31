"""
@author:menglei
@group:公共API
@desc:获取物流模式列表
"""
from xhs.api.base import RestApi

class CommonLogisticsModeRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.logisticsMode'