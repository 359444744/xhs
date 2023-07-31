"""
@author:menglei
@group:订单API
@desc:三方保税商品备案信息同步
"""
from xhs.api.base import RestApi

class OrderSyncItemCustomsInfoRequest(RestApi):
    """
    @:param: barcode:string:商品条形码
    @:param: customsName:string:口岸编码，取值为三方保税支持口岸接口返回的口岸编码集合中的某个值
    @:param: hsCode:string:HS编码，即海关税则号
    @:param: generalTaxRate:number:税率
    @:param: quantity1:number:法一数量
    @:param: quantity2:number:法二数量
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.barcode = None
        self.customsName = None
        self.hsCode = None
        self.generalTaxRate = None
        self.quantity1 = None
        self.quantity2 = None

    def getapiname(self):
        return 'order.syncItemCustomsInfo'