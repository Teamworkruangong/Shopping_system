import jsonpickle


def getLoginUserInfo(request):
    """获取登录用户对象信息"""
    user = request.session.get('user','')
    print(user)
    if user:
        user = jsonpickle.loads(user)
        # print(user)


    return {'loginUser':user}