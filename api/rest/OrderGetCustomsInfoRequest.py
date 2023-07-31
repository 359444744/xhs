"""
@author:menglei
@group:订单API
@desc:三方保税商品备案信息查询
"""
from xhs.api.base import RestApi

class OrderGetCustomsInfoRequest(RestApi):
    """
    @:param: barcode:string:商品条形码
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.barcode = None

    def getapiname(self):
        return 'order.getCustomsInfo'