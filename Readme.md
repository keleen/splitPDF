# 分割PDF

## 简介
自定义页数切割PDF

![效果图](assets/image/img.png)

### linux 环境
- deepin os 20.3 
- python3.7
- PyPDF2==1.26.0
- PySimpleGUI==4.55.1

### window 环境
- window 10 
- python3.7
- PyPDF2==1.26.0
- PySimpleGUI==4.55.1

### 构建
```shell
git clone git@github.com:keleen/splitPDF.git
cd splitPDF
python3 -m venv venv 

```

### 打包
```shell
pyinstaller -F index.py --name 分割PDF -i assets/image/m10.ico -w
```