# flask-seed

### 运行方法：

```sh
python app.py runserver -h 0.0.0.0 -p 8080
```

> 生产环境下，需要将环境变量 ENV_MODE 设为 PROD，来禁用 DEBUG 模式。

### 构建方法

```sh
python app.py assets build  --parse-templates
python app.py assets clean  --parse-templates
python app.py assets watch  --parse-templates
```

> 构建这一步不是必须的，如果你的应用非常大，那么可以提前构建一下，以免影响服务器吐出页面的速度。