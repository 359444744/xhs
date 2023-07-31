"""
@author:menglei
@group:商品API
@desc:修改规格图
"""
from xhs.api.base import RestApi

class ProductUpdateVariantImageRequest(RestApi):
    """
    @:param: spuId:string:spu编号
    @:param: variantId:string:规格id
    @:param: variantValue:string:规格值
    @:param: materialUrl:string:素材url
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.spuId = None
        self.variantId = None
        self.variantValue = None
        self.materialUrl = None

    def getapiname(self):
        return 'product.updateVariantImage'