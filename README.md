# IG圖片物件偵測

## 介紹
- 利用爬蟲selenium開啟Instagram,透過Hashtag搜尋關鍵字,將關鍵字的圖片下載下來
- 使用Tkinter製作GUI介面,並進行YOLOv7的辨識
- 目前辨識類別只有**貓**.**狗**.**馬**.**鳥**

## 事前準備
- 先安裝YOLOv7環境
``` shell
pip install -r yolov7/requirements.txt
```
- 安裝GUI所需套件
``` shell
pip install tkinter
pip install Pillow
```

## 使用方法
- 左上角新增檔案(選擇欲辨識的圖)
- 勾選需要辨識的類別
- 按下**Detect**按鈕,此時文字會呈現紅色,代表正在辨識中,需耐心等待
- 辨識完成後會跳出訊息視窗,按下確定後即可在中間看到辨識後的圖片
## 結果
- 辨識是否成功會呈現於圖片上方
- 如果為擬人繪畫圖或是特徵不明顯的照片,容易辨識不出來
<div align="center">
    <a href="./">
        <img src="./figure/fig1.PNG" width="70%"/>
    </a>
</div>
<div align="center">
    <a href="./">
        <img src="./figure/fig2.PNG" width="45%"/>
    </a>
    <a href="./">
        <img src="./figure/fig3.PNG" width="45%"/>
    </a>
</div>
