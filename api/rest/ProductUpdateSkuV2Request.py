"""
@author:menglei
@group:商品API
@desc:更新SKU
"""
from xhs.api.base import RestApi

class ProductUpdateSkuV2Request(RestApi):
    """
    @:param: itemId:string:item编号
    @:param: ipq:integer:打包数，只允许创建ipq为1的商品，该字段查询使用
    @:param: originalPrice:integer:市场价，单位分
    @:param: price:integer:售价，单位分，要求小于市场价，上限10w元，即10000000分
    @:param: stock:integer:库存
    @:param: logisticsPlanId:string:物流方案Id
    @:param: whcode:string:仓库号
    @:param: priceType:integer:是否包税
    @:param: erpCode:string:商家编码
    @:param: variants:array:规格列表
    @:param: deliveryTime:object:发货时间信息
    @:param: specImage:string:规格图
    @:param: barcode:string:商品条形码，创建特定品类必填
    @:param: rowNumber:integer:sku在item中的顺序,不支持更新
    @:param: id:string:商品id
    @:param: updatedFields:array:更新字段，不填默认全量，填入后只有传入的字段会被更新
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.itemId = None
        self.ipq = None
        self.originalPrice = None
        self.price = None
        self.stock = None
        self.logisticsPlanId = None
        self.whcode = None
        self.priceType = None
        self.erpCode = None
        self.variants = None
        self.deliveryTime = None
        self.specImage = None
        self.barcode = None
        self.rowNumber = None
        self.id = None
        self.updatedFields = None

    def getapiname(self):
        return 'product.updateSkuV2'