from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_order_item_table_query() -> None:
    """
    Creates a table for storing order items.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS order_item (
        id BIGSERIAL PRIMARY KEY,
        order_id BIGINT REFERENCES orders(id) NOT NULL,
        name VARCHAR(64) NOT NULL,
        quantity INT NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_order_item_from_id_query(order_item_id: int) -> DictRow:
    """
    Retrieves an order item from the database by its ID.

    Args:
        order_item_id (int): The ID of the order item to retrieve.

    Returns:
        DictRow: The retrieved order item.
    """
    query = "SELECT * FROM order_item WHERE id = %s AND status = %s;"
    params = (order_item_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_order_items_from_order_id_query(order_id: int) -> list:
    """
    Retrieves order items from the database by their order ID.

    Args:
        order_id (int): The ID of the order.

    Returns:
        list: The retrieved order items.
    """
    query = "SELECT * FROM order_item WHERE order_id = %s AND status = %s;"
    params = (order_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def insert_order_item_query(order_id: int, name: str, quantity: int, price: float) -> None:
    """
    Inserts a new order item into the database.

    Args:
        order_id (int): The ID of the order.
        name (str): The name of the product.
        quantity (int): The quantity of the product.
        price (float): The price of the product.
    """
    query = "INSERT INTO order_item (order_id, name, quantity, price) VALUES (%s, %s, %s, %s);"
    params = (order_id, name, quantity, price)
    execute_query(query, params)
    return None


def update_order_item_query(order_item_id: int, name: str, quantity: int, price: float) -> None:
    """
    Updates an existing order item in the database.

    Args:
        order_item_id (int): The ID of the order item to update.
        name (str): The new name of the product.
        quantity (int): The new quantity of the product.
        price (float): The new price of the product.
    """
    query = "UPDATE order_item SET name = %s, quantity = %s, price = %s WHERE id = %s;"
    params = (name, quantity, price, order_item_id)
    execute_query(query, params)
    return None


def delete_order_item_query(order_item_id: int) -> None:
    """
    Deletes an order item from the database.
    """
    query = "UPDATE order_item SET status = %s WHERE id = %s;"
    params = (False, order_item_id)
    execute_query(query, params)
    return None


def get_all_order_items_query() -> list:
    """
    Retrieves all active order items from the database.

    Returns:
        list: The retrieved order items.
    """
    query = "SELECT * FROM order_item WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
