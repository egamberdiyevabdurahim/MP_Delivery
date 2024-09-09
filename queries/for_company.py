from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_company_table_query() -> None:
    """
    Creates a table for storing company.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS company (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE,
        manager_id BIGINT REFERENCES users(id) NOT NULL,
        contribution_percent_for_siystem BIGINT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_company_from_id_query(company_id: int) -> DictRow:
    """
    Retrieves a company from the database by its ID.

    Args:
        company_id (int): The ID of the company to retrieve.

    Returns:
        DictRow: The retrieved company.
    """
    query = "SELECT * FROM company WHERE id = %s AND status = %s;"
    params = (company_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_company_from_name_query(name: str) -> DictRow:
    """
    Retrieves a company from the database by its name.

    Args:
        name (str): The name of the company to retrieve.

    Returns:
        DictRow: The retrieved company.
    """
    query = "SELECT * FROM company WHERE name = %s AND status = %s;"
    params = (name, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_company_from_manager_id_query(manager_id: int) -> list:
    """
    Retrieves a company from the database by its manager ID.

    Args:
        manager_id (int): The ID of the manager associated with the company.

    Returns:
        DictRow: The retrieved company.
    """
    query = "SELECT * FROM company WHERE manager_id = %s AND status = %s;"
    params = (manager_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def insert_company_query(name: str, manager_id: int, contribution_percent_for_system: int) -> None:
    """
    Inserts a new company into the database.

    Args:
        name (str): The name of the new company.
        manager_id (int): The ID of the manager associated with the company.
        contribution_percent_for_system (int): The percentage of the company's contribution to the system.
    """
    query = """
    INSERT INTO company (name, manager_id, contribution_percent_for_system)
    VALUES (%s, %s, %s);
    """
    params = (name, manager_id, contribution_percent_for_system)
    execute_query(query, params)
    return None


def update_company_query(company_id: int, name: str, manager_id: int, contribution_percent_for_system: int) -> None:
    """
    Updates a company's information in the database.

    Args:
        company_id (int): The ID of the company to update.
        name (str): The new name of the company.
        manager_id (int): The new ID of the manager associated with the company.
        contribution_percent_for_system (int): The new percentage of the company's contribution to the system.
    """
    query = """
    UPDATE company
    SET name = %s, manager_id = %s, contribution_percent_for_system = %s
    WHERE id = %s AND status = %s;
    """
    params = (name, manager_id, contribution_percent_for_system, company_id, True)
    execute_query(query, params)
    return None


def delete_company_query(company_id: int) -> None:
    """
    Deletes a company from the database.

    Args:
        company_id (int): The ID of the company to delete.
    """
    query = "UPDATE company SET status = %s WHERE id = %s;"
    params = (False, company_id)
    execute_query(query, params)
    return None


def get_all_companies_query() -> list:
    """
    Retrieves all companies from the database.

    Returns:
        List[DictRow]: The retrieved companies.
    """
    query = "SELECT * FROM company WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params)
    return result
