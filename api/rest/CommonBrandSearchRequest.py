"""
@author:menglei
@group:公共API
@desc:获取品牌信息
"""
from xhs.api.base import RestApi

class CommonBrandSearchRequest(RestApi):
    """
    @:param: categoryId:string:末级类目id
    @:param: keyword:string:品牌关键字
    @:param: pageNo:integer:品牌页数, 从第一页开始,默认为1
    @:param: pageSize:integer:品牌列表每页数量，默认为20,最大20
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.categoryId = None
        self.keyword = None
        self.pageNo = None
        self.pageSize = None

    def getapiname(self):
        return 'common.brandSearch'