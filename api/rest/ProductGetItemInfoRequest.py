"""
@author:menglei
@group:商品API
@desc:获取ITEM详情
"""
from xhs.api.base import RestApi

class ProductGetItemInfoRequest(RestApi):
    """
    @:param: pageSize:integer:当前页码
    @:param: pageNo:integer:页码大小
    @:param: itemId:string:itemid
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.pageSize = None
        self.pageNo = None
        self.itemId = None

    def getapiname(self):
        return 'product.getItemInfo'