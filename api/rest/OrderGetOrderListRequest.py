"""
@author:menglei
@group:订单API
@desc:订单列表
"""
from xhs.api.base import RestApi

class OrderGetOrderListRequest(RestApi):
    """
    @:param: startTime:integer:时间范围起点
    @:param: endTime:integer:时间范围终点
    @:param: timeType:integer:startTime/endTime对应的时间类型，1 创建时间  限制 end-start<=24h、2 更新时间 限制 end-start<=30min 倒序拉取 最后一页到第一页
    @:param: orderType:integer:订单类型，0/null 全部 1 普通 normal 2 定金预售   3 全款预售(废弃)  4 全款预售(新)  5 换货补发
    @:param: orderStatus:integer:订单状态，0全部 1已下单待付款 2已支付处理中 3清关中 4待发货 5部分发货 6待收货 7已完成 8已关闭 9已取消 10换货申请中
    @:param: pageNo:integer:页码，默认1，限制100 
    @:param: pageSize:integer:查询总数，默认50，限制100
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.startTime = None
        self.endTime = None
        self.timeType = None
        self.orderType = None
        self.orderStatus = None
        self.pageNo = None
        self.pageSize = None

    def getapiname(self):
        return 'order.getOrderList'