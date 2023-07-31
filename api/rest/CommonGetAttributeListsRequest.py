"""
@author:menglei
@group:公共API
@desc:由末级分类获取属性
"""
from xhs.api.base import RestApi

class CommonGetAttributeListsRequest(RestApi):
    """
    @:param: categoryId:string:末级分类
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.categoryId = None

    def getapiname(self):
        return 'common.getAttributeLists'