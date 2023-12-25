# Jetson Nano
這裡主要負責Jetson Nano利用OPC UA將感測器讀到的資訊發布出去。理論上Jetson Nano在整個流程中只需要執行一個main檔而已。

This is where the Jetson Nano publishes information read from the sensors using OPC UA. Theoretically, Jetson Nano only needs to execute one main file in the whole process.

## Jetson Nano Initialization Environment
```
sudo pip3 install smbus2
sudo pip3 install crcmod
```

## Things to do before running main.py
**每次**要開啟main.py前**都要**執行下列步驟，否則會出錯！

**Every time** you start main.py you **must do** the following steps before you start it, otherwise you will get an error!
```
cd /sys/bus/i2c/devices/i2c-0
sudo vi bus_clk_rate
```

接著將檔案裡頭的數字改成：

Then change the number in the file to:
```
100000
```

:::info
### How to use vi the text editor
開啟vi編輯器後按下「INSERT」鍵就可編輯檔案。儲存檔案時按「ESC」後輸入「:wq」就可退回指令介面。

Open vi the text editor and then press "INSERT" key to edit the file. When saving a file, press "ESC" and enter ":wq" to return to the command interface.
:::

## Sensor Wiring
MPU6050和量測底板的MLX90614使用I2C Bus 0，量測噴頭的MLX90614使用I2C Bus 1。

MPU6050 and MLX90614 for measuring nozzle use I2C Bus 0, and the MLX90614 for measuring plate uses I2C Bus 1.

## Function "linear_adjustment"
使用此方法可以讓感測器讀值調整至正確的溫度。使用時需要輸入兩個參數，第一個是理想上應該要讀到的數值，第二個是實際上讀到的**最大值**。建議在開始讀值前使用此方法。

Use this function to adjust the sensor reading to the correct temperature. There are two parameters that need to be entered, the first is the value that should ideally be read and the second is the **maximum value** that actually is read. It is recommended to use this function before starting to read values.

```python
def linear_adjustment(self, ideal=1, real=1)
```

###### 版本號：v1.0.0-beta