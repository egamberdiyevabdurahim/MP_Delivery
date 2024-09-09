import threading
import hashlib


from queries.for_category import get_all_categories_query, get_category_from_id_query

from queries.for_company import (get_all_companies_query, get_company_from_id_query,
                                 get_company_from_manager_id_query)

from queries.for_products import insert_product_query, get_all_products_query
from queries.for_products import update_product_query, delete_product_query
from queries.for_products import search_product

from queries.for_users import get_user_from_email_query


def menu(role, email):
    print(""""
    1. Create
    2. See all
    3. Update
    4. Search
    5. Delete
    6. Logout
    """)

    user_input = input("Enter your choice: ")
    if user_input == '1':
        if role == "Product":
            add_product(email=email)
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '2':
        if role == "Product":
            pass
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '3':
        if role == "Product":
            pass
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '4':
        if role == "Product":
            pass
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '5':
        if role == "Product":
            pass
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '6':
        manager_menu()
    else:
        print("Invalid choice. Please try again")
    return menu(role=role, email=email)
    

def manager_menu(email):
    print("""
1. Product management(CRUD)
2. Branch management(CRUD)
3. Employee management(CRUD)
4. Logout
""")
    user_input = input("Enter your choice: ")
    if user_input == '1':
        menu(role="Product")
    elif user_input == '2':
        menu(role="Branch")
    elif user_input == '3':
        menu(role="Employee")
    elif user_input == '4':
        pass
    else:
        print("Invalid choice. Please try again")
        return manager_menu()
    
                                
                                            #Products functions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def add_product(email):
    """
    Add a new product to the products table.
    """
    product_name = input("Enter product name: ").strip()
    product_price = input("Enter product price: ").strip()
    category_data = get_all_categories_query()
    for category in category_data:
        print(f"{category['id']}. {category['name']}")

        category_id: int = int(input("Enter your category ID: "))
        # Check if the category exists
        while not get_category_from_id_query(category_id):
            print("Invalid category ID!")
            category_id = int(input("Re-Enter your category ID: "))
        
        user_data = get_user_from_email_query(email)
        manager_id = user_data['id']
        company_data = get_company_from_manager_id_query(manager_id)

    insert_product_query(category_id=category_id,name=product_name,price=product_price, company_id=company_data['id'])
    print(f"\nCreated Successfully!") 
    return None


def show_products(email):
    """
    Show all products in the products table.
    """
    result = get_all_products_query()
    if result:
        print("Products:")
        for product in result:
            print(f"""ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, 
                    Category ID: {product[3]}, Company ID: {product[4]}""")
    else:
        print("No products found.")
    return None


def update_product(email):

    """
    Update the name and price of a product in the products table.
    """
    product_id = int(input("Enter product Id: "))
    product_name = input("Enter new product name: ")
    product_price = input("Enter new product price: ")
    category_data = get_all_categories_query()
    for category in category_data:
        print(f"{category['id']}. {category['name']}")

        category_id: int = int(input("Enter your new category ID: "))
        # Check if the category exists
        while not get_category_from_id_query(category_id):
            print("Invalid category ID!")
            category_id = int(input("Re-Enter your new category ID: "))
        
        user_data = get_user_from_email_query(email)
        manager_id = user_data['id']
        company_data = get_company_from_manager_id_query(manager_id)
        
    update_product_query(product_id=product_id,category_id=category_id,name=product_name,
                         price=product_price, company_id=company_data['id'])

    print(f"Update Successfully!")
    return None


def delete_product():
    """
    Delete a product from the products table.
    """
    product_id = int(input("Enter product ID: "))
    delete_product_query(product_id=product_id)

    print(f"Delete Successfully!")
    return None


def search_product_():
    """
    Search a product from the products table.
    """
    product_id = int(input("Enter product ID: "))
    search_product(product_id=product_id)

    return None


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""