"""
@author:menglei
@group:订单API
@desc:订单物流轨迹
"""
from xhs.api.base import RestApi

class OrderGetOrderTrackingRequest(RestApi):
    """
    @:param: orderId:string:订单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None

    def getapiname(self):
        return 'order.getOrderTracking'