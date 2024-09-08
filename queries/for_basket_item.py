from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_basket_item_table_query() -> None:
    """
    Creates a table for storing basket items.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS basket_item (
        id BIGSERIAL PRIMARY KEY,
        basket_id BIGINT REFERENCES basket(id) NOT NULL,
        product_id BIGINT REFERENCES products(id) NOT NULL,
        quantity BIGINT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_basket_item_from_id_query(basket_item_id: int) -> DictRow:
    """
    Retrieves a basket item from the database by its ID.

    Args:
        basket_item_id (int): The ID of the basket item to retrieve.

    Returns:
        DictRow: The retrieved basket item.
    """
    query = "SELECT * FROM basket_item WHERE id = %s AND status = %s;"
    params = (basket_item_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_basket_items_from_basket_id_query(basket_id: int) -> list:
    """
    Retrieves basket items from the database by their basket ID.

    Args:
        basket_id (int): The ID of the basket.

    Returns:
        list: The retrieved basket items.
    """
    query = "SELECT * FROM basket_item WHERE basket_id = %s AND status = %s;"
    params = (basket_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_product_from_basket_item_query(basket_id: int) -> DictRow:
    """
    Retrieves the product from the database associated with a basket item.

    Args:
        basket_id (int): The ID of the basket.

    Returns:
        DictRow: The retrieved product.
    """
    query = """
    SELECT p.*
    FROM basket_item b
    JOIN products p ON b.product_id = p.id
    WHERE bi.basket_id = %s AND p.status = %s;
    """
    params = (basket_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_basket_item_query(basket_id: int, product_id: int, quantity: int) -> None:
    """
    Inserts a new basket item into the database.

    Args:
        basket_id (int): The ID of the basket.
        product_id (int): The ID of the product.
        quantity (int): The quantity of the product.
    """
    query = "INSERT INTO basket_item (basket_id, product_id, quantity) VALUES (%s, %s, %s);"
    params = (basket_id, product_id, quantity)
    execute_query(query, params)
    return None


def update_basket_item_query(basket_item_id: int, quantity: int) -> None:
    """
    Updates an existing basket item in the database.

    Args:
        basket_item_id (int): The ID of the basket item to update.
        quantity (int): The new quantity of the product.
    """
    query = "UPDATE basket_item SET quantity = %s WHERE id = %s AND status = %s;"
    params = (quantity, basket_item_id, True)
    execute_query(query, params)
    return None


def delete_basket_item_query(basket_item_id: int) -> None:
    """
    Deletes a basket item from the database.

    Args:
        basket_item_id (int): The ID of the basket item to delete.
    """
    query = "UPDATE basket_item SET status = %s WHERE id = %s;"
    params = (False, basket_item_id)
    execute_query(query, params)
    return None


def get_all_product_items_query() -> list:
    """
    Retrieves all active basket items from the database.

    Returns:
        list: The retrieved basket items.
    """
    query = "SELECT * FROM basket_item WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
