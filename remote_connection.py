import psycopg2

def connect_to_redshift(host, dbname, user, password, port=5439):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection to Redshift established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to Redshift: {e}")
        return None

# Example usage
if __name__ == "__main__":
    host = "your-redshift-cluster-endpoint"
    dbname = "your-database-name"
    user = "your-username"
    password = "your-password"
    
    connection = connect_to_redshift(host, dbname, user, password)
    if connection:
        # Perform database operations
        connection.close()