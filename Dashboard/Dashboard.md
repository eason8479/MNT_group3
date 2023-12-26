# Dashboard
這裡主要負責使Dashboard可以讓使用者啟動3D列印機前手動輸入預計要列印的模型資料後，預測此次列印是否成功。以及附有圖表即時顯示3D列印機的機台狀況，並隨時預測目前機台狀況是否正常。

This is what enables the Dashboard to predict the success of a print run after the user manually enters the model data to be printed before starting the 3D printer. A chart shows the status of the 3D printer in real time, and predicts whether the current machine status is good or not.

## Palette
開始使用Node-red前需要先安裝這幾個palette：

You need to install these palettes before you start using Node-red:
```
node-red-contrib-pythonshell
node-red-contrib-ui-led
```

## pip
由於需要安裝「requests」函示庫才能正常執行，因此需要先在Node-red環境中安裝pip。[在Linux安裝pip函式庫可以參照這篇文章](https://docs.aws.amazon.com/zh_tw/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html)，其中3.b步驟需要輸入下列指令：

Since you need to install the "requests" library in order to run it properly, you need to install pip in the Node-red environment first. [You can refer to this article to install the pip library in Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html), where step 3.b requires the following commands:
```
export PATH=${PATH}:/usr/src/node-red/.local/bin
```

###### 版本號：v1.0.0