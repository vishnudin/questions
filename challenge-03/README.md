# Challenge - 03

Files provided:
```
├── challenge-03
│   ├── README.md
│   └── configs
│       ├── config.json
│       └── input.csv
```


## Ask
- Please find `configs` folder which has csv file and a json file

- your task is to write a simple python code to read from CSV file and update json file.
- we should pass ENV as runtime parameter, based on which python code only update that part of json file leaving other json elements untouched.

- runtime CLI command should look like but may not exactly.
```
#python3 ./updatejson.py --env DEV --json ./config.json --csv ./input.csv
```
- Submit/commit your code as a new file/s to your personal repo folder named challenge-03

- Please provide complete written instructions on how to use your solution files. Like how to run & get to answer.

## Solution 
- I've created a python script "Solution.py" to achieve the ask.

### Prerequisites
- We need Python and Pip installed in our environment to execute the above Python Script.
```
yum install -y python3
yum install -y python3-pip
```
- We are using Pandas and Openpyxl libraries in our script. Need to install them as well.
```
pip3 install pandas
pip3 install openpyxl
```

### Steps to execute Script
- Navigate inside "challenge-03" directory. 
- Execute the below command to update Dev section of JSON file by passing DEV as paramater.
```
python3 solution.py DEV
```

- Execute the below command to update Prod section of JSON file by passing PROD as paramater.
```
python3 solution.py PROD
```

### Result
- On executing the script for Dev env.
<img width="316" alt="challenfe03-Dev" src="https://user-images.githubusercontent.com/54766634/164423088-bc27eb57-627a-4f11-afd5-4ef4263b9f28.png">
- On executing the script for Prod env.
<img width="327" alt="challenge03-Prod" src="https://user-images.githubusercontent.com/54766634/164423785-565f6d69-67d7-45af-8573-36338a310a9e.png">
