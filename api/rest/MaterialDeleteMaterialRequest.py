"""
@author:menglei
@group:素材中心API
@desc:删除素材
"""
from xhs.api.base import RestApi

class MaterialDeleteMaterialRequest(RestApi):
    """
    @:param: materialId:string:
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.materialId = None

    def getapiname(self):
        return 'material.deleteMaterial'