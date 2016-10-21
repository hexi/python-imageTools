# python-imageTools
git clone git@github.com:baidao/python-imageTools.git

mac环境下安装python3
没有brew先安装brew
brew install python3

cd python-imageTools

pip3 install Pillow

pip3 install --upgrade tinify

##自动压缩图片
python3 /Users/hexi/Documents/python-demo/imageTools/CompressImage.py [目标路径]
###`注意`
	1. 不带参数就是当前路径
	2. 目前图片压缩用的是TinyPNG的工具，需要去网站申请key，https://tinypng.com/developers。
	3. 拿到key之后需要修改CompressImage.py的'tinify.key'为自己的key。
	4. 如果谁知道怎么通过python完成图片的压缩，并告诉我，将非常感谢。

##查找重复图片
python3 /Users/hexi/Documents/python-demo/imageTools/diffImage.py [目标路径]
