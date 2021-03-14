import psycopg2

# When I opened up my container, my IP address had changed, so this is the code to check it:
# docker inspect team-3-project_devcontainer_postgres_1 | grep IPAddress

# CREATE TYPE size AS ENUM ('Standard' , 'Regular' , 'Large');

def create_db_connection():
    connection = psycopg2.connect(
                    database="team-3-group-project",
                    user="root", 
                    password="password", 
                    host="172.18.0.2", 
                    port="5432"
                    )
    return connection

def create_product_size_table():
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS product_size(
                        product_size_id SERIAL PRIMARY KEY,
                        product_size VARCHAR(50) NOT NULL
                        );
                        INSERT INTO product_size(product_size)
                        VALUES('standard'), ('regular'), ('large')'''
            cursor.execute(sql)        
            connection.commit()
    except Exception as e:
        print(e)

def create_product_table():
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS product(
                        product_id SERIAL PRIMARY KEY,
                        product_name VARCHAR(100) NOT NULL,
                        product_size_id INT,
                        product_price FLOAT,
                        CONSTRAINT fk_product_size FOREIGN KEY(product_size_id) REFERENCES product_size(product_size_id)
                        )'''
            cursor.execute(sql)
            connection.commit() 
    except Exception as e:
        print(e)     

def create_branch_table():
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS branch(
                        branch_id SERIAL PRIMARY KEY,
                        branch_location VARCHAR(100) NOT NULL
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_transaction_table():
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS transaction(
                        transaction_id SERIAL PRIMARY KEY,
                        date_time TIMESTAMP,
                        transaction_total FLOAT NOT NULL,
                        branch_id INT,
                        CONSTRAINT fk_branch FOREIGN KEY(branch_id) REFERENCES branch(branch_id)
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

def create_basket_table():
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            sql = '''CREATE TABLE IF NOT EXISTS basket(
                        basket_id SERIAL PRIMARY KEY,
                        product_id INT,
                        transaction_id INT,
                        CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES product(product_id),
                        CONSTRAINT fk_transaction FOREIGN KEY(transaction_id) REFERENCES transaction(transaction_id)
                        )'''
            cursor.execute(sql)
            connection.commit()
    except Exception as e:
        print(e)

create_product_size_table()
create_product_table()
create_branch_table()
create_transaction_table()
create_basket_table()

print("Your tables have been created successfully")
