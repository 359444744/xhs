"""
@author:menglei
@group:订单API
@desc:取消申请审核（即将下线）
"""
from xhs.api.base import RestApi

class PackageAuditCancelApplyRequest(RestApi):
    """
    @:param: packageId:string:订单编号
    @:param: auditType:integer:1审核通过   2 审核拒绝
    @:param: refuseReason:string:审核拒绝理由
    @:param: operator:string:操作人 最好精确到个人
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.packageId = None
        self.auditType = None
        self.refuseReason = None
        self.operator = None

    def getapiname(self):
        return 'package.auditCancelApply'