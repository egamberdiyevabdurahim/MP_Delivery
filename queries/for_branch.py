from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_branch_table_query() -> None:
    """
    Creates a table for storing branch.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS branch (
        id BIGSERIAL PRIMARY KEY,
        id_name VARCHAR(64) NOT NULL UNIQUE,
        company_id BIGINT REFERENCES company(id) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_branch_from_id_query(branch_id: int) -> DictRow:
    """
    Retrieves a branch from the database by its ID.

    Args:
        branch_id (int): The ID of the branch to retrieve.

    Returns:
        DictRow: The retrieved branch.
    """
    query = "SELECT * FROM branch WHERE id = %s AND status = %s;"
    params = (branch_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_branch_from_id_name_query(id_name: str) -> DictRow:
    """
    Retrieves a branch from the database by its ID name.

    Args:
        id_name (str): The ID name of the branch to retrieve.

    Returns:
        DictRow: The retrieved branch.
    """
    query = "SELECT * FROM branch WHERE id_name = %s AND status = %s;"
    params = (id_name, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_branches_from_company_id_query(company_id: int) -> list:
    """
    Retrieves branches associated with a company from the database.

    Args:
        company_id (int): The ID of the company.

    Returns:
        list: The retrieved branches.
    """
    query = "SELECT * FROM branch WHERE company_id = %s AND status = %s;"
    params = (company_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def insert_branch_query(id_name: str, company_id: int) -> None:
    """
    Inserts a new branch into the database.

    Args:
        id_name (str): The ID name of the new branch.
        company_id (int): The ID of the company associated with the branch.
    """
    query = """
    INSERT INTO branch (id_name, company_id)
    VALUES (%s, %s);
    """
    params = (id_name, company_id)
    execute_query(query, params)
    return None


def update_branch_query(branch_id: int, id_name: str, company_id: int) -> None:
    """
    Updates a branch's information in the database.

    Args:
        branch_id (int): The ID of the branch to update.
        id_name (str): The new ID name for the branch.
        company_id (int): The new ID of the company associated with the branch.
    """
    query = """
    UPDATE branch
    SET id_name = %s, company_id = %s, updated_at = NOW()
    WHERE id = %s AND status = %s;
    """
    params = (id_name, company_id, branch_id, True)
    execute_query(query, params)
    return None


def delete_branch_query(branch_id: int) -> None:
    """
    Deletes a branch from the database.

    Args:
        branch_id (int): The ID of the branch to delete.
    """
    query = "UPDATE branch SET status = %s WHERE id = %s;"
    params = (False, branch_id)
    execute_query(query, params)
    return None


def get_all_branches_query() -> list:
    """
    Retrieves all branches from the database.

    Returns:
        list: The retrieved branches.
    """
    query = "SELECT * FROM branch WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result


def search_branch(branch_id: int):
    """
    Search for branch in the branchs table.
    """
    query = "SELECT * FROM branch WHERE id LIKE %s;"
    result = execute_query(query, params=("%" + branch_id + "%",), fetch="all")
    if result:
        print("branch:")
        for branch in result:
            print(f"""ID: {branch[0]}, ID name: {branch[1]}, Company ID: {branch[2]}, 
                    Status: {branch[3]}, Created at: {branch[4]}""")
    else:
        print("No branch found.")
    return None