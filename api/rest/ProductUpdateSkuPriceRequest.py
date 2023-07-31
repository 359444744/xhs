"""
@author:menglei
@group:商品API
@desc:修改价格
"""
from xhs.api.base import RestApi

class ProductUpdateSkuPriceRequest(RestApi):
    """
    @:param: skuId:string:skuId
    @:param: price:array:价格信息，组合品才是list
    @:param: originalPrice:integer:市场价，单位为分
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuId = None
        self.price = None
        self.originalPrice = None

    def getapiname(self):
        return 'product.updateSkuPrice'