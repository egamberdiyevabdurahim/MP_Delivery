from queries.for_category import get_all_categories_query, get_category_from_id_query

from queries.for_company import (get_all_companies_query, get_company_from_id_query,
                                 get_company_from_manager_id_query)

from queries.for_products import insert_product_query, get_all_products_query
from queries.for_products import update_product_query, delete_product_query
from queries.for_products import search_product

from queries.for_branch import insert_branch_query, get_all_branches_query
from queries.for_branch import update_branch_query, delete_branch_query
from queries.for_branch import search_branch

from queries.for_employee import insert_employee_query, get_all_employees_query
from queries.for_employee import update_employee_query, delete_employee_query
from queries.for_employee import search_employee

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
            show_products()
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '3':
        if role == "Product":
            update_product(email=email)
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '4':
        if role == "Product":
            search_product_()
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '5':
        if role == "Product":
            delete_product()
        elif role == "Branch":
            pass
        else:
            pass
    elif user_input == '6':
        manager_menu(email)
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
        menu(role="Product", email=email)
    elif user_input == '2':
        menu(role="Branch", email=email)
    elif user_input == '3':
        menu(role="Employee", email=email)
    elif user_input == '4':
        pass
    else:
        print("Invalid choice. Please try again")
        return manager_menu(email)
    
                                
                                            #Product functions
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

        category_id: str = input("Enter your category ID: ")
        # Check if the category exists
        while not get_category_from_id_query(int(category_id)):
            print("Invalid category ID!")
            category_id = input("Re-Enter your category ID: ")
        
        user_data = get_user_from_email_query(email)
        manager_id = user_data['id']
        company_data = get_company_from_manager_id_query(manager_id)

    insert_product_query(category_id=int(category_id), name=product_name, price=int(product_price), company_id=company_data['id'])
    print(f"\nCreated Successfully!") 
    return None


def show_products():
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
                         price=int(product_price), company_id=company_data['id'])

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


def search_product_(l):
    """
    Search a product from the products table.
    """
    product_id = int(input("Enter product ID: "))
    search_product(product_id=product_id)

    return None

                                            #Brach functions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                

def add_branch(email):
    """
    Add a new branch to the branchs table.
    """
    id_name = input("Enter should branch ID name: ").strip()
        
    user_data = get_user_from_email_query(email)
    manager_id = user_data['id']
    company_data = get_company_from_manager_id_query(manager_id)

    insert_branch_query(id_name=id_name, company_id=company_data['id'])
    print(f"\nCreated Successfully!") 
    return None


def show_branchs():
    """
    Show all branchs in the branchs table.
    """
    result = get_all_branches_query()
    if result:
        print("branch:")
        for branch in result:
            print(f"""ID: {branch[0]}, ID name: {branch[1]}, Company ID: {branch[2]}, 
                    Status: {branch[3]}, Created at: {branch[4]}""")
    else:
        print("No branchs found.")
    return None


def update_branch(email):

    """
    Update the company_id and id_name of a branch in the branch table.
    """
    branch_id = int(input("Enter branch Id: "))
    id_name = input("Enter should branch ID name: ").strip()
        
    user_data = get_user_from_email_query(email)
    manager_id = user_data['id']
    company_data = get_company_from_manager_id_query(manager_id)
        
    update_branch_query(branch_id=branch_id,id_name=id_name,company_id=company_data['id'])

    print(f"Update Successfully!")
    return None


def delete_branch():
    """
    Delete a branch from the branch table.
    """
    branch_id = int(input("Enter branhc ID: "))

    delete_branch_query(branch_id=branch_id)

    print(f"Delete Successfully!")
    return None


def search_branch_():
    """
    Search a branch from the branch table.
    """
    branch_id = int(input("Enter branch ID: "))
    search_branch(branch_id=branch_id)

    return None


                                            #Employee functions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                

def add_employee(email):
    """
    Add a new employee to the employee table.
    """
    id_name = input("Enter should branch ID name: ").strip()
        
    user_data = get_user_from_email_query(email)
    manager_id = user_data['id']
    company_data = get_company_from_manager_id_query(manager_id)

    insert_employee_query(id_name=id_name, company_id=company_data['id'])
    print(f"\nCreated Successfully!") 
    return None


def show_employees():
    """
    Show all employees in the employee table.
    """
    result = get_all_employees_query()
    if result:
        print("branch:")
        for branch in result:
            print(f"""ID: {branch[0]}, ID name: {branch[1]}, Company ID: {branch[2]}, 
                    Status: {branch[3]}, Created at: {branch[4]}""")
    else:
        print("No branchs found.")
    return None


def update_employee(email):

    """
    Update the company_id and id_name of a employee in the branch table.
    """
    branch_id = int(input("Enter branch Id: "))
    id_name = input("Enter should branch ID name: ").strip()
        
    user_data = get_user_from_email_query(email)
    manager_id = user_data['id']
    company_data = get_company_from_manager_id_query(manager_id)
        
    update_employee_query(branch_id=branch_id,id_name=id_name,company_id=company_data['id'])

    print(f"Update Successfully!")
    return None


def delete_employee():
    """
    Delete a branch from the branch table.
    """
    branch_id = int(input("Enter branhc ID: "))

    delete_employee_query(branch_id=branch_id)

    print(f"Delete Successfully!")
    return None


def search_employee_():
    """
    Search a employee from the branch table.
    """
    branch_id = int(input("Enter branch ID: "))
    search_employee_(branch_id=branch_id)

    return None
