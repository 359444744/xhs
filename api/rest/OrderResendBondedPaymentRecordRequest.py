"""
@author:menglei
@group:订单API
@desc:三方保税重推支付单
"""
from xhs.api.base import RestApi

class OrderResendBondedPaymentRecordRequest(RestApi):
    """
    @:param: orderId:string:订单号
    @:param: customsType:string:海关类型{总署海关取值:zongshu/地方海关取值：local}
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None
        self.customsType = None

    def getapiname(self):
        return 'order.resendBondedPaymentRecord'