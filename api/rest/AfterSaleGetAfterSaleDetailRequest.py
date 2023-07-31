"""
@author:menglei
@group:售后API
@desc:售后详情
"""
from xhs.api.base import RestApi

class AfterSaleGetAfterSaleDetailRequest(RestApi):
    """
    @:param: afterSaleId:string:售后id
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.afterSaleId = None

    def getapiname(self):
        return 'afterSale.getAfterSaleDetail'