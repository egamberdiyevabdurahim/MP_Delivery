from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_order_table_query() -> None:
    """
    Creates a table for storing orders.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS order (
        id BIGSERIAL PRIMARY KEY,
        user_id BIGINT REFERENCES users(id) NOT NULL,
        courier_id BIGINT REFERENCES courier(id) NOT NULL,
        total_quantity INT DEFAULT 0,
        total_price DECIMAL(10, 2) DEFAULT 0.00,
        is_delivered BOOLEAN DEFAULT FALSE,
        promocode_code VARCHAR(64) REFERENCES promocode(code),
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_order_from_id_query(order_id: int) -> DictRow:
    """
    Retrieves an order from the database by its ID.

    Args:
        order_id (int): The ID of the order to retrieve.

    Returns:
        DictRow: The retrieved order.
    """
    query = "SELECT * FROM order WHERE id = %s AND status = %s;"
    params = (order_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_orders_from_user_id_query(user_id: int) -> list:
    """
    Retrieves orders from the database by the user's ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: The retrieved orders.
    """
    query = "SELECT * FROM order WHERE user_id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_orders_from_courier_id_query(courier_id: int) -> list:
    """
    Retrieves orders from the database by the courier's ID.

    Args:
        courier_id (int): The ID of the courier.

    Returns:
        list: The retrieved orders.
    """
    query = "SELECT * FROM order WHERE courier_id = %s AND status = %s;"
    params = (courier_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def insert_order_query(user_id: int, courier_id: int, promocode_code: str) -> None:
    """
    Inserts a new order into the database.

    Args:
        user_id (int): The ID of the user who placed the order.
        courier_id (int): The ID of the courier assigned to the order.
        promocode_code (str): The code of the promocode used for the order.
    """
    query = "INSERT INTO order (user_id, courier_id, promocode_code) VALUES (%s, %s, %s);"
    params = (user_id, courier_id, promocode_code)
    execute_query(query, params)
    return None


def update_order_query(order_id: int, total_amount: int, total_price: float) -> None:
    """
    Updates an order's total amount and total price in the database.

    Args:
        order_id (int): The ID of the order to update.
        total_amount (int): The new total quantity of the order.
        total_price (float): The new total price of the order.
    """
    query = "UPDATE order SET total_quantity = %s, total_price = %s WHERE id = %s;"
    params = (total_amount, total_price, order_id)
    execute_query(query, params)
    return None


def mark_order_as_delivered_query(order_id: int) -> None:
    """
    Marks an order as delivered in the database.

    Args:
        order_id (int): The ID of the order to mark as delivered.
    """
    query = "UPDATE order SET is_delivered = %s WHERE id = %s AND status = %s;"
    params = (True, order_id, True)
    execute_query(query, params)
    return None


def delete_order_query(order_id: int) -> None:
    """
    Deletes an order from the database.

    Args:
        order_id (int): The ID of the order to delete.
    """
    query = "UPDATE order SET status = %s WHERE id = %s;"
    params = (False, order_id)
    execute_query(query, params)
    return None


def get_all_orders() -> list:
    """
    Retrieves all orders from the database.

    Returns:
        list: The retrieved orders.
    """
    query = "SELECT * FROM order WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
