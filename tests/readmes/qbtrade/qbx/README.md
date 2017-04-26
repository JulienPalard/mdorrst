# upload to pypi
写好setup.py文件后，执行<center>`python setup.py sdist bdist_wininst upload`</center >
就可以上传到pypi服务器，执行命令后要求输入username和password。
有时候会出现bug，password验证不通过就需要配置~/.pypirc文件，格式如下  
```
[distutils]
index-servers =
    pypi
	
[pypi]
repository: https://pypi.python.org/pypi
username = <username>
password = <password>
```
配置完执行命令就会自动验证。