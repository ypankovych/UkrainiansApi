# Python Ukrainians-Api (obsolete!)

![Python Versions](https://img.shields.io/badge/python-3.x-green.svg)

## All methods:

* addComment
* deleteFriends
* acceptFollower
* getFollowers
* getMessages
* getDialogs
* getFriends
* sendMessage
* searchUsers
* inviteAllFriendsInGroup
* uploadImage
* makeLike
* makeShare
* wallPost
* getMutualFriends
* getGroups
* leaveGroup
* joinGroup
* searchGroups
* setProfilePhoto

# Examples for each method in method documentation.
For get example type:
```python
from UkrainiansApi import searchGroups
print(searchGroups.__doc__)
```
and you'll see this:
```
Example: searchGroups(skip = 50, orderby = 1)
Default this method return 50 groups
Param 'orderby', values: 0 - sort by relevance, 1 - sort by followers count
This method will return json object
```
## How it works:

```python
from UkrainiansApi import Session

sessionObject = Session(userName = 'login', password = 'password')
groups = sessionObject.searchGroups(skip = 0, orderby = 1)['items'][0]
print(groups)
```
__Output:__

```python
{
    'routeId': 32, 
    'name': 'Ukrainians Official', 
    'cover': 'https://produkrainians.blob.core.windows.net/images/32/594bddeab7fa9a178cb5aa1b/community/cover/f3/4735ba6abe.png', 
    'photo': 'https://produkrainians.blob.core.windows.net/images/32/594bddeab7fa9a178cb5aa1b/community/photo/f4/7903c9c962.png',
    'type': 0, 
    'accessType': 0, 
    'counts': {
        'followers': 32669, 
        'posts': 0
        }, 
    'admins': [], 
    'dateOfCreation': '0001-01-01T00:00:00+00:00',
    'score': 0.0, 
    'isDeleted': False, 
    'isBanned': False, 
    'subjectFirst': 1, 
    'subjectSecond': 1, 
    'subjectThird': 5, 
    'follower': 0, 
    'isAdmin': False
}
```

Full [documentation](https://github.com/P-Alban/UkrainiansApi/blob/master/Doc.md)
# Contacts.
* VK: https://vk.com/paveldurmanov
* Telegram: @PavelDurmanov (https://t.me/PavelDurmanov)

__Updates will be in the future.__
