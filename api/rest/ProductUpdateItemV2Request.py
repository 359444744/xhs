"""
@author:menglei
@group:商品API
@desc:更新ITEM
"""
from xhs.api.base import RestApi

class ProductUpdateItemV2Request(RestApi):
    """
    @:param: name:string:item标题
    @:param: ename:string:item英文名
    @:param: brandId:integer:品牌ID,目前查询品牌返回均为String但是是数字可以强转成Long使用
    @:param: categoryId:string:末级商品类目ID
    @:param: attributes:array:item属性
    @:param: shippingTemplateId:string:运费模板ID
    @:param: shippingGrossWeight:integer:商品物流重量（克），当运费模版选择按重量计费时，该值必须大于0
    @:param: variantIds:array:item下商品规格列表
    @:param: images:array:商品主图(必传)
    @:param: videoUrl:string:主图视频
    @:param: articleNo:string:商品货号
    @:param: imageDescriptions:array:商品详情描述图片
    @:param: transparentImage:string:透明图
    @:param: description:string:商品描述文字，上限500字
    @:param: faq:array:常见问题
    @:param: deliveryMode:integer:物流模式,0：普通，1：支持无物流发货（限定类目支持，不支持的类目创建会报错）
    @:param: freeReturn:integer:是否支持7天无理由,1：支持，2：不支持，不传会按照规则给默认值，必须支持则支持，不必须则不支持
    @:param: id:string:商品id
    @:param: updatedFields:array:更新字段，不填默认全量，填入后只有传入的字段会被更新
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.name = None
        self.ename = None
        self.brandId = None
        self.categoryId = None
        self.attributes = None
        self.shippingTemplateId = None
        self.shippingGrossWeight = None
        self.variantIds = None
        self.images = None
        self.videoUrl = None
        self.articleNo = None
        self.imageDescriptions = None
        self.transparentImage = None
        self.description = None
        self.faq = None
        self.deliveryMode = None
        self.freeReturn = None
        self.id = None
        self.updatedFields = None

    def getapiname(self):
        return 'product.updateItemV2'