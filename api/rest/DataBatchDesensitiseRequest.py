"""
@author:menglei
@group:订单API
@desc:批量脱敏
"""
from xhs.api.base import RestApi

class DataBatchDesensitiseRequest(RestApi):
    """
    @:param: baseInfos:array:加密数据列表，上限100条
    @:param: actionType:string:操作类型1 - 单个查看订单明文，2 - 批量解密打单，3 - 批量解密后面向三方的数据下发，4 - 其他场景,解密接口必填
    @:param: appUserId:string:三方操作id，服务商自定义，解密接口必填
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.baseInfos = None
        self.actionType = None
        self.appUserId = None

    def getapiname(self):
        return 'data.batchDesensitise'