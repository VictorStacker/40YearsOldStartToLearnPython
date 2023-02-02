# Git 学习笔记

### 什么是Git

- Git是一个开源的**分布式**<u>版本控制</u>系统，用于敏捷高效地处理任何或大或小的项目。

### 安装Git

- 下载Git软件 https://git-scm.com/downloads
- 然后一直下一步就好 XD



### Git操作指令

- 进入要管理的文件夹，右键菜单选择 Git Bash Here

- 显示版本

  ```
  git --version
  ```

- 执行初始化命令

```
git init
```

- 管理目录下的文件状态

```
got status

#新增的文件和修改过后的文件会展示红色
```

- 管理指定文件

```
git add 文件名 #单个文件
git add .     #所有文件(注意有个.)
```

配置管理信息 (仅需配置一次)

```
 git config --global user.email "you@example.com"
 git config --global user.name "Your Name"
```

- 生成版本
  ```
  git commit -m '描述信息'
  ```

- 查看版本记录

  ```
  git 
  ```

  