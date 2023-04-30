## DoorDash Snowflake pipeline


## About 

Fairly simple ETL pipeline that imports c 



## Data Source


The entire dataset comes from <a ahref = "">here.</a> The data is ismply

<b>NOTE</b> I belive this dataset is purely synthetic. I am simply using the data set as a way to work with transactional data.



## Getting Started

### Requirements




## Pipe-Line Components





## Dataset Description




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
| Amount_of_tip| Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges. |
| Refunded_amount | $0.50 MTA tax that is automatically triggered based on the metered rate in use. | 
| Total_time_elapsed | Total time elapsed | 


Index(['Unnamed: 0', 'Customer_placed_order_datetime',
       'Placed_order_with_restaurant_datetime',
       'Driver_at_restaurant_datetime', 'Delivered_to_consumer_datetime',
       'Driver_ID', 'Restaurant_ID', 'Consumer_ID', 'Is_New',
       'Delivery_Region', 'Is_ASAP', 'Order_total', 'Amount_of_discount',
       'Amount_of_tip', 'Refunded_amount', 'Total_time_elapsed'],
      dtype='object')