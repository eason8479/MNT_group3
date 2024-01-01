# Application of IoT technology on 3D-Printer performance

![](https://img.shields.io/badge/release-v1.0.0-blue?style=flat-square)

## Division of Work
| 林劭芸          | 褚紘維         | 柯登獻           | 歐子萌         | 林義軒         | Carlos Avramoff          |
| --------------- | -------------- | ---------------- | -------------- | -------------- | ------------------------ |
| 設計感測器夾具  | 設計感測器夾具 | 尋找適合的感測器 | 監控列印機數據 | 感測器接線布局 | 尋找適合訓練AI的列印模型 |
| 開發Jetson Nano | 監控列印機數據 | 焊接感測器       |                | 監控列印機數據 |                          |
| 開發Dashboard   |                | 設計感測器夾具   |                | 開發GPU Server |                          |
|                 |                | 開發Jetson Nano  |                | 開發AI回歸模型 |                          |
|                 |                | 開發SQL Database |                |                |                          |
|                 |                | 開發Dashboard    |                |                |                          |

| 林劭芸                     | 褚紘維                | 柯登獻                     | 歐子萌               | 林義軒                          | Carlos Avramoff                          |
| -------------------------- | --------------------- | -------------------------- | -------------------- | ------------------------------- | ---------------------------------------- |
| Design sensor fixture      | Design sensor fixture | Finding the right sensor   | Monitor printer data | Sensor wiring layout            | Finding printable models for AI training |
| Developing the Jetson Nano | Monitor printer data  | Welding sensor             |                      | Monitor printer data            |                                          |
| Developing the Dashboard   |                       | Design Sensor Fixture      |                      | Developing the GPU Server       |                                          |
|                            |                       | Developing the Jetson Nano |                      | Developing AI regression models |                                          |
|                            |                       | 開發SQL Database           |                      |                                 |                                          |
|                            |                       | Developing the Dashboard   |                      |                                 |                                          |

## Objective

### 中文
1. 監控底板的水平角度
2. 監控噴頭、底板的溫度
3. 開發回歸模型，開始前預測此次列印是否成功、以及隨時監控預測機台狀況是否正常
4. 在Dashboard中遠端顯示列印機和預測的資訊

### English
1. Monitor the horizontal angle of the plate
2. Monitor the temperature of the nozzle and the plate
3. Develop regression models, predict the success of the print before starting, and monitor the status of the 3D printer at all times
4. Remote display of printer and forecast information in the Dashboard

## Work

### Requirements
目標是使用邊緣裝置以及感測器收集3D列印機的資訊並顯示在Dashboard上，以及利用收集到的資料用於訓練AI回歸模型預測列印是否成功與機台狀況是否正常。

The goal is to use edge devices and sensors to collect information about the 3D printer and display it on the Dashboard, as well as to use the collected data to train an AI regression model to predict whether a print was successful or not, and whether the printer was in proper condition.

### Hardware
1. Jetson Nano
2. Wireless network interface controller(WNIC)
3. Computer to show dashboard
4. MPU6050
5. MLX90614
6. Wire

### Software
1. pip3
2. python3
3. sys
4. time
5. opcua
6. [mpu6050](https://github.com/m-rtijn/mpu6050)
7. [mlx90614](https://github.com/sightsdev/PyMLX90614)

### Result

#### 中文
1. 感測器成功讀到數值
2. 其他裝置可以連線至OPC UA
3. 每2秒可儲存數據到SQL Database裡
4. 成功使用GPU Server並訓練AI回歸模型
5. 資訊可以顯示在Dashboard中

#### English
1. Sensors successfully read the value
2. Other devices can be connected to the OPC UA
3. Save data to SQL Database every 2 seconds
4. Successfully using GPU Server and training AI regression models
5. Information can be displayed in the Dashboard

## Discussion and Suggetion

### Summery

#### 中文
1. 透過感測器收集資料（MPU6050、MLX90614）
2. 將Jetson Nano作為邊緣裝置並使用OPC UA技術與其他裝置連線
3. 使用Node-red儲存3D列印機的資料至SQL Database裡
4. 將SQL Database的資料預處理後，使用GPU Server並訓練AI回歸模型
5. 將資訊顯示在Dashboard中

#### English
1. Data collection via sensors (MPU6050, MLX90614)
2. Use the Jetson Nano as an edge device and connect to other devices using OPC UA technology
3. Use Node-red to store 3D printer data in SQL Database
4. Preprocess data from SQL Database, then use GPU Server and train AI regression model
5. Display information in the Dashboard

### Suggestion

#### 中文
1. 可嘗試使用非同步方法將預測功能整合進Jetson Nano裡，減少主機的運算負擔

#### English
1. Try integrating predictions into the Jetson Nano using asynchronous method to reduce the computational burden on the host

## License
Project is licensed under the [MIT](https://github.com/eason8479/MNT_group3/blob/main/LICENSE.txt) license