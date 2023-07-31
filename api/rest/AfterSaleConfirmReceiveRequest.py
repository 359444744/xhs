"""
@author:menglei
@group:售后API
@desc:售后确认收货（新）
"""
from xhs.api.base import RestApi

class AfterSaleConfirmReceiveRequest(RestApi):
    """
    @:param: returnsId:string:售后id
    @:param: action:integer:操作类型，1：确认收货；2：拒绝；3：延期
    @:param: reason:integer:拒绝原因，5：未收到退件，快递还在途中；6：已与买家协商一致；7：其他
    @:param: description:string:拒绝原因描述
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.returnsId = None
        self.action = None
        self.reason = None
        self.description = None

    def getapiname(self):
        return 'afterSale.confirmReceive'