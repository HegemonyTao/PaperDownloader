# 文献搜索与批量下载

本项目使用[谷歌学术](https://scholar.google.com.hk/?hl=zh-CN)进行文献搜索，使用[SCI-HUB](https://sci-hubtw.hkvisa.net/)进行文献下载。目前可实现仅通过输入关键字便可获取所有相关文献的描述信息（标题、链接、摘要以及被引用数等信息）以及文献下载

## 安装

本项目完全使用python编写，你可以通过如下方式安装：

```python
git clone https://github.com/HegemonyTao/PaperDownloader.git
cd PaperDownloader
python -m pip install --user -r requirements.txt
```

## 用法

### 文献检索

本项目采用[谷歌学术](https://scholar.google.com.hk/?hl=zh-CN)作为搜索引擎，通过输入关键字来获取到文献的描述信息。默认情况下，会采集到检索到的全部文献，并将它们的信息保存在目录[PaperInfo](./data/PaperInfo)中。在根目录下，可采用如下方式进行文件检索：

```python
python GoogleScholar.py --keyword "输入的关键字"
```

### 文献下载

本项目采用[SCI-HUB](https://sci-hubtw.hkvisa.net/)作为文献下载引擎。下载的过程是：首先通过文件检索获取到文献的链接，而后通过向[SCI-HUB](https://sci-hubtw.hkvisa.net/)发送post请求获取到文献下载地址，即可实现下载。默认情况下，会将检索到的全部文献进行下载，并将他们保存在目录[Paper](./data/Paper)中。在根目录下，可采用如下方式进行文献下载：

```python
python SCIHUB.py --keyword "输入的关键字"
```

## 注意事项

* 访问[谷歌学术](https://scholar.google.com.hk/?hl=zh-CN)需要科学上网，推荐使用[AnyConnect](https://www.micron.com/remote-access/micron-managed-device/cisco-anyconnect)，这样无需配置代理
* 在使用前请先在CONFIG.py文件中设置好[谷歌学术](https://scholar.google.com.hk/?hl=zh-CN)和[SCI-HUB](https://sci-hubtw.hkvisa.net/)的cookie，如遇到网络错误，重新设置cookie即可
* 实测下来文献下载速度较慢，如有速度要求，可自行加入多线程等手段提高效率
* 如需改变文件保存路径，改变CONFIG.py中的PaperInfoAddr及PaperAddr即可

