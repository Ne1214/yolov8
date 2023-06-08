# yolov8
 
 ## 1. 首先下載CUDA版本，以及cuDNN
我們可以從NVIDIA官網進行下載，選定你的作業系統以及想要下載的版本

https://developer.nvidia.com/cuda-downloads

<img width="549" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/a8980d7a-6877-4fcf-affb-7f3aeda0946e">

另外小提醒，cuDNN需要註冊會員後才能下載

<img width="547" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/29d4fa9d-e925-4d75-9b57-3bcd4b6c0239">

## 2. 接著安裝Python版本，筆者使用的版本是Python3.9，注意要從Python官網下載才行

Python的版本需>=3.7

https://www.python.org/

## 3. 接下來透過pip進行安裝，可從PyTorch官網上選擇執行版本對應的指令

安裝PyTorch, 版本需>=1.7

https://pytorch.org/get-started/locally/

<img width="565" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/7a7c6e26-7f3e-4ee7-aec0-fd6e96ac2cac">

安裝YOLOv8
```ccs
pip install ultralytics
```
至此，基本環境已建置完成
## 4.辨識/訓練

參考網址:
https://hackmd.io/@luckychi/yolov8_simple_tutorial
### 1.training
1.先在虛擬環境的資料夾下創建一個資料夾裡放https://www.larrysprognotes.com/files/splitFile.py
這個程式，然後在裡面創一個檔名為:all的資料夾，裡面放訓練資料以及圖片

注意:裡面一定要有classes.txt(裡面放labalimg的訓練資料)

2.執行splitFile.py<img width="380" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/6a42db5f-ce04-4d98-b716-7152b4df0c5a">
後面的數字代表訓練圖片數量

3.images和labels資料夾裡的兩個資料夾內的內容要相同

4.val.txt內容複製到train.txt然後

<img width="541" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/76d7f9a4-41aa-4dd2-b4cc-98e7d336fa24">

5.創建一個data.yaml檔(內容如下)

```ccs
path: C:/yolo/yolov8  #虛擬環境資料夾 OR data資料夾
train: ./train/train.txt #訓練圖片位置
val: ./valid/val.txt #標註資料位置
test: #資料位置

nc: 1 #標註數量
names: [‘cat’]#標註標籤名稱
```

6.訓練指令:
```ccs
yolo task=detect mode=train data=data.yaml model=yolov8n.pt epochs=100 imgsz=320 conf=0 device=cpu #device更改cpu、gpu
```

也可以使用Python指令來進行訓練

<img width="543" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/010ddcbf-ffe9-41ec-ad5e-f2184c5bb758">

其中device參數若未指定則會使用GPU進行訓練，device=0即使用第一張GPU卡，也可device=0,1使用2張卡來進行運算，而device=cpu即使用CPU來運算
由於筆者測試的電腦顯示卡型號太舊，會出現以下錯誤
RuntimeError: cuDNN error: CUDNN_STATUS_NOT_INITIALIZED
因此筆者下面都使用CPU來進行訓練與預測

訓練完後的資料會出現在runs/detect/train底下，訓練好的模型放在runs/detect/train/weights底下，我們接下來將使用best.pt來進行估測
### 2.predict

使用以下指令進行估測
```ccs
yolo task=detect mode=predict model=best.pt source=test/images save=true device=cpu
```
當save=true時，會將預測的結果儲存在runs/detect/predict底下

同樣以Python指令執行時

<img width="538" alt="image" src="https://github.com/Ne1214/yolov8/assets/132657666/a6bd14de-c60e-4979-b96f-6ad9131bb157">

