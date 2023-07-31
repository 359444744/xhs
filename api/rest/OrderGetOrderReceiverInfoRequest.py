"""
@author:menglei
@group:订单API
@desc:查询订单收件人信息
"""
from xhs.api.base import RestApi

class OrderGetOrderReceiverInfoRequest(RestApi):
    """
    @:param: receiverQueries:array:收件人详情查询列表，请务必在发货前调用一次避免用户修改导致不一致
    @:param: isReturn:boolean:是否是换货单
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.receiverQueries = None
        self.isReturn = None

    def getapiname(self):
        return 'order.getOrderReceiverInfo'