"""
@author:menglei
@group:商品API
@desc:修改商品主图、主图视频
"""
from xhs.api.base import RestApi

class ProductUpdateItemImageRequest(RestApi):
    """
    @:param: itemId:string:itemId
    @:param: materialType:integer:素材类型，1：图片，2：视频
    @:param: materialUrls:array:素材url，图片全量覆盖、视频取第一个
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.itemId = None
        self.materialType = None
        self.materialUrls = None

    def getapiname(self):
        return 'product.updateItemImage'