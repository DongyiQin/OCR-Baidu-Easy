# OCR-Text
百度OCR调用，实现图片到文字的识别。
首先在百度AI创建一个应用，创建后会获得如下信息：
APP_ID = '******'
API_KEY = '************'
SECRET_KEY = '**************'

下面就是百度API包的安装，在终端cmd输入如下语句直接pip方式安装，注意是 baidu-api 哦！
pip install baidu-aip
接下来运行BaiduOCR.py代码，图片修改为你的图片就可以直接运行了。

这里还提供了普通OCR方法的代码，使用前需要安装pytesseract包：
pip install pytesseract
还需要下载这里提供的tesseract文件，代码中的
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dell\Desktop\tesseract\Tesseract-OCR\tesseract.exe'改为你自己存储的地址。
