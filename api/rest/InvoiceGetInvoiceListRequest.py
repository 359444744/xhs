"""
@author:menglei
@group:订单API
@desc:开票列表查询
"""
from xhs.api.base import RestApi

class InvoiceGetInvoiceListRequest(RestApi):
    """
    @:param: invoiceStatus:integer:开票状态，1:待开票；6：已开票；10：待作废
    @:param: refNo:string:来源单号
    @:param: startDateLong:integer:申请时间（开始时间）ms
    @:param: endDateLong:integer:申请时间（结束时间）ms
    @:param: pageNum:integer:分页号
    @:param: pageSize:integer:分页大小,分页大小建议在100以内
    @:param: sortEnum:integer:升序or降序，1:升序；2：降序
    @:param: titleType:integer:发票抬头类型，1：个人；2：企业
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.invoiceStatus = None
        self.refNo = None
        self.startDateLong = None
        self.endDateLong = None
        self.pageNum = None
        self.pageSize = None
        self.sortEnum = None
        self.titleType = None

    def getapiname(self):
        return 'invoice.getInvoiceList'