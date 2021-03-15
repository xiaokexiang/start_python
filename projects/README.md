### command
- 生成虚拟环境
```python 
python3 -m venv ${venv name}
```
-  基于当前环境生成requirements.txt 
```shell script
pip3 freeze > ./requirements.txt
```
- django新建项目
```shell script
django-admin startproject ${project_name} .
```

- django创建数据库

```python3
python3 manage.py migrate
```

- django运行服务在指定端口号（不写默认8000）
```python3
python3 manage.py runserver ${port}
```