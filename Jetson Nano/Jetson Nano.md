# Jetson Nano
這裡主要負責Jetson Nano利用OPC UA將感測器讀到的資訊發布出去。理論上Jetson Nano在整個流程中只需要執行一個main檔而已。

This is where the Jetson Nano publishes information read from the sensors using OPC UA. Theoretically, Jetson Nano only needs to execute one main file in the whole process.

## Jetson Nano Initialization Environment
```
sudo pip3 install smbus2
sudo pip3 install crcmod
```