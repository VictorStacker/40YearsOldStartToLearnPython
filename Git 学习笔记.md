# Git 学习笔记

## 什么是Git

- Git是一个开源的**分布式**<u>版本控制</u>系统，用于敏捷高效地处理任何或大或小的项目。



## 安装Git

- 下载Git软件 https://git-scm.com/downloads
- 打开Git软件，然后一直下一步就好 XD



## Git操作指令

- 进入要管理的文件夹，右键菜单选择 Git Bash Here

- 显示版本

  ```
  git --version
  ```

  

- 配置管理信息 (仅需配置一次)

  ```
   git config --global user.email "you@example.com"
   git config --global user.name "Your Name"
  ```

  

- 执行初始化命令

  ```
  git init
  ```

  

- 管理目录下的文件状态

  ```
  got status #检测当前文件匣中的文件状态
  
  #对于新增的文件和修改过后的文件会展示红色标示
  #已经add(进入管理暂存区)的文件为绿色
  ```

  

- 管理指定文件
  ```
  git add 文件名 #单个文件
  git add .     #所有未管理文件(注意有个.)
  ```

  

- 生成版本
  ```
  git commit -m '描述信息'
  ```

  
  
- 查看版本记录

  ```
  git log
  ```






## 进阶指令

- 查看分支
  ```
  git branch
  ```



- 创建分支
  ```
  git branch 分支名称
  ```



- 切换分支
  ```
  git checkout 分支名称
  ```



- 分支合并
  ```
  git merge 要合份的分支
  
  #注意事项，要先切换到主要分支再合并分支
  #可能会产生冲突
  ```



- 删除分支
  ```
  git branch -d 分支名称
  ```



## Git工作流

创建Dev分支，用作于开发，等开放确认后，再合并至 Master分支



## Github代码仓库使用

简易流程：

1. 注册帐号
2. 创建库库
3. 本地代码推送至远程仓库
4. 异地同步



- 创建本地SSH KEY

  ```
  ssh-keygen -t rsa -C "youremail@example.com"
  ```

  然后一路回车即可
  SSH KEY存储在C盘用户名下的.ssh目录里找到id_rsa和id_rsa.pub这两个文件



- 设置Github上的SSH KEY

  1. 登录GitHub，点开右上角头像，下拉选择Settings；

  2. 选择"SSH and GPG KEYS"，点击右上角的"New SSH key"；

  3. 然后Title里面随便填，再把刚才id_rsa.pub里面的内容复制到Title下面的Key内容框里面，最后点击"Add SSH key"，这样就完成了SSH Key的加密。

     

- 关联远程仓库
  ``` 
  git remote add origin https://github.com/XXXXX(仓库地址)
  ```



- 向远程仓库推送代码
  ```
  git push -u origin
  ```



- 复制远程仓库代码至新电脑
  ``` 
  git clone 远程仓库地址 
  ```

  

