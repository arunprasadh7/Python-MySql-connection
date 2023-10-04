import mysql.connector

mydb  = mysql.connector.connect(
    host = 'localhost', 
  user = 'root',
  password = '',
  database = 'store')

if mydb.is_connected():
  print('Connection Successful')
else:
  print('Failed to connect to DB')

def get_products_by_category():
  cname = input('Enter category name : ')
  conn = mydb.cursor(dictionary = True)
  conn.execute("SELECT p.product_name, p.price, p.stock_quantity FROM products p INNER JOIN product_categories pc  ON p.product_id = pc.product_id INNER JOIN categories c ON pc.category_id = c.category_id WHERE c.category_name = %s", (cname,))
  result = conn.fetchall()
  return result


def low_stock_products():
  qty = int(input('Enter minimum stock quantity : '))
  conn = mydb.cursor()
  conn.execute("SELECT product_name FROM products WHERE stock_quantity < %s LIMIT 3", (qty,))
  result = conn.fetchall()
  print(result)

def create_new_product():
  pname = input('Enter product name : ')
  price = int(input('Enter product price : '))
  qty = int(input('Enter stock quantity : '))
  conn = mydb.cursor()
  result = conn.execute("INSERT INTO products(product_name, price, stock_quantity) VALUES (%s, %s, %s)", (pname, price, qty))
  mydb.commit()
  print('Product creation successful')
  # return result

# print(get_products_by_category())

# print(low_stock_products())

create_new_product()