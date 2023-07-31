"""
@author:menglei
@group:库存API
@desc:获取商品库存
"""
from xhs.api.base import RestApi

class InventoryGetSkuStockRequest(RestApi):
    """
    @:param: skuId:string:商品编号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuId = None

    def getapiname(self):
        return 'inventory.getSkuStock'