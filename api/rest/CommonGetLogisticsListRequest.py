"""
@author:menglei
@group:公共API
@desc:获取物流方案列表
"""
from xhs.api.base import RestApi

class CommonGetLogisticsListRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.getLogisticsList'