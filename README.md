# BlueboxPanelMonitor
使用前请下载 chrome 驱动，驱动详情：http://blog.csdn.net/chaomaster/article/details/52963265 

使用脚本前必须创建配置文件（文件名 config.ini）,且需要将配置文件和脚本放在同一目录。必须使用 config.ini 作为文件名 

脚本使用前请确定已安装 python 2.7 以及 slenium 框架, 故不再做二进制版本支持

由于 bluebox 登录需要使用 yubkey ，因此脚本会打开网页自动填入配置文件中的用户名和密码，但是会等待 yubkey 的输入

# 配置文件 config.ini 样例
```
[info]
username = xxxx@xxxx.com
password = xxxxxx
driverpath = /Users/ABC/DEF/XXXX/chromedriver
audiopath = file:///Users/ABC/Desktop/1234.mp3
```
