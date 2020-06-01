## 关于调用亚马逊api的方法的封装，版本==v2

配置config.py中的信息，包括开发者信息，地区等信息

获取授权

## 1、获取授权url

```python
from auth import BaseAuth

ba = BaseAuth()

print(ba.get_grant_url())
```

#点进这个url后用自己的店铺登录后看到网址信息上有个code=xxxx,这个code就是我们所需要的

## 2、获取 access_token 和refresh_token

```python
print(ba.get_refresh_token(code))
```

#通过该方法得到access_token和refresh_token，将这个refresh_token保存到自己的记事本中，可永久使用

#access_token是有有效期的，如果要获得新的access_token可以直接

```python
print(ba.get_new_access_token(refresh_token))
```

## 3、获取 profile

将上一步的access_token复制下来，通过该方法得到你的店铺ID

```python
from profiles import Profiles

profile = Profiles(access_token)

print(profile.get_profiles())
```
