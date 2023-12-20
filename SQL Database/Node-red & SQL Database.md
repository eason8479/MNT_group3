# Node-red & SQL Database
這裡主要負責讓筆電使用Node-Red接收OPC UA的資料並資料處理儲存於SQL Database裡。其中一個方法節點需要手動調整參數。

This is where Laptop uses Node-Red to receive OPC UA data and process the data to be stored in SQL Database. One of the function nodes requires manual parameter adjustment.

## SQL Database Structure
| Print No | Nozzle Temperature| Plate Temperature | X-axis Angle | Y-axis Angle | X | Y | Model | Time | Successful |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
|  |  |  |  |  |  |  |  |  |  |

列印時需要手動輸入以下四個參數：

The following four parameters need to be entered manually when printing:
1. Print No
2. X
3. Y
4. Model

## Check for Successful
另一個流則是在成品完成後，主觀認定是否列印成功。其中一個方法節點需要手動調整列印編號以及成功欄位的布林值。

The other flow is to subjectively determine whether the product is successful or not after finishing work. One of the function nodes requires manual adjustment of the Print No and Boolean value of the Successful column.