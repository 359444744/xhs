"""
@author:menglei
@group:公共API
@desc:获取老版本商家授权信息
"""
from xhs.api.base import RestApi

class CommonGetSellerKeyInfoRequest(RestApi):
    """
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)

    def getapiname(self):
        return 'common.getSellerKeyInfo'