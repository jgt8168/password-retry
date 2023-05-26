'''
密碼重試程式
先在程式碼中設定好密碼password='a123456'
讓使用者【最多輸入3次密碼】
不對的話，就印出"密碼錯誤! 還有_次機會"
對的話，就印出"登入成功
'''
password='a123456'

count=3
while count>0:
    user_in=input("請輸入密碼:")
    if user_in==password:
        print("登入成功")
        break
    else:
        count-=1
        print("密碼錯誤! 還有",count,"次機會")