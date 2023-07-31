"""
@author:menglei
@group:公共API
@desc:批量获取发货时间规则
"""
from xhs.api.base import RestApi

class CommonGetDeliveryRuleRequest(RestApi):
    """
    @:param: getDeliveryRuleRequests:array:批量查询
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.getDeliveryRuleRequests = None

    def getapiname(self):
        return 'common.getDeliveryRule'