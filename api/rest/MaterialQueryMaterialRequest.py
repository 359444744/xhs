"""
@author:menglei
@group:素材中心API
@desc:素材列表
"""
from xhs.api.base import RestApi

class MaterialQueryMaterialRequest(RestApi):
    """
    @:param: materialId:string:素材id
    @:param: name:string:素材名
    @:param: type:string:素材类型
    @:param: status:integer:状态,1:上传成功，2：上传中，3：上传失败
    @:param: createTimeFrom:integer:创建开始时间 ms
    @:param: createTimeTo:integer:创建结束时间 ms
    @:param: ascByCreateTime:boolean:创建时间升序
    @:param: pageNo:integer:分页查询，页码
    @:param: pageSize:integer:分页查询，页面大小
    """
    def __init__(self,domain='ark.xiaohongshu.com'):
        RestApi.__init__(self, domain)
        self.materialId = None
        self.name = None
        self.type = None
        self.status = None
        self.createTimeFrom = None
        self.createTimeTo = None
        self.ascByCreateTime = None
        self.pageNo = None
        self.pageSize = None

    def getapiname(self):
        return 'material.queryMaterial'