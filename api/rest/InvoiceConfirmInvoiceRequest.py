"""
@author:menglei
@group:订单API
@desc:开票结果回传（正向蓝票开具）
"""
from xhs.api.base import RestApi

class InvoiceConfirmInvoiceRequest(RestApi):
    """
    @:param: xhsInvoiceNo:string:财务开票编码
    @:param: refNo:string:来源单号
    @:param: invoiceType:integer:发票类型，0:发票类型未知;1:增值税专用发票；2:增值税纸质普通发票；3:增值税电子普通发票；4:形式发票
    @:param: file:array:发票pdf文件字节数组，使用读取照片或视频后的byte[]数组， 请求转json时byte[]数组通过base64编码转成String
    @:param: invoiceNo:string:发票号码，8位数字
    @:param: operatorId:string:操作人ID
    @:param: operatorName:string:操作人名称
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.xhsInvoiceNo = None
        self.refNo = None
        self.invoiceType = None
        self.file = None
        self.invoiceNo = None
        self.operatorId = None
        self.operatorName = None

    def getapiname(self):
        return 'invoice.confirmInvoice'