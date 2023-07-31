"""
@author:menglei
@group:售后API
@desc:获取售后列表
"""
from xhs.api.base import RestApi

class AfterSaleListAfterSaleApiRequest(RestApi):
    """
    @:param: status:integer:售后状态 1：待审核；2:待用户寄回；3:待收货；4:完成；5:取消；6:关闭；9:拒绝；9001：商家收货拒绝；11：换货转退款；12:订单商家已确认收货，等待商家发货；13:订单商家已发货，等待用户确认收货。不传默认全部；14：平台介入中
    @:param: pageNo:integer:返回页码 默认 1，页码从 1 开始 PS：当前采用分页返回，数量和页数会一起传，如果不传，则采用 默认值
    @:param: pageSize:integer:返回数量，默认50最大100
    @:param: startTime:integer:查询时间起点
    @:param: endTime:integer:查询时间终点
    @:param: timeType:integer:时间类型，1：根据创建时间查询 end-start<=24h；2：根据更新时间查询 end-start<=30min
    @:param: useHasNext:boolean:是否返回所有数据,true 不返会total 返回 hasNext = true 表示仍有数据，false 返回total
    @:param: reasonId:integer:编号
    @:param: returnType:integer:售后类型 不传/0:全部；1:退货退款；2:换货；3:仅退款(old) 4:仅退款(new) 理论上不会有3出现；5:未发货仅退款
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.status = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.timeType = None
        self.useHasNext = None
        self.reasonId = None
        self.returnType = None

    def getapiname(self):
        return 'afterSale.listAfterSaleApi'