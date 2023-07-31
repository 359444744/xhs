"""
@author:menglei
@group:物流API
@desc:查询电子面单订购关系
"""
from xhs.api.base import RestApi

class ExpressQueryEbillSubscribesRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: needUsage:boolean:是否需要返回使用情况
    @:param: brandCode:string:品牌编码
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.needUsage = None
        self.brandCode = None

    def getapiname(self):
        return 'express.queryEbillSubscribes'