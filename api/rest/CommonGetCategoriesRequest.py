"""

@author:menglei

@group:公共API

@desc:获取分类列表

"""

from xhs.api.base import RestApi



class CommonGetCategoriesRequest(RestApi):

    """

    @:param: categoryId:string:父级分类,如果该参数为空，则返回所有的一级分类

    """

    def __init__(self,domain='ark.xiaohongshu.com'):

        RestApi.__init__(self, domain)

        self.categoryId = None



    def getapiname(self):

        return 'common.getCategories'