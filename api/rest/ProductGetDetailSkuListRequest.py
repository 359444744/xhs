"""
@author:menglei
@group:商品API
@desc:商品列表完整版（新）
"""
from xhs.api.base import RestApi

class ProductGetDetailSkuListRequest(RestApi):
    """
    @:param: id:string:商品编号，使用id查询其他条件可以不填
    @:param: createTimeFrom:integer:商品创建时间开始时间，Unix-Time时间戳
    @:param: createTimeTo:integer:商品创建时间结束时间，Unix-Time时间戳
    @:param: updateTimeFrom:integer:商品更新时间开始时间，Unix-Time时间戳
    @:param: updateTimeTo:integer:商品更新时间结束时间，Unix-Time时间戳
    @:param: buyable:boolean:是否在架上
    @:param: stockGte:integer:库存大于等于某数
    @:param: stockLte:integer:库存小于等于某数
    @:param: pageNo:integer:返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值
    @:param: pageSize:integer:返回数量，默认50最大100
    @:param: barcode:string:商品条码
    @:param: scSkucode:string:小红书编码
    @:param: singlePackOnly:boolean:只返回单品类型的商品
    @:param: lastId:string:查询起始商品id，全店商品时间倒序
    @:param: isChannel:boolean:不传返回全部，传true只返回渠道商品，传false只返回非渠道商品
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.id = None
        self.createTimeFrom = None
        self.createTimeTo = None
        self.updateTimeFrom = None
        self.updateTimeTo = None
        self.buyable = None
        self.stockGte = None
        self.stockLte = None
        self.pageNo = None
        self.pageSize = None
        self.barcode = None
        self.scSkucode = None
        self.singlePackOnly = None
        self.lastId = None
        self.isChannel = None

    def getapiname(self):
        return 'product.getDetailSkuList'