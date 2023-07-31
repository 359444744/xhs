"""
@author:menglei
@group:售后API
@desc:售后审核（新）
"""
from xhs.api.base import RestApi

class AfterSaleAuditReturnsRequest(RestApi):
    """
    @:param: returnsId:string:售后订单ID
    @:param: action:integer:操作类型，1：同意直接退款 (换货不适用)；2：同意寄回(仅退款不适用)；3：拒绝
    @:param: reason:integer:拒绝原因, 当操作类型为“拒绝”时必传, 拒绝原因有: 1-买家未能提供有效凭证； 99-其他
    @:param: description:string:拒绝原因描述, 当拒绝原因为“其他”时必填
    @:param: message:string:给用户留言, 当操作类型为“同意寄回”时字段有效
    @:param: receiverInfo:object:寄回地址信息, 同意寄回时字段有效 
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.returnsId = None
        self.action = None
        self.reason = None
        self.description = None
        self.message = None
        self.receiverInfo = None

    def getapiname(self):
        return 'afterSale.auditReturns'