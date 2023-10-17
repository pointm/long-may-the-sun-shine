## 这里储存我遇到过的奇奇怪怪的网页问题
### 上传/克隆443
- 将端口转化到梯子的代理服务器，如果一直挂着梯子的话这种设置方法更快。
  注意代理后面的端口，应该于自己的梯子的代理端口一致，Windows11的具体的梯子的代理端口可以通过在设置页面搜索`代理服务器设置->点击手动设置代理的编辑按钮`查看：
  命令行输入以下命令：
  ```
  git config --global http.proxy 127.0.0.1:7890
  git config --global https.proxy 127.0.0.1:7890
  ```
如果没有梯子的话就用这种方法，取消端口代理：
- 取消端口代理
  ``` 
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```
不知道自己是否设置了端口代理？命令行输入以下命令查看详细情况：
- 查看代理窗口命令
  ```
  git config --global http.proxy #查看git的http代理配置
  git config --global https.proxy #查看git的https代理配置
  git config --global -l #查看git的所有配置
  ```
### VS Code上传非常非常慢
  关闭设置左下角设置-`Use Editor As Commit Input`
### GitHub部分下载加速网址

  - git clone https://hub.fastgit.org/pointm/SelfSimilarFractal  

    https://down.itsvse.com/tools/fastgit.html
    
    https://blog.csdn.net/weixin_44821644/article/details/107574297?spm=1001.2014.3001.5506

  - 这个网址可以只下载文件中的部分分支子文件夹：
  https://www.itsvse.com/downgit/#/home

### Git操作详解

[Git操作详解以及在VScode中的使用 - 鬼木士的文章 - 知乎](https://zhuanlan.zhihu.com/p/276376558)


### 更新GitHub Personal Access Token
如果VS CODE里面编辑自己的分支仓库的时候一直输入账号密码提示错误试试把密码换成GitHub Personal Access Token？
记得这个TOKEN 会强制一个月手动更新一次

Token更新方法，安装好git后命令行输入：
```
git config --global github.accesstoken <输入你的token，记得删掉尖括号>
```
[GitHub Token设置地址](https://github.com/settings/tokens)
```
  Create a GitHub Personal Access Token and copy the token to your clipboard 

  Run git config --global github.accesstoken <token>, replacing <token> with the token from above.
  You can remove the --global option if you want to set the token specifically for your current project.s
```
## 每次pull/push都要输入密码
- 首先进入你的git 工作目录下。
- 在终端执行一下命令：
``` 
  git config --global credential.helper store
```
- 然后再重新执行一次git pull,这次它还是提示你输入账号和密码，再输入密码就好了

## 同步文件显示fatal: HttpRequestException encountered.

因为GitHub的认证文件过期了，我们需要用新的认证文件
[认证文件仓库地址在这里，下载Release即可](https://github.com/microsoft/Git-Credential-Manager-for-Windows/tree/v1.14.0)

## ZOTERO翻译器抽风
有时候ZOTERO的茉莉花脚本会无法正常的爬取文献，或者到了文献页面结果添加的是快照。在检查完其它的配置均没有问题，并且在官网更新完了浏览器的插件以及本地ZOTERO应用之后可以考虑修复ZOTERO的翻译器（Translators）。

相应的翻译器仓库与下载位置：
https://github.com/l0o0/translators_CN

在下载并且安装完自己需要的翻译器之后记得回到浏览器的ZOTERO脚本里面更新翻译器。具体的更新方法就是邮件浏览器ZOTERO图标，选择扩展选项->Advanced->Translators把里面的`Update Translators`和`Reset Translators`都点一下，然后重启浏览器。

## python使用清华源进行下载的方法
[参考网址在这里](https://zhuanlan.zhihu.com/p/129866307)

具体的指令的话：
```python
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```