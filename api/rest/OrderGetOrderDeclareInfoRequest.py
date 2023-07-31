"""
@author:menglei
@group:订单API
@desc:海关申报信息
"""
from xhs.api.base import RestApi

class OrderGetOrderDeclareInfoRequest(RestApi):
    """
    @:param: orderId:string:订单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None

    def getapiname(self):
        return 'order.getOrderDeclareInfo'