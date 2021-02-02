Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data=input('enter the any kind of data')
if data<='a' and data>='z' or data>="z" and data<='z':
    print(data,'alphabet')
elif data>'0' and data<='9':
    print(data,'is digit')
else:
    print(data,'special character')
