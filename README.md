## 关于调用亚马逊api的方法的封装，版本==v2

配置**config.py**中的信息，包括开发者信息，地区等信息

获取授权

## 1、获取授权url

```python
from auth import BaseAuth

ba = BaseAuth()

print(ba.get_grant_url())
```

点进这个url后用自己的店铺登录后看到网址信息上有个**code=xxxx**,这个code就是我们所需要的

## 2、获取 access_token 和refresh_token

```python
print(ba.get_refresh_token(code))
```

通过该方法得到**access_token**和**refresh_token**，将这个**refresh_token**保存到自己的记事本中，可永久使用

**access_token**是有有效期的，如果要获得新的**access_token**可以直接

```python
print(ba.get_new_access_token(refresh_token))
```

## 3、获取 profile

将上一步的**access_token**复制下来，通过该方法得到你的店铺的**profileId**

```python
from profiles import Profiles

profile = Profiles(access_token)

print(profile.get_profiles())
```
