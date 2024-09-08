import os

from database_config.db_settings import execute_query

from for_purse import create_purse_table_query
from for_regions import create_regions_table_query
from for_user_role import create_user_role_table_query
from for_users import create_users_table_query
from for_courier import create_courier_table_query
from for_promocode import create_promocode_table_query
from for_company import create_company_table_query
from for_branch import create_branch_table_query
from for_employee import create_employee_table_query
from for_category import create_category_table_query
from for_products import create_products_table_query
from for_basket import create_basket_table_query
from for_basket_item import create_basket_item_table_query
from for_order import create_order_table_query
from for_order_item import create_order_item_table_query

def create_is_used_table_query() -> None:
    """
    Creates a new table for tracking whether the application is already run.
    """
    query = """
        CREATE TABLE IF NOT EXISTS is_used (
            id BIGSERIAL PRIMARY KEY,
            is_used BOOLEAN DEFAULT FALSE
        );
    """
    execute_query(query)
    return None


def insert_is_used_query():
    """
    Inserts a new record into the is_used table.
    """
    query = """
        SELECT * FROM is_used
        ORDER BY id DESC
        LIMIT 1;
        """
    data = execute_query(query, fetch="one")
    if data is None:
        query = "INSERT INTO is_used (is_used) VALUES (False);"
        execute_query(query)
    return None


def update_is_used_query():
    """
    Updates the is_used column in the is_used table.
    """
    query = "UPDATE is_used SET is_used = TRUE;"
    execute_query(query)
    return None


def is_used():
    query = """
    SELECT * FROM is_used
    ORDER BY id DESC
    LIMIT 1;
    """
    data = execute_query(query, fetch="one")
    return data['is_used'] is True


def before_run() -> None:
    """
    Creates all required tables before running the application.
    """
    create_purse_table_query()
    create_regions_table_query()
    create_user_role_table_query()
    create_users_table_query()
    create_courier_table_query()
    create_promocode_table_query()
    create_company_table_query()
    create_branch_table_query()
    create_employee_table_query()
    create_category_table_query()
    create_products_table_query()
    create_basket_table_query()
    create_basket_item_table_query()
    create_order_table_query()
    create_order_item_table_query()
    return None


def if_not_used():
    path = os.path.join(os.path.dirname(__file__),)
    create_is_used_table_query()
    insert_is_used_query()
    if not is_used():
        before_run()

        with open(f"{path}/inserter_for_roles.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_region.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_category.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        update_is_used_query()

    return None
