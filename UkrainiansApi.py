# coding: utf8
__author__ = 'Alban'
import requests
import MethodsUrls

class Session:
	def __init__(self, userName, password):
		# Authorization payloads
		self.AuthPL = {
			'grant_type': 'password',
			'userName': userName, 
			'password': password
		}
		# Info about your account
		self.usrinfo = requests.post(MethodsUrls.url, data = self.AuthPL).json()
		# Request headers
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
			'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,uk;q=0.2',
			'Authorization': 'bearer ' + self.usrinfo['access_token']
		}

	def setProfilePhoto(self, path, url = False):
		'''
		Example: setProfilePhoto(path = 'https://site/image.png/', url = True)
		Params: set path to folder on your PC if param url = False.
		If url = True, set url to image
		'''
		if url:
			uploadImagePayLoads = [
				('images', ('foo.png', requests.get(path).content, 'image/png'))
			]
		else:
			uploadImagePayLoads = [
		        ('images', ('foo.png', open(path, 'rb'), 'image/png'))
			]
		requests.post(MethodsUrls.setPhotoUrl, headers = self.headers, files = uploadImagePayLoads)

	def getMutualFriends(self, userID, skip = 0):
		'''
		Example: getMutualFriends(userID = 1337, skip = 0)
		This method will return json object
		'''
		return requests.get(MethodsUrls.getMutualFriendsUrl.format(userID, skip), headers = self.headers).json()

	def getGroups(self):
		'''
		Example: getGroups()
		This method will return json object
		'''
		return requests.get(MethodsUrls.getMyGroupsUrl, headers = self.headers).json()

	def leaveGroup(self, groupID):
		'''
		Example: leaveGroup(1337)
		This method will return json object
		'''
		return requests.post(MethodsUrls.unFollowUrl.format(groupID), headers = self.headers).json()

	def joinGroup(self, groupID):
		'''
		Example: joinGroup(groupID = 1337)
		This method will return json object
		'''
		return requests.post(MethodsUrls.communityFollowUrl.format(groupID), headers = self.headers).json()

	def searchGroups(self, skip = 0, orderby = 0):
		'''
		Example: searchGroups(skip = 50, orderby = 1)
		Default this method return 50 groups
		Param 'orderby', values: 0 - sort by relevance, 1 - sort by followers count
		This method will return json object
		'''
		return requests.get(MethodsUrls.communitySearchUrl.format(orderby, skip), headers = self.headers).json()

	def addComment(self, postID, text):
		'''
		Example: addComment(postID = 'post_id', text = 'Hello world')
		This method will return json object
		'''
		return requests.post(MethodsUrls.commentAddUrl, data = {
			"contentType":0,
			"contentId":postID,
			"text":text}, headers = self.headers).json()

	def deleteFriends(self, userID):
		'''
		Example: deleteFriends(userID = 1337)
		This method will return json object
		'''
		return requests.post(MethodsUrls.deleteFriendUrl, data = {
			"routeId": userID
			}, headers = self.headers).json()

	def acceptFollower(self, userID):
		'''
		Example: acceptFollower(userID = 1337)
		This method will return json object
		'''
		return requests.post(MethodsUrls.acceptFollowersUrl, data = {
			"routeId": userID
			}, headers = self.headers).json()

	def getFollowers(self, skip = 0, userID = None):
		'''
		Example: getFollowers(userID = 1337, skip = 0)
		This method will return json object
		This method will return 20 followers, for get more, set the skip param
		'''
		if userID is None:
			userID = self.usrinfo['routeId']
		return requests.get(MethodsUrls.getFollowersUrl.format(userID, skip), headers = self.headers).json()

	def getMessages(self, userID):
		'''
		Example: getMessages(userID = 1337)
		This method will return json object
		'''
		return requests.get(MethodsUrls.getMessageUrl.format(userID), headers = self.headers).json()

	def getDialogs(self):
		'''
		Example: getDialogs()
		This method will return json object
		This method will return 20 dialogs, for get more, set the skip param
		'''
		return requests.get(MethodsUrls.getDialogsUrl, headers = self.headers).json()

	def getFriends(self, userID = None, skip = 0): # return 20 friends without offset
		'''
		Example: getMessages(userID = 1337, skip = 0)
		This method will return json object
		This method will return 20 friends, for get more, set the skip param
		'''
		if userID is None:
			userID = self.usrinfo['routeId']
		return requests.get(MethodsUrls.getFriendsUrl.format(userID, skip), headers = self.headers).json()

	def sendMessage(self, ID, text):
		'''
		Example: sendMessage(userID = 1337, text = 'hello')
		This method will return json object
		'''
		return requests.post(MethodsUrls.sendMsgUrl, data = {"text":text,
			"dialogId":ID}, headers = self.headers).json()

	def searchUsers(self, sex = 0, city = 0, country = 0, online = 'false', relationship = 0, maxage = 100, minage = 0, skip = 0, school = 0, universityId = 0, top = 40):
		'''
		Params: sex, city, country, online, relationship, maxage, minage, skip, school, universityId, top 
		Example: searchUsers(sex = 0, city = 0, country = 0, online = 'false', relationship = 0, maxage = 100, minage = 0, skip = 0, school = 0, universityId = 0, top = 40)
		This method will return json object
		'''
		return requests.get(MethodsUrls.userSearchUrl.format(
			city, country, sex, online, maxage, minage, relationship, school, skip, top, universityId), headers = self.headers).json()

	def inviteAllFriendsInGroup(self, groupID, skip = 0):
		'''
		Example: inviteAllFriendsInGroup(groupID = 1337, skip = 0)
		This method will added all your friends into the group
		'''
		while requests.get(MethodsUrls.inviteFriendsUrl.format(groupID, skip), headers = self.headers).json():
			for User in requests.get(MethodsUrls.inviteFriendsUrl.format(groupID, skip), headers = self.headers).json():
				requests.post(MethodsUrls.inviteUrl.format(groupID), data = {
					"routeId": User['routeId']
					}, headers = self.headers)

	def uploadImage(self, path, url = False): # upload image on Ukrainians server
		'''
		Example: uploadImage(path = 'path', url = False)
		Params: set path to folder on your PC if param url = False.
		If url = True, set url to image
		This method will return json object
		'''
		if url:
			uploadImagePayLoads = [
				('images', ('foo.png', requests.get(path).content, 'image/png'))
			]
		else:
			uploadImagePayLoads = [
		        ('images', ('foo.png', open(path, 'rb'), 'image/png'))
			]
		return requests.post(MethodsUrls.imageUploadUrl, files = uploadImagePayLoads, headers = self.headers).json()

	def makeLike(self, postID):
		'''
		Example: makeLike(postID = 1337)
		This method will return json object
		'''
		return requests.post(MethodsUrls.likeURL, data = {
			"contentId": postID,
			"likeType": 0,
			"isLiked": 'false'
			}, headers = self.headers).json() # like

	def makeShare(self, postID, text=''):
		'''
		Example: makeShare(postID = 1337, text = 'hello')
		This method will return json object
		'''
		return requests.post(MethodsUrls.postUrl, data = {
			"sharePostId":postID,
			"text":text,
			"receiverId":requests.post(MethodsUrls.url, data = self.headers).json()['id'],
			"receiverType":0,
			"ownerType":0
			}, headers = self.headers).json() # Share
			
	def wallPost(self, text='', ID = 0, image = ''):
		'''
		Example: wallPost(ID = 1337, text = 'hello')
		This method will return json object
		'''
		if not ID:
			ID = self.usrinfo['routeId']
		receiverType = 0 if ID > 0 else 1
		return requests.post(MethodsUrls.postUrl, data = {
			"receiverId":ID,
			"receiverType":receiverType,
			"ownerType":receiverType,
			"text":text,
			"imagesCacheKey":image['cacheKey'] if image else '',
			"images":[image['files'][0]] if image else '',
			"link":'null'
		}, headers = self.headers).json()
