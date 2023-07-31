"""
@author:menglei
@group:公共API
@desc:运费模版详情
"""
from xhs.api.base import RestApi

class CommonGetCarriageTemplateRequest(RestApi):
    """
    @:param: templateId:string:运费模板id
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.templateId = None

    def getapiname(self):
        return 'common.getCarriageTemplate'