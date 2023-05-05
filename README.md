## DoorDash Snowflake pipeline

A manual step-by-step data pipeline that extracts data files from s3, transforms the data, and loads them into a snowflake table. 

<b> Tools used:</b>









## Pipeline Diagram
![alt text](pipepic.svg)


## Getting Started


### Requirements
    -AWS account (IAM user with full access to S3). You need:
        -AWS_ACCESS_KEY_ID
        -AWS_SECRET_ACCESS_KEY
    -SnowFlake account(Used the free trial). You need:
        -Your account username
        -Your account password
        -Your account name
    -Docker Installed on local machine
### Setup

1. Create and env file named `.env` with the content below. Fill in the # with the your snowflake information and AWS keys.

```
snowflake_user = '######'
snowflake_password = '######'
snowflake_account = '######'

snowflake_database = 'ddtosfpipeline' # Dont need to change
snowflake_schema = 'ddtosfpipelineschema' # Dont need to change
AWS_REGION = "us-west-1" # Dont need to change
BUCKET_NAME = 'ddsfpipeline' # Dont need to change


```


2. Build your docker image using the command

```
docker build -t myimage:latest 
```

3. Run the 







    






## Dataset Description

We are dealing with DoorDash transactional data. Each row represents a doordash order.




| Field Name      | Description |
| ----------- | ----------- |
| Customer_placed_order_datetime      | The data and time when the customer placed the order |
| Driver_at_restaurant_datetime  | The date and time when the driver arrived at the restaurant|
| Delivered_to_consumer_datetime   | The date and time when the food was delivered to the consumer    |
| Driver_ID   | The ID of the Driver      |
| Restaurant_ID  | The ID of the Restaurant      |
| Consumer_ID  | The ID of the Consumer    |
| Is_New  |  Whether or not the consumer is a new user |
| Delivery_Region  | Region of the customer address |
| Is_ASAP | Customer included|
| Order_total | The total Order amount  |
| Amount_of_discount | Discounted amount towards the Order | 
| Amount_of_tip| Total amount of tips the customer gave|
| Refunded_amount | The amount refunded  | 
| Total_time_elapsed | Total time it took for the order to be delivered after the customer placed the order | 



## S3 description

# Bucket has three directories
| Directory    | Description |
| ----------- | ----------- |
| Customer_placed_order_datetime      | The data and time when the customer placed the order |
| Driver_at_restaurant_datetime  | The date and time when the driver arrived at the restaurant|
| Delivered_to_consumer_datetime   | The date and time when the food was delivered to the consumer    |
| Driver_ID   | The ID of the Driver      |




## Pipe-Line Components


## Data Source


The entire dataset comes from <a ahref = "">here.</a> The data 

<b>NOTE</b> I believe this dataset is purely synthetic. I am simply using the data set as a way to work with transactional data. Since I am creating this project for learning purposes, the actual data does not really matter. (Any dataset could work)


## Whats Next?

- Orchestration using Airflow. Will probably not apply to this project



