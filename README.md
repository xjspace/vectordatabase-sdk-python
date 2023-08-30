# INSTALL

```sh
pip install wheel
python3 setup.py sdist bdist_wheel || true
pip3 install dist/tcvectordb-0.0.2-py3-none-any.whl
```

# 使用示例
[example.py](example.py)

# 代码分析
部分的解释：

## 导入所需的库和模块，包括time、json、tcvectordb以及一些自定义的异常类和数据类型。

##禁用或启用HTTP请求日志打印。

##创建一个数据库客户端对象，用于连接到腾讯云向量数据库。需要提供数据库的URL、用户名和密钥。

##定义一个名为print_object的函数，用于打印对象。这个函数会遍历对象的每个元素，如果元素具有__dict__属性（即它是一个字典），则以JSON格式打印它；否则，直接打印元素。

##定义一个名为init_db_collction的函数，用于初始化数据库和集合。首先删除已存在的数据库，然后创建一个新的数据库，并列出数据库列表。接着创建一个集合，并为其配置索引。最后，将新创建的集合添加到数据库中，并返回0表示成功。

##定义一个名为upsert_data的函数，用于向集合中插入数据。首先获取集合对象，然后调用upsert方法插入文档。插入完成后，暂停1秒，然后返回0表示成功。

##定义一个名为clear_db_coll的函数，用于清除数据库和集合。首先获取数据库对象和集合对象，然后删除集合。接着删除数据库，并列出数据库列表，最后返回0表示成功。

##定义一个名为query_data的函数，用于查询数据。首先获取数据库对象和集合对象，然后根据不同的查询条件进行查询。查询完成后，打印查询结果，并返回0表示成功。

##在主程序中，依次调用init_db_collction、upsert_data、query_data和clear_db_coll函数，完成数据库和集合的创建、数据的插入、查询和清除操作。
