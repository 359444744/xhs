"""
@author:menglei
@group:订单API
@desc:查询月度结算单下载地址
"""
from xhs.api.base import RestApi

class BillDownloadStatementRequest(RestApi):
    """
    @:param: month:string:结算月份，yyyy-MM格式
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.month = None

    def getapiname(self):
        return 'bill.downloadStatement'