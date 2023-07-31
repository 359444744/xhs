"""
@author:menglei
@group:售后API
@desc:售后换货确认收货并发货
"""
from xhs.api.base import RestApi

class AfterSaleReceiveAndShipRequest(RestApi):
    """
    @:param: returnsId:string:售后id
    @:param: expressCompanyCode:string:物流公司编码
    @:param: expressNo:string:物流单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.returnsId = None
        self.expressCompanyCode = None
        self.expressNo = None

    def getapiname(self):
        return 'afterSale.receiveAndShip'