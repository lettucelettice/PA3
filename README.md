# EXPERIMENT 3 - PYTHON DATA ANALYSIS

This repository features Python scripts designed to solve various problems in ECE2112. Below is a summary of each script. 

### Problem 1

###### This problem involves (a) loading a ".csv" file into the notebook and (b) displaying the first 5 and last 5 rows from the said file.

**Function:**

```python

#access pandas library
import pandas pd 

#read and output the declared ".csv" file
cars = pd.read_csv('cars.csv')
cars

```

**Ouput:**

![image](https://github.com/user-attachments/assets/ed248319-09b2-47ca-a279-1b57c0b89473)

![image](https://github.com/user-attachments/assets/24b0aefc-da9f-40e5-be91-5f6c74a4a637)

```python

#load the first five rows from the ".csv" file
cars.head()

```
**Output:**

![image](https://github.com/user-attachments/assets/1abec3da-e67a-42bf-a11d-d0dbcd7b85ca)

```python

#load the last five rows from the ".csv" file
cars.tail()

```
**Output:**

![image](https://github.com/user-attachments/assets/8f219257-a6d5-45b2-9ea6-1c012cc0d31a)

### Problem 2

###### This problem requires data extraction from the "cars" data frame using subsetting, slicing, and indexing techniques. It involves retrieving specific rows, columns, and values based on conditions related to car models, cylinder counts, and gear types.

**Function:**

```python

#display the first five odd rows of cars
odd = cars.iloc[[1,3,5,7,9]]
odd

```
**Output:**

![image](https://github.com/user-attachments/assets/f20093c4-987d-48e0-a05a-e57b9ce71687)


**Function:**

```python

#output row containing the model of Mazda RX4
cars.loc[[1]]

```

**Output:**

![image](https://github.com/user-attachments/assets/effa9fc6-ecdb-4b17-9282-b70d4b80c71e)

**Function:**
```python

#output the value for "cyl" of car model 'Camaro Z28'
cars.loc[[23],['cyl']]

```

**Output:**

![image](https://github.com/user-attachments/assets/2844e616-5786-4221-9f78-b909eb6fb215)

**Function:**
```python

#output the values for "cyl" and "gear" for the following car models
cars.loc[[1,18,28],['cyl','gear']]

```

**Output:**

![image](https://github.com/user-attachments/assets/fff50e04-3503-45e3-93b1-9d234ed48883)






