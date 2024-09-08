from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_promocode_table_query() -> None:
    """
    Creates a table for storing promocodes.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS promocode (
        id BIGSERIAL PRIMARY KEY,
        code VARCHAR(64) NOT NULL UNIQUE,
        discount_percent INT NOT NULL,
        user_id BIGINT REFERENCES users(id) NOT NULL,
        minimum_price BIGINT NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        end_date TIMESTAMPTZ NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_promocode_from_id_query(promocode_id: int) -> DictRow:
    """
    Retrieves a promocode from the database by its ID.

    Args:
        promocode_id (int): The ID of the promocode to retrieve.

    Returns:
        DictRow: The retrieved promocode.
    """
    query = "SELECT * FROM promocode WHERE id = %s AND status = %s;"
    params = (promocode_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_promocode_from_code_query(code: str) -> DictRow:
    """
    Retrieves a promocode from the database by its code.

    Args:
        code (str): The code of the promocode to retrieve.

    Returns:
        DictRow: The retrieved promocode.
    """
    query = "SELECT * FROM promocode WHERE code = %s AND status = %s;"
    params = (code, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_active_promocodes_query() -> list:
    """
    Retrieves active promocodes from the database.

    Returns:
        list: The retrieved active promocodes.
    """
    query = "SELECT * FROM promocode WHERE is_active = %s AND status = %s;"
    params = (True, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_promocodes_from_user_id(user_id: int) -> list:
    """
    Retrieves promocodes associated with a user from the database.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list: The retrieved promocodes.
    """
    query = "SELECT * FROM promocode WHERE user_id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def insert_promocode_query(code: str, discount_percent: int, user_id: int, minimum_price: int, end_date: str) -> None:
    """
    Inserts a new promocode into the database.

    Args:
        code (str): The code of the new promocode.
        discount_percent (int): The discount percentage of the new promocode.
        user_id (int): The ID of the user associated with the new promocode.
        minimum_price (int): The minimum price for using the new promocode.
        end_date (str): The end date of the new promocode.
    """
    query = """
    INSERT INTO promocode (code, discount_percent, user_id, minimum_price, end_date)
    VALUES (%s, %s, %s, %s, %s);
    """
    params = (code, discount_percent, user_id, minimum_price, end_date)
    execute_query(query, params)
    return None


def disable_promocode_query(promocode_id: int) -> None:
    """
    Disables a promocode in the database.

    Args:
        promocode_id (int): The ID of the promocode to disable.
    """
    query = "UPDATE promocode SET is_active = %s WHERE id = %s;"
    params = (False, promocode_id)
    execute_query(query, params)
    return None


def delete_promocode_query(promocode_id: int):
    """
    Deletes a promocode from the database.

    Args:
        promocode_id (int): The ID of the promocode to delete.
    """
    query = "UPDATE promocode SET status = %s WHERE id = %s;"
    params = (False, promocode_id)
    execute_query(query, params)
    return None


def get_all_promocodes_query() -> list:
    """
    Retrieves all promocodes from the database.

    Returns:
        list: The retrieved promocodes.
    """
    query = "SELECT * FROM promocode WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
