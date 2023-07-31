"""
@author:menglei
@group:商品API
@desc:删除SKU
"""
from xhs.api.base import RestApi

class ProductDeleteSkuV2Request(RestApi):
    """
    @:param: skuIds:array:待删除skuId列表
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuIds = None

    def getapiname(self):
        return 'product.deleteSkuV2'