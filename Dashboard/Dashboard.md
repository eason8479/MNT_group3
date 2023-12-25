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

###### 版本號：v2-dev