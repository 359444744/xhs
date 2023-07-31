"""
@author:menglei
@group:素材中心API
@desc:上传素材
"""
from xhs.api.base import RestApi

class MaterialUploadMaterialRequest(RestApi):
    """
    @:param: name:string:素材名
    @:param: type:string:素材类型，IMAGE/VIDEO
    @:param: materialContent:array:素材文件字节数组，使用读取照片或视频后的byte[]数组， 请求转json时byte[]数组通过base64编码转成String
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.name = None
        self.type = None
        self.materialContent = None

    def getapiname(self):
        return 'material.uploadMaterial'