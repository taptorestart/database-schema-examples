# Database Schema to excel

## Test Environments
Python v3.8.2
MacOS v12.2.1

## Install
```shell
$ python3 -m venv venv
$ soruce ./venv/bin/activate
$ pip install -r requirements.txt
```

## Input your database configurations.
```python
username = 'username'
password = 'verysecret'
host = 'db_host'
port = 3306 
database = 'db_name'
```

## Run
```shell
$ python database_schema_to_excel.py 
```
