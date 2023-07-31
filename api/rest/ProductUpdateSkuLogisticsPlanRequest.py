"""
@author:menglei
@group:商品API
@desc:更新物流方案
"""
from xhs.api.base import RestApi

class ProductUpdateSkuLogisticsPlanRequest(RestApi):
    """
    @:param: skuId:string:skuId
    @:param: logisticsPlanId:string:wuliufanganid
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuId = None
        self.logisticsPlanId = None

    def getapiname(self):
        return 'product.updateSkuLogisticsPlan'