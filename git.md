#### 如果 git clone 的时候，使用的是 "https://" 而不是 "git@git"，就会导致 git pull/push 的时候，需要重复输入账号和密码。解决方法：

```bash
git config --global credential.helper store
```

#### 远程和本地冲突，重置：

```bash
git fetch --all
git reset --hard origin/main
git pull
```
