"""
@author:menglei
@group:公共API
@desc:获取商家地址库
"""
from xhs.api.base import RestApi

class CommonGetAddressRecordRequest(RestApi):
    """
    @:param: pageIndex:integer:默认返回商家收货地址的页数为1，限制 小于100
    @:param: pageSize:integer:默认返回20，限制 小于200
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.pageIndex = None
        self.pageSize = None

    def getapiname(self):
        return 'common.getAddressRecord'