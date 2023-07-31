import json
import requests
#from bs4 import BeautifulSoup

header={
'Accept':'application/json',
'Content-Type': 'application/json;charset=UTF-8'
}

api_group_response=requests.get('https://open.xiaohongshu.com/api/doc/list',headers=header)
api_groups=api_group_response.json().get('data')
api_groups = json.loads(api_groups)
for api_group in api_groups:
    
    api_group_id=api_group.get('id')
    api_group_name=api_group.get('navigationName')
    #print(api_group_name)
    api_group_detail_response=requests.get('https://open.xiaohongshu.com/api/doc/second/list?apiNavigationId={}'.format(api_group_id),headers=header)
    
    
    api_list=json.loads(api_group_detail_response.json().get('data'))
    
    for api in api_list:
        id=api.get('apiId')
        gatewayId=api.get('gatewayId')
        gatewayVersionId=api.get('gatewayVersionId')
        grouop_name=api.get('navigationDetailName')
        navigationDetailDesc=api.get('navigationDetailDesc')#接口描述
        api_path=api.get('path')
        url="https://open.xiaohongshu.com/api/doc/info?gatewayId={}&gatewayVersionId={}&apiId={}".format(gatewayId,gatewayVersionId,id)
        response=requests.get(url,headers=header)
        #print(response.json())
        api_info=response.json().get('data')
        if  api_info.get('specJson').get('requestBody'):#有参数
            reuqest_body=api_info.get('specJson').get('requestBody')
            propertys=reuqest_body.get('content').get('application/json').get('schema').get('properties')
            required=reuqest_body.get('content').get('application/json').get('schema').get('required')
            if not required:
                required=[]
            print(propertys)
        else:
            print('没有参数')
            propertys={}
        param_desc=""
        param_result=""
        name=api_path
        api_des=navigationDetailDesc
        class_name='Request'

        cname=''.join(["".join(i[:1].upper() + i[1:])  for i in name.split('.')]).strip()
        class_name=cname+class_name
        pyheader = "\"\"\"\r\n@author:menglei\r\n@group:{}\r\n@desc:{}\r\n\"\"\"\r\nfrom xhs.api.base import RestApi\r\n\r\nclass {}(RestApi):\r\n    \"\"\"\r\n".format(
          api_group_name,  api_des, class_name
        )

        pyend="\r\n    def getapiname(self):\r\n" \
        "        return '{}'".format(name)
        data = {'id':name}

        for key ,value in propertys.items():
                paramName=key
                paramType=value['type']
                if key in required:
                    isMust='true'
                else:
                    isMust='false'
                paramDesc=value.get('description','')
                param_desc+="    @:param: {}:{}:{}\r\n".format(paramName,paramType,paramDesc)

                param_result+="        self.{} = None\r\n".format(paramName)


        pycentor="    \"\"\"\r\n    def __init__(self,domain='ark.xiaohongshu.com'):\r\n        RestApi.__init__(self, domain)\r\n"

        pyresult=pyheader+param_desc+pycentor+param_result+pyend
        print(pyresult)

        with open('C:\\Users\\menlei\\小红书\\xhs\\api\\rest\\{}.py'.format(class_name),'w',encoding='utf-8') as f:
            f.write(pyresult)
        # with open('E:\\拼多多api\\pdd\\api\\_init_.py','a') as f:
        #     f.write('from pdd.api.rest.{} import {} \n'.format(class_name,class_name))
        print("from pdd.api.rest.{} import {}".format(class_name,class_name))


# response=requests.get('https://op.jinritemai.com/doc/external/open/queryDocArticleDetail?articleId=82&onlyView=false')
# text=response.json().get('data').get('article').get('content')
# lins= text.split('\n')
# for line in lins:
#     if '请求入参' in line:
#         index=lins.index(line)
#         data=lins[index+1]
#         if 'Tree' in data:
#             doucment=BeautifulSoup(data,'lxml')
#             treetable=doucment.find('treetable')
#             datasource=treetable.attrs['datasource']
#             print(datasource)
#     if '响应字段' in line:
#         index=lins.index(line)
#         data=lins[index+1]
#         print(data)