# flask-seed

### 安装依赖

```sh
pip install -r reuqirements.txt

npm i -g less
```

`less` 用于编译CSS（或LESS）。

### 运行方法：

```sh
python app.py runserver -h 0.0.0.0 -p 8080
```

生产环境下，需要将环境变量 ENV_MODE 设为 PROD，来禁用 DEBUG 模式。

### 离线压缩

```sh
python app.py jac
```

当你将应用部署到生产环境的服务器时，需要进行离线压缩，这样做有两个作用：

* 离线压缩后，就无需服务器响应时的临时编译了，提高了速度。另外，当你在开发过程中，觉得响应太慢时，也可以先进行离线压缩，这样服务器响应就快了。
* 当你将应用部署在多台服务器中时，就必须进行离线压缩，这样可以保证每台服务的静态资源链接是相同的，从而不会导致404错误。