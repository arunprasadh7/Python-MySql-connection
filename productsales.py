#product sales

import mysql.connector

mydb  = mysql.connector.connect(
    host = 'localhost', 
  user = 'root',
  password = '',
  database = 'productsales')


if mydb.is_connected():
  print('Connection Successful')
else:
  print('Failed to connect to DB')


#1 total sales by product category

q1 = """SELECT 
	product_name,
    SUM(stock_qty * price) AS total_sales
FROM products p 
JOIN order_items oi 
	USING(product_id)
GROUP BY product_name
ORDER BY total_sales DESC"""

def sales_by_product_category():
	conn = mydb.cursor()
	conn.execute(q1)
	result = conn.fetchall()
	return result

#2Customers with most orders

q2 = '''SELECT 
	customer_name,
    COUNT(order_id) AS total_orders
FROM customers c 
JOIN orders o
	USING(customer_id)
GROUP BY customer_name
ORDER BY total_orders DESC
LIMIT 5'''

def cx_most_orders():
	conn = mydb.cursor()
	conn.execute(q2)
	result = conn.fetchall()
	return result

#3 PRODUCTS with low stock

q3 = '''SELECT 
	product_name,
    stock_qty
 FROM products
 WHERE stock_qty < 10'''

def low_stock():
 	conn = mydb.cursor()
 	conn.execute(q3)
 	result = conn.fetchall()
 	return result


print(sales_by_product_category())

print(cx_most_orders())

print(low_stock())