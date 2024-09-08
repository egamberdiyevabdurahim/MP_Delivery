from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_products_table_query() -> None:
    """
    Creates a table for storing products.
    """
    execute_query("""
    CREATE TABLE IF NOT EXISTS products (
        id BIGSERIAL PRIMARY KEY,
        category_id BIGINT REFERENCES category(id) NOT NULL,
        name VARCHAR(255) NOT NULL,
        price BIGINT NOT NULL,
        company_id BIGINT REFERENCES company(id) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW(),
        status BOOLEAN DEFAULT TRUE
    );
    """)
    return None


def get_product_from_id_query(product_id: int) -> DictRow:
    """
    Retrieves a product from the database by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        DictRow: The retrieved product.
    """
    query = "SELECT * FROM products WHERE id = %s AND status = %s;"
    params = (product_id, True)
    result = execute_query(query, params, fetch='one')
    return result


def get_products_from_category_id_query(category_id: int) -> list:
    """
    Retrieves products from the database by their category ID.

    Args:
        category_id (int): The ID of the category.

    Returns:
        list: The retrieved products.
    """
    query = "SELECT * FROM products WHERE category_id = %s AND status = %s;"
    params = (category_id, True)
    result = execute_query(query, params, fetch='all')
    return result


def get_products_from_company_id_query(company_id: int) -> list:
    """
    Retrieves products from the database by their company ID.

    Args:
        company_id (int): The ID of the company.

    Returns:
        list: The retrieved products.
    """
    query = "SELECT * FROM products WHERE company_id = %s AND status = %s;"
    params = (company_id, True)
    result = execute_query(query, params, fetch='all')
    return result


# def get_products_by_search_query(search_term: str) -> list:
#     """
#     Retrieves products from the database by a search term.
#
#     Args:
#         search_term (str): The search term.
#
#     Returns:
#         list: The retrieved products.
#     """
#     query = """
#     SELECT * FROM products
#     WHERE name ILIKE %s OR category_id IN (
#         SELECT id FROM category WHERE name ILIKE %s
#     ) OR company_id IN (
#         SELECT id FROM company WHERE name ILIKE %s
#     ) AND status = %s;
#     """
#     params = (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', True)
#     result = execute_query(query, params, fetch='all')
#     return result


def insert_product_query(category_id: int, name: str, price: int, company_id: int) -> None:
    """
    Inserts a new product into the database.

    Args:
        category_id (int): The ID of the product's category.
        name (str): The name of the product.
        price (int): The price of the product.
        company_id (int): The ID of the product's company.
    """
    query = "INSERT INTO products (category_id, name, price, company_id) VALUES (%s, %s, %s, %s);"
    params = (category_id, name, price, company_id)
    execute_query(query, params)
    return None


def update_product_query(product_id: int, category_id: int, name: str, price: int, company_id: int) -> None:
    """
    Updates an existing product in the database.

    Args:
        product_id (int): The ID of the product to update.
        category_id (int): The new ID of the product's category.
        name (str): The new name of the product.
        price (int): The new price of the product.
        company_id (int): The new ID of the product's company.
    """
    query = """
    UPDATE products
    SET category_id = %s, name = %s, price = %s, company_id = %s, updated_at = NOW()
    WHERE id = %s AND status = %s;
    """
    params = (category_id, name, price, company_id, product_id, True)
    execute_query(query, params)
    return None


def delete_product_query(product_id: int) -> None:
    """
    Deletes a product from the database.

    Args:
        product_id (int): The ID of the product to delete.
    """
    query = "UPDATE products SET status = %s WHERE id = %s;"
    params = (False, product_id)
    execute_query(query, params)
    return None


def get_all_products_query() -> list:
    """
    Retrieves all products from the database.

    Returns:
        list: The retrieved products.
    """
    query = "SELECT * FROM products WHERE status = %s;"
    params = (True,)
    result = execute_query(query, params, fetch='all')
    return result
