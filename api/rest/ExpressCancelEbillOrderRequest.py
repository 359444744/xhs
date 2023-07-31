"""
@author:menglei
@group:物流API
@desc:取消面单
"""
from xhs.api.base import RestApi

class ExpressCancelEbillOrderRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: waybillCode:string:快递单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.waybillCode = None

    def getapiname(self):
        return 'express.cancelEbillOrder'