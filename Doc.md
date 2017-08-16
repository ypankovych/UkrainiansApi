* __Make session:__

```python
from UkrainiansApi import Session
ApiSession = Session(userName = 'Login', password = 'Password')
```
* __addComment.__ This method adds a comment to the post.
  * __Example:__
  ```python
  ApiSession.addComment(postID = '598dd6830a93f2532cd4b080', text = 'Hello World!')
  ```
* __deleteFriends.__ This method will delete your friends.
  * __Example:__
  ```python
  ApiSession.deleteFriends(userID = 1337)
  ```
* __acceptFollower.__ This method will accept your follower.
  * __Example:__
  ```python
  ApiSession.acceptFollower(userID = 1337)
  ```
* __getFollowers.__ This method will return your followers.

  This method will return 20 followers, for get more, set the skip param
  * __Example:__
  ```python
  ApiSession.getFollowers(userID = 1337, skip = 0)
  ```
* __getMessages.__ This method will return your messages.
  * __Example:__
  ```python
  ApiSession.getMessages(userID = 1337)
  ```
* __getDialogs.__ This method will return your dialogs.
  * __Example:__
  ```python
  ApiSession.getDialogs()
  ```
* __getFriends.__ This method will return your friends.

  This method will return 20 friends, for get more, set the skip param
  * __Example:__
  ```python
  ApiSession.getFriends(userID = 1337, skip = 0)
  ```
* __sendMessage.__ This method will send the message.
  * __Example:__
  ```python
  ApiSession.sendMessage(userID = 1337, text = 'hello')
  ```
* __searchUsers.__ This method will return found users.
  * __Example:__
  ```python
  ApiSession.searchUsers(sex = 0, city = 0, country = 0, online = 'false', relationship = 0, maxage = 100, minage = 0, skip = 0, school = 0, universityId = 0, top = 40)
  ```
* __inviteAllFriendsInGroup.__ This method will added all your friends into the group.
  * __Example:__
  ```python
  ApiSession.inviteAllFriendsInGroup(groupID = 1337, skip = 0)
  ```
* __uploadImage.__ This method will upload image on Ukrainians server.
  If url = True, set url to image
  * __Example:__
  ```python
  ApiSession.uploadImage(path = 'path', url = False)
  ```
* __makeLike.__
  * __Example:__
  ```python
  ApiSession.makeLike(postID = 1337)
  ```
* __makeShare.__
  * __Example:__
  ```python
  ApiSession.makeShare(postID = 1337, text = 'hello')
  ```
* __wallPost.__
  * __Example:__
  ```python
  ApiSession.wallPost(ID = 1337, text = 'hello')
  ```
