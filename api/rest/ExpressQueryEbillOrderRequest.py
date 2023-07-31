"""
@author:menglei
@group:物流API
@desc:查询面单
"""
from xhs.api.base import RestApi

class ExpressQueryEbillOrderRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: waybillCode:string:面单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.waybillCode = None

    def getapiname(self):
        return 'express.queryEbillOrder'