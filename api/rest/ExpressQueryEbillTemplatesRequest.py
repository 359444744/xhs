"""
@author:menglei
@group:物流API
@desc:查询电子面单模板列表
"""
from xhs.api.base import RestApi

class ExpressQueryEbillTemplatesRequest(RestApi):
    """
    @:param: cpCode:string:快递公司编码
    @:param: brandCode:string:品牌编码，当前只有顺丰快运和顺丰速运查询需要传值
    @:param: type:string:类型，默认不填返回标准模板列表， ark-返回小红书商家配置的模板列表
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.cpCode = None
        self.brandCode = None
        self.type = None

    def getapiname(self):
        return 'express.queryEbillTemplates'