"""
@author:menglei
@group:公共API
@desc:获取快递公司信息
"""
from xhs.api.base import RestApi

class CommonGetExpressCompanyListRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.getExpressCompanyList'