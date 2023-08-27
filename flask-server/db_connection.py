import oracledb

def create_connection():    

    #connection = oracledb.connect(user="kosa18", password="kosa2023oraclE", dsn="edudb_high",
                                  #config_dir="/Users/KOSA/dev/Wallet_edudb",
                                  #wallet_location="/Users/KOSA/dev/Wallet_edudb",
                                  #wallet_password="pythonoracle21")
    connection = oracledb.connect("system/oracle@localhost:1521/xepdb1")
    return connection


CURSOR = oracledb.CURSOR


def fetch_data_from_table(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return result

if __name__ == "__main__":
    tables = ["MED_USER", "COMPANY", "INGREDIENT", "MEDICINE"]
    
    for table in tables:
        print(f"Fetching data from {table} table:")
        data = fetch_data_from_table(table)
        for row in data:
            print(row)