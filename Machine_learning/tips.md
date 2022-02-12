##### jupyter 配置虚拟环境
1. 在主环境执行 conda install nb_conda  
2. 进入虚拟环境 conda activate py2  
3. 执行 conda install nb_conda  即可在jupyter上刷新出现要的kernel  
4. 退出虚拟环境 conda deactivate

##### Jupyter中删除虚拟环境步骤
1. 查看安装了哪些虚拟环境kernel（在base或虚拟环境下运行都可以）：jupyter kernelspec list
2. 删除指定的kernel：jupyter kernelspec uninstall myenv

##### 用复制的办法重命名conda虚拟环境
1. 复制一个 conda create -n conda-new --clone conda-old
2. 删除旧的 conda remove -n conda-old --all

##### github网站下载上传代码速度太慢  
```fatal: unable to access 'https://github.com/xxxx.git/': OpenSSL SSL_connect: Connection was reset in co nnection to github.com:443```
有可能是因为github的IP地址更新了，手动更新即可。
https://blog.csdn.net/z1026544682/article/details/86635367  

##### jupyter上matplotlib的使用(结合官方文档食用)
https://blog.csdn.net/weixin_42042680/article/details/80738699
https://matplotlib.org/

##### excel转markdown（格式转换器）
`https://tableconvert.com/`

##### 常见的文件夹环境变量
| %ALLUSERSPROFILE%         | C:\ProgramData                 |
|---------------------------|--------------------------------|
|                           |                                |
| %APPDATA%                 | C:\Users\用户名\AppData\Roaming   |
|                           |                                |
| %COMMONPROGRAMFILES%      | C:\Program                     |
|                           |                                |
| %COMMONPROGRAMFILES(x86)% | C:\Program                     |
|                           |                                |
| %COMSPEC%                 | C:\Windows\System32\cmd.exe    |
|                           |                                |
| %HOMEDRIVE%和%SystemDrive% | C:\                            |
|                           |                                |
| %HOMEPATH%                | C:\Users\用户名                   |
|                           |                                |
| %LOCALAPPDATA%            | C:\Users\用户名\AppData\Local     |
|                           |                                |
| %PROGRAMDATA%             | C:\ProgramData                 |
|                           |                                |
| %PROGRAMFILES%            | C:\Program Files               |
|                           |                                |
| %PROGRAMFILES(X86)%       | C:\Program Files (x86)         |
|                           |                                |
| %PUBLIC%                  | C:\UsersPublic                 |
|                           |                                |
| %SystemRoot%              | C:\Windows                     |
|                           |                                |
| %TEMP%和%TMP%              | C:\Users\用户名\AppData\LocalTemp |
|                           |                                |
| %USERPROFILE%             | C:\Users用户名                    |
