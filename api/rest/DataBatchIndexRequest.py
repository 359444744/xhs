"""
@author:menglei
@group:订单API
@desc:批量获取索引串
"""
from xhs.api.base import RestApi

class DataBatchIndexRequest(RestApi):
    """
    @:param: indexBaseInfoList:array:索引串查询列表
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.indexBaseInfoList = None

    def getapiname(self):
        return 'data.batchIndex'