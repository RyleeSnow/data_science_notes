# 如何在本地浏览器使用 Jupyter Notebook 连接远程服务器/虚拟机

环境：

- MacBook / PC
- 系统版本：macOS Monterey / Windows 10
- 虚拟机系统：linux Ubuntu 18

## 第一步：在远程机和本地都安装 jupyter-notebook

```linux
pip install jupyter
```

## 第二步：在远程机上运行 jupyter-notebook

```linux
jupyter notebook password  # 建议提前设置好密码，一台主机设置好密码后不需要重复设置
jupyter notebook --no-browser --port=8889
```

## 关键！第三步：在本地 terminal 运行命令行

```linux
ssh -N -f -L localhost:8888:localhost:8889 username@your_remote_host_name

# 比如
ssh -N -f -L localhost:8888:localhost:8889 my_name@0.0.0.0
```

## 第四步：打开本地浏览器进入“https://localhost:8888”（如果需要，输入Jupyter密码）
