# Enjoy 使用说明

这是一款**静态下载网站**生成工具。意思就是说，您可以将生成好的静态网站发布在 `Github Pages` 或 `Netlify` 等静态网站托管平台上。这是一个在线的 DEMO：

[下载站 (pandaoxi.github.io)](https://pandaoxi.github.io/enjoy-WebsiteMaker/)

目前界面比较简陋（~~其实是因为我不会写网页啊 QWQ~~），可以从网上找喜欢的样式。您可以根据自己的需要编辑 `template.html` 模板文件，只要包含以下的关键字即可：

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<style>...</style>
		<title>%s</title>							<!--标题-->
	</head>
	<body>
		<h1>%s 的索引</h1>							  <!--索引-->
		<hr><br>
		%s											<!--文件区-->
		<br><hr><br>
		%s											<!--README 区-->
	</body>
	
</html>
```

这里我已经将各个 `%s` 的作用写出来了。如果您不想要某些关键字的话，可以使用 HTML 注释掉，这里不再赘述。



程序的用了 Python，如果您需要用 GUI 辅助操作，请安装依赖包：

```
pip install easygui
```

推荐在 Windows 上操作，在别的系统上不知道会出现什么 BUG。

如果您想直接从 Python 使用 Enjoy，可以在同文件夹下使用包的形式导入其中的类 `MakeTree`。

代码：

```python
from enjoy import MakeTree
mt = MakeTree()
```

可以修改其中的一些参数，例如：

```python
mt.temp = "<你想要修改的临时路径>"
mt.tl = "<你想要更换的模板（必须遵从上面的关键字）>"
```

```python
mt.copyPath("<会把这个地方的文件复制到 mt.temp 中>")
mt.makeIndex(oldPath = "<您想要生成索引的路径>", data={"title":"<HTML的标题>", "README":{"type":"<填写markdown或者其他的（会直接显示）>", "code":"<就是下面的那个说明>"}})
```

单独地，您可以在文件夹下创建 `README.md`，只要程序发现将会优先按照其中的说明；没有此文件的文件夹将会使用 `makeIndex` 参数中的说明。

另外，由于 Github 可能不支持一些文件夹的名称，也可能有重名的，请仔细检查。

完成后，您可以在 `mt.temp` 的位置找到已经生成索引的文件夹，直接拖到仓库里最后配置静态网页即可。
