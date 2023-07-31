"""
@author:menglei
@group:订单API
@desc:修改快递单号
"""
from xhs.api.base import RestApi

class OrderModifyOrderExpressInfoRequest(RestApi):
    """
    @:param: orderId:string:订单号
    @:param: expressNo:string:快递单号
    @:param: expressCompanyCode:string:快递公司编码
    @:param: expressCompanyName:string:快递公司名称
    @:param: deliveryOrderIndex:integer:修改拆包订单快递单号必传
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None
        self.expressNo = None
        self.expressCompanyCode = None
        self.expressCompanyName = None
        self.deliveryOrderIndex = None

    def getapiname(self):
        return 'order.modifyOrderExpressInfo'