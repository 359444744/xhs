"""
@author:menglei
@group:库存API
@desc:同步库存
"""
from xhs.api.base import RestApi

class InventorySyncSkuStockRequest(RestApi):
    """
    @:param: skuId:string:商品编号
    @:param: qty:integer:同步库存数/增减库存数，同步库存时：qty是商品总库存数，可售库存+独立库存+保留库存，接口逻辑会用这个数 - 独立库存 - 保留库存，去设置可售库存；增减库存时：操作可售库存的增减
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.skuId = None
        self.qty = None

    def getapiname(self):
        return 'inventory.syncSkuStock'