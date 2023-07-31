"""
@author:menglei
@group:公共API
@desc:商品标题类目预测
"""
from xhs.api.base import RestApi

class CommonCategoryMatchRequest(RestApi):
    """
    @:param: spuName:string:spu名称
    @:param: topK:integer:返回最符合的类目数量，默认为1
    @:param: externalCategoryName:string:可能的类目名称
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.spuName = None
        self.topK = None
        self.externalCategoryName = None

    def getapiname(self):
        return 'common.categoryMatch'