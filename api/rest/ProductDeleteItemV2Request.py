"""
@author:menglei
@group:商品API
@desc:删除ITEM
"""
from xhs.api.base import RestApi

class ProductDeleteItemV2Request(RestApi):
    """
    @:param: itemIds:array:
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.itemIds = None

    def getapiname(self):
        return 'product.deleteItemV2'