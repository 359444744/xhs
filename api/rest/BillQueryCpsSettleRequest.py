"""
@author:menglei
@group:订单API
@desc:CPS带货达人侧详情查询
"""
from xhs.api.base import RestApi

class BillQueryCpsSettleRequest(RestApi):
    """
    @:param: orderId:string:订单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None

    def getapiname(self):
        return 'bill.queryCpsSettle'