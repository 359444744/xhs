"""
@author:menglei
@group:商品API
@desc:查询Item列表
"""
from xhs.api.base import RestApi

class ProductSearchItemListRequest(RestApi):
    """
    @:param: pageNo:integer:页码
    @:param: pageSize:integer:页大小
    @:param: searchParam:object:查询条件
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.pageNo = None
        self.pageSize = None
        self.searchParam = None

    def getapiname(self):
        return 'product.searchItemList'