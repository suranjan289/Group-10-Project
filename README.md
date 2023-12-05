# Group-10-Project
 DAB111 - Final project files for Python

 Objective:

 To showcase ability to transfer data from an existing dataset into a new database.
 To use Flask within a Python environment to connect to the mentioned new database.
 Create a skeleton website using Python/Flask to display/render data within the database via HTML.

 Approach:
 1. All data within downloaded csv dataset replicated in a new database. New data has also been inserted. This process has been done via the script: __Group 9- DAB111.ipynb__
 2. Database connection done via sqlite3. HTML rendering done via Flask. The script for these task is within: __app.py__. This script is to be executed via a Python terminal.
 3. All HTML files are located within the __/templates__ directory.

 Project requirements:

    5% informative/formatted readme + requirements  
    5% file organization on GitHub
    5% data collection requirements satisfied
    25% database creation and data insertion
    60% website
        50% creation
        10% formatting

1. Original dataset from Kaggle: https://www.kaggle.com/datasets/ahmedabbas757/coffee-sales
<br>
   Overview of variables:
   <br>
   <br>
   transaction_id : Unique sequential ID representing an individual transaction
   <br>
   transaction_date : Date of the transaction (MM/DD/YY)
   <br>
   transaction_time : Timestamp of the transaction (HH:MM:SS)
   <br>
   transaction_qty : Quantity of items sold
   <br>
   store_id : Unique ID of the coffee shop where the transaction took place
   <br>
   store_location : Location of the coffee shop where the transaction took place
   <br>
   product_id : Unique ID of the product sold
   <br>
   unit_price : Retail price of the product sold
   <br>
   product_category : Description of the product category
   <br>
   product_type : Description of the product type
   <br>
   product_detail : Description of the product being sold
   <br>
