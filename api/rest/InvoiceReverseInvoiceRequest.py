"""
@author:menglei
@group:订单API
@desc:发票冲红（逆向冲红）
"""
from xhs.api.base import RestApi

class InvoiceReverseInvoiceRequest(RestApi):
    """
    @:param: xhsInvoiceNo:string:系统开票号
    @:param: operatorId:string:操作人ID
    @:param: operatorName:string:操作人名称
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.xhsInvoiceNo = None
        self.operatorId = None
        self.operatorName = None

    def getapiname(self):
        return 'invoice.reverseInvoice'