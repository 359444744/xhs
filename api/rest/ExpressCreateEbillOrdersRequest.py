"""
@author:menglei
@group:物流API
@desc:批量取号
"""
from xhs.api.base import RestApi

class ExpressCreateEbillOrdersRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: sender:object:寄件人地址必须和订购关系的地址保持一致
    @:param: tradeOrderInfoList:array:请求面单列表（上限10个）
    @:param: extraInfo:string:拓展信息，特殊场景下使用
    @:param: customerCode:string:月结卡号，直营快递公司一般要求必填
    @:param: brandCode:string:品牌编码，顺丰要求必填
    @:param: productCode:string:产品编码，仅部分快递公司支持传入，见[对接说明](https://open.xiaohongshu.com/document/developer/file/38)附录物流产品类型
    @:param: callDoorPickUp:boolean:是否预约上门，仅部分快递公司支持传入
    @:param: doorPickUpTime:string:预约上门取件时间，'yyyy-MM-dd HH:mm:ss'，仅部分快递公司支持传入
    @:param: doorPickUpEndTime:string:预约上门取件截止时间，'yyyy-MM-dd HH:mm:ss'，仅部分快递公司支持传入
    @:param: sellerName:string:店铺名称，对参数内容没有限制
    @:param: branchCode:string:网点编码，加盟型快递公司一般要求必填
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.sender = None
        self.tradeOrderInfoList = None
        self.extraInfo = None
        self.customerCode = None
        self.brandCode = None
        self.productCode = None
        self.callDoorPickUp = None
        self.doorPickUpTime = None
        self.doorPickUpEndTime = None
        self.sellerName = None
        self.branchCode = None

    def getapiname(self):
        return 'express.createEbillOrders'