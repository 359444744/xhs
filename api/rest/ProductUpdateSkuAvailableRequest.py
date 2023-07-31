"""
@author:menglei
@group:商品API
@desc:商品上下架
"""
from xhs.api.base import RestApi

class ProductUpdateSkuAvailableRequest(RestApi):
    """
    @:param: skuId:string:skuId
    @:param: available:boolean:商家上架意愿
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuId = None
        self.available = None

    def getapiname(self):
        return 'product.updateSkuAvailable'