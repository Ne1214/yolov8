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

創建一個data.yaml檔

```ccs
path: C:/yolo/yolov8  #虛擬環境資料夾 OR data資料夾
train: ./train/images #訓練
val: ./valid/images
test: ./test/images

nc: 1
names: [‘cat’]
```

訓練指令:
```ccs
yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=320 conf=0 device=cpu
```

