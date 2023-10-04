import mysql.connector
mydb  = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'store')

if mydb.is_connected():
    print('Connection successful')

def get_products_by_category();
    cname = input('Enter category name : ')
    conn = mydb.cursor()
    conn.execute("SELECT p.product_name, p.price, p.stock_quantity FROM categories c JOIN product_categories pc USING(category_id) JOIN products p USING(product_id) WHERE c.category_name = %s",(cname))
    result = conn.fetchall()
    final_result = dict(result)
    
