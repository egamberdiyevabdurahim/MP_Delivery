from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_purse_table_query() -> None:
    """
    Creates a table for storing purses.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS purse (
        id BIGSERIAL PRIMARY KEY,
        amount DECIMAL(10, 2) NOT NULL DEFAULT 0
    );
    """)
    return None


def get_purse_from_id_query(purse_id: int) -> DictRow:
    """
    Retrieves a purse from the database by its ID.

    Args:
        purse_id (int): The ID of the purse to retrieve.

    Returns:
        DictRow: The retrieved purse.
    """
    query = f"SELECT * FROM purse WHERE id = %s AND status = %s;"
    params = (purse_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_purse_query() -> None:
    """
    Inserts a new purse into the database with an initial amount of 0.

    Returns:
        None.
    """
    query = ("INSERT INTO purse (amount)"
             "VALUES (%s);")
    params = (0,)
    execute_query(query, params)
    return None


def update_purse_amount_query(purse_id: int, amount: float) -> None:
    """
    Updates a purse's amount in the database.

    Args:
        purse_id (int): The ID of the purse to update.
        amount (float): The new amount for the purse.

    Returns:
        None.
    """
    query = "UPDATE purse SET amount = %s WHERE id = %s AND status = %s;"
    params = (amount, purse_id, True)
    execute_query(query, params)
    return None


def delete_purse_query(purse_id: int) -> None:
    """
    Deletes a purse from the database.

    Args:
        purse_id (int): The ID of the purse to delete.

    Returns:
        None.
    """
    query = "UPDATE purse SET status = %s WHERE id = %s;"
    params = (False, purse_id)
    execute_query(query, params)
    return None


def get_all_purses_query() -> list:
    """
    Retrieves all purses from the database.

    Returns:
        List[DictRow]: The retrieved purses.
    """
    query = "SELECT * FROM purse WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
