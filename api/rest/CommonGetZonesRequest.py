"""
@author:menglei
@group:公共API
@desc:获取地址信息（新）
"""
from xhs.api.base import RestApi

class CommonGetZonesRequest(RestApi):
    """
    @:param: code:string:行政区域代码
    @:param: name:string:行政区域名称
    @:param: upper:string:上一级行政区域
    @:param: filterNonContinental:boolean:是否过滤非大陆行政区域
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.code = None
        self.name = None
        self.upper = None
        self.filterNonContinental = None

    def getapiname(self):
        return 'common.getZones'