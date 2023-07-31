"""
@author:menglei
@group:公共API
@desc:运费模版列表
"""
from xhs.api.base import RestApi

class CommonGetCarriageTemplateListRequest(RestApi):
    """
    @:param: pageIndex:integer:默认返回运费模板的页数为1，限制 小于100
    @:param: pageSize:integer:默认返回20，限制 小于100
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.pageIndex = None
        self.pageSize = None

    def getapiname(self):
        return 'common.getCarriageTemplateList'