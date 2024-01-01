# Model 1
- Use for predict the print will success or not
- Inputs and their order for the model are as follow

Name | order
--- | ---
Printing_object | 0
pos_x | 1
pos_y | 2
plate_angel | 3
nozzle_temperture | 4
plate_temperature | 5

- The model will return 1(print will success) ,or 0(print will fail)

> [!WARNING]  
> Due to the lack of the training data, this modle shouldn't be use in any real case.
> Please just take this model as a prove of concept for running duo model on the same server.

# Model 2
- Use for checking current machin is working normally or not
- Inputs and their order for the model are as follow

Name | order
--- | ---
plate_angel_x | 0
plate_angel_y | 1
nozzle_temperture | 2
plate_temperature | 3

- The model will return 1(machine is normal) ,or 0(machine is not normal)

# Use of the code in this folder
- /Model_1: The data for traing model 1 and the code for training/interate with it.
- /Model_2: The data for traing model 2 and the code for training/interate with it.
- Cloud_Computer.ipynb: The code that is running on the cloud server.