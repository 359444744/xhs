"""
@author:menglei
@group:素材中心API
@desc:修改素材
"""
from xhs.api.base import RestApi

class MaterialUpdateMaterialRequest(RestApi):
    """
    @:param: materialId:string:素材id
    @:param: materialName:string:素材名
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.materialId = None
        self.materialName = None

    def getapiname(self):
        return 'material.updateMaterial'