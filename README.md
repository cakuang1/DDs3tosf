## DoorDash Snowflake pipeline


## About 

Fairly simple ETL pipeline that mimics a batch processing ETL pipeline. 



## Data Source


The entire dataset comes from <a ahref = "">here.</a> The data is ismply

<b>NOTE</b> I believe this dataset is purely synthetic. I am simply using the data set as a way to work with transactional data. Thus, I am adding certain columns that might 



## Getting Started




### Requirements

    -AWS account(IAM user with full access to S3)
        -AWS_ACCESS_KEY_ID
        -AWS_SECRET_ACCESS_KEY
    -SnowFlake account(Used the free trial)
    
















    






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



