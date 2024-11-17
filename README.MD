# 注意事项
由于`manim 0.18.0`的CE版本的重构，所以说此时的`Manim`并不能像以前，直接创建`anaconda3`环境之后使用以下语句直接进行安装:
```python
pip install manim
```
这样子做的话会出现报错，无法正常安装，如果想要正常安装的话请搜索`manim conda`，在官方文档里面寻找`conda`平台的`manim`安装方法，现在的链接大概位于[这里](https://docs.manim.community/en/stable/installation/conda.html)

具体的语句是，在`conda activate <your_env_name>`进入所需要的`conda`环境之后，使用语句:
```conda
conda install -c conda-forge manim
```
进行安装，切记~