# -*- coding: utf-8 -*-
'''
Create on 20230726
@author:menglei
'''

import urllib
import xhs
import time
import urllib.request
X_APP_KEY= 'appId'
X_APP_SECRET= 'app_secret'
X_METHOD= 'method'
X_TIMESTAMP='timestamp'
X_SIGN = "sign"
X_SESSION='accessToken'
X_CODE = 'error_code'
X_SUB_CODE = 'sub_code'
X_MSG = 'error_msg'

X_REQUEST_ID='log_id'
import hashlib
V='version'
import json



def sign(secret, parameters):
    md5_string = "{}?appId={}&timestamp={}&version={}{}".format(parameters.get(X_METHOD),parameters.get(X_APP_KEY),parameters.get(X_TIMESTAMP),parameters.get(V),secret)
    m = hashlib.md5()
    m.update(md5_string.encode("utf-8"))
    sign = m.hexdigest()
    return sign




class XHSException(Exception):
    # ===========================================================================
    # 业务异常类
    # ===========================================================================
    def __init__(self):
        self.errorcode = None
        self.message = None


    def __str__(self, *args, **kwargs):
        sb = "errorcode=" + str(self.errorcode) + \
            " message=" + str(self.message) 

        return sb

class RequestException(Exception):
    # ===========================================================================
    # 请求连接异常类
    # ===========================================================================
    pass



class RestApi():
    def __init__(self,domain='ark.sit.xiaohongshu.com'):
        self.__domain = domain
        self.__httpmethod = "POST"
    
        if (xhs.getDefaultAppInfo()):
            self.__app_id = xhs.getDefaultAppInfo().app_key
            self.__app_secret = xhs.getDefaultAppInfo().app_secret
        
    def get_timestamp(self):
        return str(int(time.time()))
    
    def getapiname(self):
        return ""
    
    def get_request_header(self):
        return {
            'Content-type': 'application/json'
        }
        
    def getTranslateParas(self):
        return {};
        
    def getMultipartParas(self):
        return [];
    
    def set_app_info(self, appinfo):
        # =======================================================================
        # 设置请求的app信息
        # @param appinfo: import top
        #                 appinfo top.appinfo(appkey,secret)
        # =======================================================================
        self.__app_id = appinfo.app_key
        self.__app_secret = appinfo.app_secret
        
    
    def getResponse(self,authrize=None,timeout=30):
        
        
        if 'https://' not in self.__domain:
            self.__domain = 'https://' + self.__domain
        
        sys_parameters={
            X_APP_KEY:self.__app_id,
            X_TIMESTAMP:int(time.time()),
            V:'2.0',
            X_METHOD:self.getapiname(),
        }
            
        application_parameter = self.getApplicationParameters()
        
        sign_parameter = sys_parameters.copy()
        
        sys_parameters[X_SIGN] = sign(self.__app_secret, sign_parameter)
        
        if authrize:
            sys_parameters[X_SESSION]=authrize
        
        
        sys_parameters.update(application_parameter)
        
        
        post_data = json.dumps(sys_parameters)
        
        data =post_data.encode('utf-8')
        url = self.__domain+'/ark/open_api/v3/common_controller'
        request=urllib.request.Request(url,headers=self.get_request_header(),data=data,method=self.__httpmethod)
        response=urllib.request.urlopen(request,timeout=timeout)
        if response.code != 200:
            raise RequestException('invalid http status ' + str(response.status) + ',detail body:' + response.read())
        result = response.read()
        jsonobj = json.loads(result)

        if not jsonobj.get("success"):
            error = XHSException()
            if jsonobj.get(X_CODE):
                error.errorcode = jsonobj[X_CODE]
            if jsonobj.get(X_MSG):
                error.message = jsonobj[X_MSG]
            raise error
        return jsonobj


        
        
        
        
    def getApplicationParameters(self):
        application_parameter = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__") and not key in self.getMultipartParas() and not key.startswith(
                    "_RestApi__") and value is not None:
                if (key.startswith("_")):
                    application_parameter[key[1:]] = value
                else:
                    application_parameter[key] = value
        # 查询翻译字典来规避一些关键字属性
        translate_parameter = self.getTranslateParas()
        for key, value in application_parameter.items():
            if key in translate_parameter:
                application_parameter[translate_parameter[key]] = application_parameter[key]
                del application_parameter[key]
        return application_parameter