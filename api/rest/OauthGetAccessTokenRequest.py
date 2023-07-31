from xhs.api.base import RestApi
class OauthGetAccessTokenRequest(RestApi):
	def __init__(self,domain='ark.xiaohongshu.com',port=80):
		RestApi.__init__(self,domain)
		self.code = None
	def getapiname(self):
		return 'oauth.getAccessToken'