import xhs.api as api
import xhs
from  xhs.api.base import XHSException 
from xhsorm.orm import *
from PIL import Image
import io

xhs.setDefaultAppInfo('9287154631594d41bf31','3acde8577af064e46d8522b2d076e111')


sessionKey='token-99234289e20148778c5dfc371adc2599-0c63958f978441bb987ea2808c8facee'

def get_cateroyson(sessionKey):
    with db_session:
        cats=select( c for c in Categroy  if  c.is_get==False )
        for c in cats:
            getCategories = api.CommonGetCategoriesRequest()
            getCategories.categoryId=c.id
            try:
                rsp=getCategories.getResponse(sessionKey)

                categorys=rsp['data']['categoryV3s']
                
                for category in categorys:
                    if not Categroy.exists(id=category['id']):
                        Categroy(id=category['id'],name=category['name'],level=c.level+1,parent_id=c.id)
                        commit()
                c.is_get=True
                c.is_parent=True
                commit()
            except XHSException as e:
                if e.errorcode==-1009000:
                    c.is_get=True
                    c.is_parent=False
                    commit()
                else:
                    print(e)
                    raise e

def getVariantions(sesskon_key):
    with db_session:
        cats=select( c for c in Categroy  if  c.is_parent==False )
        for c in cats:
            print(c.name)
            print(c.id)
            getVRequest = api.CommonGetVariationsRequest()
            getVRequest.categoryId=c.id
            try:
                rsp=getVRequest.getResponse(sessionKey)
                variations=rsp['data']['variations']
                for variation in variations:
                    v=Variantion.get(id=variation['id'])
                    if not v:
                        v= Variantion(id=variation['id'],name=variation['name'])
                    c.variants.add(v)
                    
                    commit()

            except XHSException as e:
                print(e)

def getAttrubutes(sesskon_key):
    with db_session:
        cats=select( c for c in Categroy  if  c.is_parent==False )
        for c in cats:
            print(c.name)
            print(c.id)
            getARequest = api.CommonGetAttributeListsRequest()
            getARequest.categoryId=c.id
            try:
                rsp=getARequest.getResponse(sessionKey)
                attributes=rsp['data']['attributeV3s']
                for attribute in attributes:
                    a=Attribute.get(id=attribute['id'])
                    if not a:
                        a= Attribute(id=attribute['id'],name=attribute['name'],is_required=attribute['isRequired'],accepts_image=attribute['acceptsImage'],is_multi=attribute['isMulti'],categroy=c)
                        a.category=c
                    
                    commit()

            except XHSException as e:
                print(e)
        


def getAttributeValues(sessionKey):
    with db_session:
        attributes=select( a for a in Attribute  )
        for att in attributes:
            print(att.name)
            print(att.id)
            getVRequest = api.CommonGetAttributeValuesRequest()
            getVRequest.attributeId=att.id
            try:
                rsp=getVRequest.getResponse(sessionKey)
                values=rsp['data']['attributeValueV3s']
                for value in values:
                    v=AttributeValue.get(value_id=value['valueId'])
                    if not v:
                        v= AttributeValue(value_id=value['valueId'],value_name=value['valueName'],attribute=att)
                        v.attribute=att
                    
                    commit()

            except XHSException as e:
                print(e)

import base64

def file_to_base64(path_file):

    with open(path_file,'rb') as f:
        image_bytes = f.read()
        image_bytearray = bytearray(image_bytes)
        base64_data  = base64.b64encode(image_bytearray)
        base64_data = base64_data.decode()
        return base64_data


def updateImages(sessionKey):
    upload_image_req=api.MaterialUploadMaterialRequest()
    upload_image_req.name='test.jpg'
    upload_image_req.type='IMAGE'
    upload_image_req.materialContent=file_to_base64('C:\\Users\\menlei\\Pictures\\MF\\O1CN01u0tzda1GHTGAaHhh0_!!2542210597.png')
    try:
        reponse=upload_image_req.getResponse(sessionKey)
        print(reponse)
    except XHSException  as e:
        print(e)





if __name__ == '__main__':
    #get_cateroyson(sessionKey)
    #getVariantions(sessionKey)
    #getAttrubutes(sessionKey)
    #getAttributeValues(sessionKey)
    updateImages(sessionKey)