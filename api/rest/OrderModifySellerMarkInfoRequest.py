"""
@author:menglei
@group:订单API
@desc:修改订单备注
"""
from xhs.api.base import RestApi

class OrderModifySellerMarkInfoRequest(RestApi):
    """
    @:param: orderId:string:订单号
    @:param: sellerMarkNote:string:商家备注内容
    @:param: operator:string:操作人名称
    @:param: sellerMarkPriority:integer:商家标记优先级，ark订单列表展示旗子颜色 1灰旗 2红旗 3黄旗 4绿旗 5蓝旗 6紫旗
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.orderId = None
        self.sellerMarkNote = None
        self.operator = None
        self.sellerMarkPriority = None

    def getapiname(self):
        return 'order.modifySellerMarkInfo'