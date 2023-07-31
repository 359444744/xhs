"""
@author:menglei
@group:订单API
@desc:小包批次创建
"""
from xhs.api.base import RestApi

class OrderCreateTransferBatchRequest(RestApi):
    """
    @:param: orders:array:转运订单信息
    @:param: planInfoId:string:物流方案id
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orders = None
        self.planInfoId = None

    def getapiname(self):
        return 'order.createTransferBatch'