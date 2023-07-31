"""
@author:menglei
@group:订单API
@desc:订单发货
"""
from xhs.api.base import RestApi

class OrderOrderDeliverRequest(RestApi):
    """
    @:param: orderId:string:订单号
    @:param: expressNo:string:快递单号（如使用的是无物流发货，expressNo为发货内容）
    @:param: expressCompanyCode:string:快递公司编码（如使用无物流发货，expressCompanyCode为selfdelivery）
    @:param: expressCompanyName:string:快递公司名称(如传入，则以传入为准，如未传入，则根据expressCompanyCode进行匹配)
    @:param: deliveringTime:integer:发货时间 不传默认当前时间（ms）
    @:param: unpack:boolean:是否拆包发货  true 拆包发货  false正常发货
    @:param: skuIdList:array:拆包发货时 必填
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None
        self.expressNo = None
        self.expressCompanyCode = None
        self.expressCompanyName = None
        self.deliveringTime = None
        self.unpack = None
        self.skuIdList = None

    def getapiname(self):
        return 'order.orderDeliver'