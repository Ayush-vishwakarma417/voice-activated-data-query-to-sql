import sqlite3

# Connect to the database (this creates 'company_data.db' in your folder)
with sqlite3.connect('company_data.db') as conn:
    cursor = conn.cursor()
    
    # Create the sales table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            revenue REAL,
            sale_date TEXT
        )
    ''')
    
    # Insert sample enterprise data
    sample_data = [
        ('Laptop Pro', 2500.00, '2026-09-01'),
        ('Wireless Mouse', 45.99, '2026-09-05'),
        ('Laptop Pro', 2500.00, '2026-09-15'),
        ('Mechanical Keyboard', 120.50, '2026-09-20')
    ]
    
    cursor.executemany('''
        INSERT INTO sales (product_name, revenue, sale_date)
        VALUES (?, ?, ?)
    ''', sample_data)
    
    print("Database 'company_data.db' created and populated successfully!")