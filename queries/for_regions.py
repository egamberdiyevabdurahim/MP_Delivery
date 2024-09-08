from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_regions_table_query() -> None:
    """
    Creates a table for storing regions.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS regions (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE
    );
    """)
    return None


def get_region_from_id_query(region_id: int) -> DictRow:
    """
    Retrieves a region from the database by its ID.

    Args:
        region_id (int): The ID of the region to retrieve.

    Returns:
        DictRow: The retrieved region.
    """
    query = f"SELECT * FROM regions WHERE id = %s AND status = %s;"
    params = (region_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_region_from_name_query(name: str) -> DictRow:
    """
    Retrieves a region from the database by its name.

    Args:
        name (str): The name of the region to retrieve.

    Returns:
        DictRow: The retrieved region.
    """
    query = f"SELECT * FROM regions WHERE name = %s AND status = %s;"
    params = (name, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_region_query(name: str) -> None:
    """
    Inserts a new region into the database.

    Args:
        name (str): The name of the new region.

    Returns:
        None.
    """
    query = "INSERT INTO regions (name) VALUES (%s);"
    params = (name,)
    execute_query(query, params)
    return None


def update_region_query(region_id: int, name: str) -> None:
    """
    Updates a region's name in the database.

    Args:
        region_id (int): The ID of the region to update.
        name (str): The new name of the region.

    Returns:
        None.
    """
    query = "UPDATE regions SET name = %s WHERE id = %s AND status = %s;"
    params = (name, region_id, True)
    execute_query(query, params)
    return None


def delete_region_query(region_id: int) -> None:
    """
    Deletes a region from the database.

    Args:
        region_id (int): The ID of the region to delete.

    Returns:
        None.
    """
    query = "UPDATE regions SET status = %s WHERE id = %s;"
    params = (False, region_id)
    execute_query(query, params)
    return None


def get_all_regions_query() -> list:
    """
    Retrieves all regions from the database.

    Returns:
        List[DictRow]: The retrieved regions.
    """
    query = "SELECT * FROM regions WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
