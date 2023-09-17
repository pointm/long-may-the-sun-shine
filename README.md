## 这里储存我遇到过的关于GitHub的网络问题的命令
### 上传/克隆443
- 将端口转化到代理服务器，注意代理后面的端口：
  ```
  git config --global http.proxy 127.0.0.1:7890
  git config --global https.proxy 127.0.0.1:7890
  ```
- 取消端口代理
  ``` 
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```
- 查看代理窗口命令
  ```
  git config --global http.proxy #查看git的http代理配置
  git config --global https.proxy #查看git的https代理配置
  git config --global -l #查看git的所有配置
  ```
### VS Code上传非常非常慢
  关闭设置左下角设置-`Use Editor As Commit Input`
### 部分下载加速网址

  git clone https://hub.fastgit.org/pointm/SelfSimilarFractal

  #只下载部分分支
  https://www.itsvse.com/downgit/#/home

  https://down.itsvse.com/tools/fastgit.html
  
  https://blog.csdn.net/weixin_44821644/article/details/107574297?spm=1001.2014.3001.5506

### Git操作详解

[Git操作详解以及在VScode中的使用 - 鬼木士的文章 - 知乎](https://zhuanlan.zhihu.com/p/276376558)


### 更新GitHub Personal Access Token
一个月一次
[GitHub Token](https://github.com/settings/tokens)
```
  Create a GitHub Personal Access Token and copy the token to your clipboard 

  Run git config --global github.accesstoken <token>, replacing <token> with the token from above.
  You can remove the --global option if you want to set the token specifically for your current project.s
```
