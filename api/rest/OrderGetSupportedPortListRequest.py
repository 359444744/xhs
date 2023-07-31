"""
@author:menglei
@group:订单API
@desc:三方保税支持口岸
"""
from xhs.api.base import RestApi

class OrderGetSupportedPortListRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'order.getSupportedPortList'