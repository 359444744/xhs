"""
@author:menglei
@group:物流API
@desc:更新面单
"""
from xhs.api.base import RestApi

class ExpressUpdateEbillOrderRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: waybillCode:string:快递单号
    @:param: objectId:string:请求id
    @:param: logisticsServices:string:增值服务,见[对接说明](https://open.xiaohongshu.com/document/developer/file/38)附录物流增值服务
    @:param: packageInfo:object:
    @:param: recipient:object:
    @:param: sender:object:
    @:param: templateId:number:电子面单模板ID
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.waybillCode = None
        self.objectId = None
        self.logisticsServices = None
        self.packageInfo = None
        self.recipient = None
        self.sender = None
        self.templateId = None

    def getapiname(self):
        return 'express.updateEbillOrder'