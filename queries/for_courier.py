from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_courier_table_query() -> None:
    """
    Creates a table for storing couriers.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS courier (
        id BIGSERIAL PRIMARY KEY,
        region_id INT(64) NOT NULL,
        phone_number VARCHAR(64) UNIQUE NOT NULL,
        user_id BIGINT REFERENCES users(id) UNIQUE NOT NULL,
        price_for_delivering BIGINT NOT NULL,
        purse_id BIGINT REFERENCES purse(id) NOT NULL
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_courier_from_id_query(courier_id: int) -> DictRow:
    """
    Retrieves a courier from the database by its ID.

    Args:
        courier_id (int): The ID of the courier to retrieve.

    Returns:
        DictRow: The retrieved courier.
    """
    query = "SELECT * FROM courier WHERE id = %s AND status = %s;"
    params = (courier_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_courier_from_phone_number_query(phone_number: str) -> DictRow:
    """
    Retrieves a courier from the database by their phone number.

    Args:
        phone_number (str): The phone number of the courier to retrieve.

    Returns:
        DictRow: The retrieved courier.
    """
    query = "SELECT * FROM courier WHERE phone_number = %s AND status = %s;"
    params = (phone_number, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_courier_from_user_id_query(user_id: int) -> DictRow:
    """
    Retrieves a courier from the database by their user ID.

    Args:
        user_id (int): The ID of the user associated with the courier.

    Returns:
        DictRow: The retrieved courier.
    """
    query = "SELECT * FROM courier WHERE user_id = %s AND status = %s;"
    params = (user_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_courier_query(region_id: int, phone_number: str, user_id: int, price_for_delivering: int, purse_id: int) -> None:
    """
    Inserts a new courier into the database.

    Args:
        region_id (int): The ID of the region the courier works in.
        phone_number (str): The phone number of the courier.
        user_id (int): The ID of the user associated with the courier.
        price_for_delivering (int): The price per delivery the courier charges.
        purse_id (int): The ID of the purse the courier has.
    """
    query = """
    INSERT INTO courier (region_id, phone_number, user_id, price_for_delivering, purse_id)
    VALUES (%s, %s, %s, %s, %s);
    """
    params = (region_id, phone_number, user_id, price_for_delivering, purse_id)
    execute_query(query, params)
    return None


def update_courier_query(courier_id: int, region_id: int, phone_number: str,
                         user_id: int, price_for_delivering: int, purse_id: int) -> None:
    """
    Updates a courier's information in the database.

    Args:
        courier_id (int): The ID of the courier to update.
        region_id (int): The new ID of the region the courier works in.
        phone_number (str): The new phone number of the courier.
        user_id (int): The new ID of the user associated with the courier.
        price_for_delivering (int): The new price per delivery the courier charges.
        purse_id (int): The new ID of the purse the courier has.
    """
    query = """
    UPDATE courier
    SET region_id = %s, phone_number = %s, user_id = %s, price_for_delivering = %s, purse_id = %s
    WHERE id = %s AND status = %s;
    """
    params = (region_id, phone_number, user_id, price_for_delivering, purse_id, courier_id, True)
    execute_query(query, params)
    return None


def delete_courier_query(courier_id: int) -> None:
    """
    Deletes a courier from the database.

    Args:
        courier_id (int): The ID of the courier to delete.
    """
    query = "UPDATE courier SET status = %s WHERE id = %s;"
    params = (False, courier_id)
    execute_query(query, params)
    return None


def get_all_couriers_query() -> list:
    """
    Retrieves all couriers from the database.

    Returns:
        List[DictRow]: The retrieved couriers.
    """
    query = "SELECT * FROM courier WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
