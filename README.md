## 这里储存我遇到过的奇奇怪怪的问题
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
- 有时候ZOTERO的茉莉花脚本会无法正常的爬取文献，或者到了文献页面结果添加的是快照。在检查完其它的配置均没有问题，并且在官网更新完了浏览器的插件以及本地ZOTERO应用之后可以考虑修复ZOTERO的翻译器（Translators）。

- 相应的翻译器仓库与下载位置：
https://github.com/l0o0/translators_CN

- 在下载并且安装完自己需要的翻译器之后记得回到浏览器的ZOTERO脚本里面更新翻译器。具体的更新方法就是邮件浏览器ZOTERO图标，选择扩展选项->Advanced->Translators把里面的`Update Translators`和`Reset Translators`都点一下，然后重启浏览器。

## python使用清华源进行下载的方法
[参考网址在这里](https://zhuanlan.zhihu.com/p/129866307)

具体的指令的话：
```python
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## python 如何无损耗的将字符串转化为浮点数或者长浮点数？
[转换方法在此](https://www.delftstack.com/zh/howto/python/how-to-convert-string-to-float-or-int/#%E5%9C%A8-python-%E4%B8%AD%E9%80%9A%E8%BF%87-astliteral_eval-%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E4%B8%BA-float-%E6%88%96-int)
`ast.literal_eval(string) `安全地评估包含 `Python` 表达式的给定字符串。它可以将字符串自动地转换为 `float` 或 `int`。

## matplotlib 如何正确的显示中文
[正确的显示中文的方法](https://zhuanlan.zhihu.com/p/345605782)

[附赠Consolas-with-Yahei仓库](https://github.com/crvdgc/Consolas-with-Yahei/tree/master)

[如何刷新matplotlib里面的字体缓存文件?](https://blog.csdn.net/qq_57313910/article/details/126733257)
具体方法就是找到我想要的字体文件，加入matplotlib的字体库
```python
import matplotlib
print(matplotlib.matplotlib_fname()) # 字体库路径    
```
之后将配置文件的取消`font.family`的注释，并在`font.sans-serif`中添加自己想要的字体名称部分注释给去掉，最后将自己想要的字体添加到字体库里面。

最后记得清空matplotlib的缓存文件，具体代码：
```python
import shutil
import matplotlib

shutil.rmtree(matplotlib.get_cachedir())
```
## py如何引用上级目录中的文件
```python
# 获取当前文件的上级目录
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将上级目录添加到sys.path中
sys.path.append(parent_dir)

# 现在你可以导入上级目录下的模块了
from Modeling import *
```

## python 安装路径与pip路径以及如何完全卸载
cmd里面直接输入即可。展示python安装路径
```cmd
where python
```
展示pip了多少包，以及展示安装包的位置：
```
pip list
```
[如何完全卸载python](https://blog.csdn.net/qq_38463737/article/details/107205696)
主要是找到C盘缓存里面的`pip`和`python`的文件夹，缓存路径是`%USERPROFILE%\AppData\Local`

## conda基本问题
[常用conda命令合集](https://zhuanlan.zhihu.com/p/363904808)
```python
conda create -n environment_name python=3.11.5 #创建conda环境
conda activate environment_name # 进入环境	
conda deactivate # 退出环境	
conda remove -n yourname --all # 删除环境	 
conda env list / conda info -e # 列出环境	
conda create --name new_env_name --clone old_env_name # 复制环境	
```

## 关于python类的初始化
`python`对于类，有自己的初始化方法`__init__`。相比于自己定义一个初始化类，这个方法初始化的类的特点是，其被实例化初始化后，实例化之后的类之间不会发生互相干扰的情况。下面以一个例子来对这个初始化方法进行简要的介绍。
```python
class Rectangular:
    a = 1
    b = 1
    area = 1

    def init(self, LongSideLength, ShortSideLength):
        self.a = LongSideLength
        self.b = ShortSideLength
        self.area = self.a * self.b
        return self


rectest = Rectangular()
rec1 = rectest.init(11, 8)
rec2 = rectest.init(20, 6)
```
这一段我们定义了一个矩形相关的类，其储存了三个属性，分别是矩形的长边、短边和面积。而面积这个属性是由长边与短边做乘法而得到的。代码最开始针对这个类进行了实例化，之后分别有两个不同的实例化后的类进行了不同的初始化。在我们运行所有的代码之后，我们会发现原先的`rec1`的属性变得跟`rec2`的属性完全相同。因为两个类的名字其实指向的是同一个实例化 的类。这样子的话改变其中的某一个另外所有的类都会发生变化。
我们现在使用预设的`__init__`这个方法来对原先的矩形进行初始化：
```python
class Rectangular:
    def __init__(self, LongSideLength, ShortSideLength):
        self.a = LongSideLength
        self.b = ShortSideLength
        self.area = self.a * self.b


rec1 = Rectangular(11, 8)
rec2 = Rectangular(20, 6)
```
我们会发现这样子初始化之后的类，`rec2`的参数跟`rec1`的参数是完全不一样的，改变`rec2`并不会影响`rec1`
我们现在知道，`__init__`会直接返回这个实例化的对象本身，并不需要其它的方法来对类进行进一步的返回操作，现在的代码可以被写作：
```python
class Rectangular:
    def __init__(self, LongSideLength, ShortSideLength):
        self.a = LongSideLength
        self.b = ShortSideLength
        self.area = self.a * self.b


rec1 = Rectangular(11, 8).returnmyself()
rec2 = Rectangular(rec1.a, 12)
```
我们在创建`rec2`的时候就能调用`rec1`的参数了，也就是说这个矩形`rec2`的长边和`rec1`的长边是完全相同的（智将）
## 关于python可变对象的`.copy`方法和直接赋值的区别
在可变对象中使用创建副本/`.copy`方法来创建副本和不可变对象完全不同，下面是可变对象（例子是字典，但是其实还有列表和集合）的一个例子。
- 当你使用`.copy()`方法时，你创建的是原字典的**浅拷贝**。这意味着，如果你修改了新字典中的一个可变对象，那么在原字典中的相应对象也会被修改。但是，**如果你向新字典添加、删除或修改一个键值对，这个改变不会影响到原字典。**

- 当你直接赋值时，你实际上只是创建了一个新的引用，而不是一个新的对象。这意味着，两个字典变量实际上指向的是同一个字典，所以对任何一个字典的修改都会影响到另一个字典。

```python
# 使用dict.copy()创建浅拷贝
dict1 = {"key": ["value"]}
dict2 = dict1.copy()
dict2["key"].append("value2")  # 修改新字典中的列表
print(dict1)  # 输出：{'key': ['value', 'value2']}
dict2["new_key"] = "new_value"  # 向新字典添加一个键值对
print(dict1)  # 输出：{'key': ['value', 'value2']}，并没有"new_key"

# 直接赋值创建引用
dict3 = {"key": ["value"]}
dict4 = dict3
dict4["key"].append("value2")  # 修改新字典中的列表
print(dict3)  # 输出：{'key': ['value', 'value2']}
dict4["new_key"] = "new_value"  # 向新字典添加一个键值对
print(dict3)  # 输出：{'key': ['value', 'value2'], 'new_key': 'new_value'}，有"new_key"
```

在这个例子中，你可以看到，使用`.copy()`方法和直接赋值得到的结果是不同的。

深拷贝可以使用`.deepcopy()`，对副本的影响完全不会影响到原本。

但是如果你是一个不可变对象（例如整数、字符串和元组），使用直接赋值来创建原变量的副本，修改副本时候并不会影响到原本的数值。
```python
# 对于不可变对象
a = 1
b = a
a = 2
print(a)  # 输出：2
print(b)  # 输出：1

# 对于可变对象
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # 输出：[1, 2, 3, 4]
print(list2)  # 输出：[1, 2, 3, 4]
```