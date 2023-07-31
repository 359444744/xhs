"""
@author:menglei
@group:公共API
@desc:由属性获取属性值
"""
from xhs.api.base import RestApi

class CommonGetAttributeValuesRequest(RestApi):
    """
    @:param: attributeId:string:属性值编号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.attributeId = None

    def getapiname(self):
        return 'common.getAttributeValues'