# coding: utf8
__author__ = 'Alban'
import requests

class Session:

	# Do not modify this urls!
	userSearchUrl = 'https://api.ukrainians.co/v1/search?cityId={0}&countryId{1}0&gender={2}&isOnline={3}&maxAge={4}&minAge={5}&relationship={6}&schoolId={7}&skip={8}&top={9}&universityId={10}&value='
	inviteUrl = 'https://api.ukrainians.co/v1/community/invite/{}'
	inviteFriendsUrl = 'https://api.ukrainians.co/v1/community/inviteFriends/{}?skip={}'
	imageUploadUrl = 'https://api.ukrainians.co/v1/post/uploadimages'
	url = 'https://api.ukrainians.co/v1/token'
	postUrl = 'https://api.ukrainians.co/v1/post/add'
	likeURL = 'https://api.ukrainians.co/v1/like'
	sendMsgUrl = 'https://api.ukrainians.co/v1/messenger/send'
	getFriendsUrl = 'https://api.ukrainians.co/v1/contacts/friends?isCounts=false&isUser=true&online=false&routeId={}&skip={}'
	getDialogsUrl = 'https://api.ukrainians.co/v1/dialog/get?skip=0'
	getMessageUrl = 'https://api.ukrainians.co/v1/messenger/get?dialogId={}&skip=0'
	getFollowersUrl = 'https://api.ukrainians.co/v1/contacts/followers?isUser=true&routeId={}&skip={}'
	acceptFollowersUrl = 'https://api.ukrainians.co/v1/contacts/accept'
	deleteFriendUrl = 'https://api.ukrainians.co/v1/contacts/delete'
	commentAddUrl = 'https://api.ukrainians.co/v1/comment/add'

	def __init__(self, userName, password):
		self.AuthPL = {
			'grant_type': 'password',
			'userName': userName, 
			'password': password
		}
		self.usrinfo = requests.post(Session.url, data = self.AuthPL).json()
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
			'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4,uk;q=0.2',
			'Authorization': 'bearer ' + self.usrinfo['access_token']
		}

	def addComment(self, postID, text):
		'''
		Example: addComment(postID = 'post_id', text = 'Hello world')
		This method will return json object
		'''
		return requests.post(Session.commentAddUrl, data = {
			"contentType":0,
			"contentId":postID,
			"text":text}, headers = self.headers).json()

	def deleteFriends(self, userID):
		'''
		Example: deleteFriends(userID = 1337)
		This method will return json object
		'''
		return requests.post(Session.deleteFriendUrl, data = {
			"routeId": userID
			}, headers = self.headers).json()

	def acceptFollower(self, userID):
		'''
		Example: acceptFollower(userID = 1337)
		This method will return json object
		'''
		return requests.post(Session.acceptFollowersUrl, data = {
			"routeId": userID
			}, headers = self.headers).json()

	def getFollowers(self, skip = 0):
		'''
		Example: getFollowers()
		This method will return json object
		This method will return 20 followers, for get more, set the skip param
		'''
		return requests.get(Session.getFollowersUrl.format(self.usrinfo['routeId'], skip), headers = self.headers).json()

	def getMessages(self, userID):
		'''
		Example: getMessages(userID = 1337)
		This method will return json object
		'''
		return requests.get(Session.getMessageUrl.format(userID), headers = self.headers).json()

	def getDialogs(self):
		'''
		Example: getDialogs()
		This method will return json object
		This method will return 20 dialogs, for get more, set the skip param
		'''
		return requests.get(Session.getDialogsUrl, headers = self.headers).json()

	def getFriends(self, userID = None, skip = 0): # return 20 friends without offset
		'''
		Example: getMessages(userID = 1337)
		This method will return json object
		This method will return 20 friends, for get more, set the skip param
		'''
		if userID is None:
			userID = self.usrinfo['routeId']
		return requests.get(Session.getFriendsUrl.format(userID, skip), headers = self.headers).json()

	def sendMessage(self, ID, text):
		'''
		Example: sendMessage(userID = 1337, text = 'hello')
		This method will return json object
		'''
		return requests.post(Session.sendMsgUrl, data = {"text":text,
			"dialogId":ID}, headers = self.headers).json()

	def searchUsers(self, sex = 0, city = 0, country = 0, online = 'false', relationship = 0, maxage = 100, minage = 0, skip = 0, school = 0, universityId = 0, top = 40):
		'''
		Params: sex, city, country, online, relationship, maxage, minage, skip, school, universityId, top 
		Example: searchUsers(sex = 0, city = 0, country = 0, online = 'false', relationship = 0, maxage = 100, minage = 0, skip = 0, school = 0, universityId = 0, top = 40)
		This method will return json object
		'''
		return requests.get(Session.userSearchUrl.format(
			city, country, sex, online, maxage, minage, relationship, school, skip, top, universityId), headers = self.headers).json()

	def inviteAllFriendsInGroup(self, groupID, skip = 0):
		'''
		Example: inviteAllFriendsInGroup(groupID = 1337)
		This method will added all your friends into the group
		'''
		while requests.get(Session.inviteFriendsUrl.format(groupID, skip), headers = self.headers).json():
			for User in requests.get(Session.inviteFriendsUrl.format(groupID, skip), headers = self.headers).json():
				requests.post(Session.inviteUrl.format(groupID), data = {
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
		return requests.post(Session.imageUploadUrl, files = uploadImagePayLoads, headers = self.headers).json()

	def makeLike(self, postID):
		'''
		Example: makeLike(postID = 1337)
		This method will return json object
		'''
		return requests.post(Session.likeURL, data = {
			"contentId": postID,
			"likeType": 0,
			"isLiked": 'false'
			}, headers = self.headers).json() # like

	def makeShare(self, postID, text=''):
		'''
		Example: makeShare(postID = 1337, text = 'hello')
		This method will return json object
		'''
		return requests.post(Session.postUrl, data = {
			"sharePostId":postID,
			"text":text,
			"receiverId":requests.post(Session.url, data = self.headers).json()['id'],
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
		return requests.post(Session.postUrl, data = {
			"receiverId":ID,
			"receiverType":receiverType,
			"ownerType":receiverType,
			"text":text,
			"imagesCacheKey":image['cacheKey'] if image else '',
			"images":[image['files'][0]] if image else '',
			"link":'null'
		}, headers = self.headers).json()