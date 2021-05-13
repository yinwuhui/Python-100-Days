"""
copyright@yinwuhui
version:1.0
date:2021.05.13
modify infor: first create
"""

#一个简单的登录验证函数

def login(usr,paswd):
    if usr == "yinwuhui" and paswd == "wuhui7245840":
        return True
    elif usr == "root" and paswd == "123456":
        return True
    else:
        return False

def main():
    ret = False
    username = input('请输入用户名:')
    password = input('请输入用户密码:')
    ret = login(username, password)
    if False == ret:
        print("登录失败！")
    else:
        print("登录成功！")

if __name__ == '__main__':
    main()