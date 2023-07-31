"""
@author:menglei
@group:订单API
@desc:获取取消申请列表（即将下线）
"""
from xhs.api.base import RestApi

class PackageGetCancelApplyListRequest(RestApi):
    """
    @:param: logistics:integer:物流模式 0 所有  1 red_auto -> auto 2 red_box -> proxy、transfer  3 red_bound->bonded
    @:param: status:integer:审核状态 ：0 所有  1 待审核  2 已审核
    @:param: pageNo:integer:从1开始 限制 小于100
    @:param: pageSize:integer:限制  小于 100
    @:param: startTime:integer:时间范围起点
    @:param: endTime:integer:时间范围终点
    @:param: timeType:integer:startTime/endTime对应的时间类型，1 创建时间  限制 end-start<=24h，2 更新时间 限制 end-start<=30min
    @:param: useHasNext:boolean:true表示分页不返会total 返回 hasNext = true 表示仍有数据，false 返回total
    @:param: packageId:string:订单号
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.logistics = None
        self.status = None
        self.pageNo = None
        self.pageSize = None
        self.startTime = None
        self.endTime = None
        self.timeType = None
        self.useHasNext = None
        self.packageId = None

    def getapiname(self):
        return 'package.getCancelApplyList'