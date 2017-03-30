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
# chrome 驱动详情
chrome 与 chromedriver 版本映射表  （表格转载自http://blog.csdn.net/huilan_same/article/details/51896672）：
```
chromedriver版本	    支持的Chrome版本
v2.27	            v54-56
v2.26	            v53-55
v2.25	            v53-55
v2.24	            v52-54
v2.23	            v51-53
v2.22	            v49-52
v2.21	            v46-50
v2.20	            v43-48
v2.19	            v43-47
v2.18	            v43-46
v2.17	            v42-43
v2.13	            v42-45
v2.15	            v40-43
v2.14	            v39-42
v2.13	            v38-41
v2.12	            v36-40
v2.11	            v36-40
v2.10	            v33-36
v2.9	            v31-34
v2.8	            v30-33
v2.7	            v30-33
v2.6	            v29-32
v2.5	            v29-32
v2.4	            v29-32
```
