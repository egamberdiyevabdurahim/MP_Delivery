from colorama import Fore, init

init(autoreset=True)

success = Fore.LIGHTGREEN_EX


from queries.for_super_admin import (total_number_of_employees_query, number_of_employees_by_department_query,
                                     number_of_employees_by_company_query, number_of_users_by_role_query,
                                     number_of_employees_by_age_query, number_of_employees_by_gender_query,
                                     number_of_employees_by_region_query, number_of_employees_by_birth_date_query,
                                     number_of_employees_by_salary_query, number_of_10_employees_by_highest_salary_query,
                                     number_of_10_employees_by_lowest_salary_query, total_salary_for_all_employees_query,
                                     average_salary_for_all_employees_query, total_salary_in_each_company_query,
                                     average_salary_in_each_company_query, total_salary_in_each_department_query,
                                     average_salary_in_each_department_query, total_salary_in_each_region_query,
                                     average_salary_in_each_region_query, total_salary_in_each_role_query,
                                     average_salary_in_each_role_query, total_salary_in_each_age_query,
                                     average_salary_in_each_age_query, total_salary_in_each_gender_query,
                                     average_salary_in_each_gender_query, total_salary_in_each_birth_date_query,
                                     average_salary_in_each_birth_date_query, total_salary_in_same_salary_query,
                                     average_salary_in_same_salary_query, show_all_users_query,
                                     show_all_companies_query, show_all_departments_query,
                                     show_all_regions_query, show_all_roles_query,
                                     sum_of_all_ages_query, all_users_by_older_to_younger_query,
                                     all_users_by_younger_to_older_query, all_users_by_new_hired_to_old_hired_query,
                                     all_users_by_old_hired_to_new_hired_query, all_users_by_starts_with_letter_query,
                                     all_users_by_starts_with_letter2_query, all_users_by_starts_with_letter_endswith_letter_query,
                                     all_users_by_ends_with_letter_query, all_users_by_ends_with_letter2_query,
                                     all_users_by_born_after_2020_query, all_users_by_born_before_2020_query,
                                     all_users_by_hired_after_2020_query, all_users_by_hired_before_2020_query,
                                     all_companies_created_after_2020_query, all_companies_created_before_2020_query,
                                     all_departments_created_after_2020_query, all_departments_created_before_2020_query)

from utils.printer import user_printer, company_printer, department_printer


def statistics_menu():
    """
    Handles the statistics menu for a specific user.
    """
    print(f"\n1. Total number of employees\n"
          "2. Number of employees by department\n"
          "3. Number of employees by company\n"
          "4. Number of users by role\n"
          "5. Number of employees by age\n"
          "6. Number of employees by gender\n"
          "7. Number of employees by region\n"
          "8. Number of employees by birth date\n"
          "9. Number of employees by salary\n"
          "10. Number of 10 employees by highest salary\n"
          "11. Number of 10 employees by lowest salary\n"
          "12. Total Salary for all employees\n"
          "13. Average Salary for all employees\n"
          "14. Total Salary in each companies\n"
          "15. Average Salary in each companies\n"
          "16. Total Salary in each departments\n"
          "17. Average Salary in each departments\n"
          "18. Total Salary in each regions\n"
          "19. Average Salary in each regions\n"
          "20. Total Salary in each roles\n"
          "21. Average Salary in each roles\n"
          "22. Total Salary in each ages\n"
          "23. Average Salary in each ages\n"
          "24. Total Salary in each genders\n"
          "25. Average Salary in each genders\n"
          "26. Total Salary in each birth dates\n"
          "27. Average Salary in each birth dates\n"
          "28. Total Salary in each same salaries\n"
          "29. Average Salary in each same salaries\n"
          "30. Show All Users\n"
          "31. Show All Companies\n"
          "32. Show All Departments\n"
          "33. Show All Roles\n"
          "34. Show All Regions\n"
          "35. Sum of All Ages\n"
          "36. All Users by Older to Younger\n"
          "37. All Users by Younger to Older\n"
          "38. All Users by New Hired to Old Hired\n"
          "39. All Users by Old Hired to New Hired\n"
          "40. All Users By Name that starts with a, b, c\n"
          "41. All Users By Name that starts with d, e, f\n"
          "42. All Users By Name that starts with g, h, i\n"
          "43. All Users By Name that starts with j, k, l\n"
          "44. All Users By Name that starts with m, n, o\n"
          "45. All Users By Name that starts with p, q, r\n"
          "46. All Users By Name that starts with s, t, u\n"
          "47. All Users By Name that starts with v, w, x\n"
          "48. All Users By Name that starts with y, z\n"
          "49. All Users By Name that starts with a and ends with e\n"
          "50. All Users By Name that starts with b and ends with e\n"
          "51. All Users By Name that starts with c and ends with e\n"
          "52. All Users By Name that ends with a, b, c\n"
          "53. All Users By Name that ends with d, e, f\n"
          "54. All Users By Name that ends with g, h, i\n"
          "55. All Users By Name that ends with j, k, l\n"
          "56. All Users By Name that ends with m, n, o\n"
          "57. All Users By Name that ends with p, q, r\n"
          "58. All Users By Name that ends with s, t, u\n"
          "59. All Users By Name that ends with v, w, x\n"
          "60. All Users By Name that ends with y, z\n"
          "61. All Users By Name that starts with a and ends with d\n"
          "62. All Users By Name that starts with b and ends with d\n"
          "63. All Users By Name that starts with c and ends with d\n"
          "64. All Users Born After 2020\n"
          "65. All Users Born Before 2020\n"
          "66. All Employees Hired after 2020\n"
          "67. All Employees Hired before 2020\n"
          "68. All Companies Created after 2020\n"
          "69. All Companies Created before 2020\n"
          "70. All Departments Created after 2020\n"
          "71. All Departments Created before 2020\n"
          "72. Back\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = total_number_of_employees_query()
        print(success+f"\nTotal number of employees: {data[0]}\n")

    elif choice == '2':
        data = number_of_employees_by_department_query()
        print(success+f"Departments | Amount")
        for dat in data:
            print(success+f"{dat[0]} | {dat[1]}")

    elif choice == '3':
        data = number_of_employees_by_company_query()
        print(success + f"Company | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '4':
        data = number_of_users_by_role_query()
        print(success + f"Role | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '5':
        data = number_of_employees_by_age_query()
        print(success + f"Age | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '6':
        data = number_of_employees_by_gender_query()
        print(success + f"Gender | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '7':
        data = number_of_employees_by_region_query()
        print(success + f"Region | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '8':
        data = number_of_employees_by_birth_date_query()
        print(success + f"BirthDate | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '9':
        data = number_of_employees_by_salary_query()
        print(success + f"Salary | Amount")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '10':
        data = number_of_10_employees_by_highest_salary_query()
        print("FirstName | LastName | Salary")
        for dat in data:
            print(success+f"{dat['first_name']} | {dat['last_name']} | {dat['salary']}")

    elif choice == '11':
        data = number_of_10_employees_by_lowest_salary_query()
        print("FirstName | LastName | Salary")
        for dat in data:
            print(success + f"{dat['first_name']} | {dat['last_name']} | {dat['salary']}")

    elif choice == '12':
        data = total_salary_for_all_employees_query()
        print(success+f"Total Salary For All Employees: {data[0]}")

    elif choice == '13':
        data = average_salary_for_all_employees_query()
        print(success+f"Average Salary For All Employees: {data[0]}")

    elif choice == '14':
        data = total_salary_in_each_company_query()
        print(success+f"Company | Total Salary")
        for dat in data:
            print(success+f"{dat[0]} | {dat[1]}")

    elif choice == '15':
        data = average_salary_in_each_company_query()
        print(success + f"Company | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '16':
        data = total_salary_in_each_department_query()
        print(success + f"Department | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '17':
        data = average_salary_in_each_department_query()
        print(success + f"Department | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '18':
        data = total_salary_in_each_region_query()
        print(success + f"Region | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '19':
        data = average_salary_in_each_region_query()
        print(success + f"Region | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '20':
        data = total_salary_in_each_role_query()
        print(success + f"Role | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '21':
        data = average_salary_in_each_role_query()
        print(success + f"Role | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '22':
        data = total_salary_in_each_age_query()
        print(success + f"Age | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '23':
        data = average_salary_in_each_age_query()
        print(success + f"Age | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '24':
        data = total_salary_in_each_gender_query()
        print(success + f"Gender | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '25':
        data = average_salary_in_each_gender_query()
        print(success + f"Gender | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '26':
        data = total_salary_in_each_birth_date_query()
        print(success + f"BirthDate | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '27':
        data = average_salary_in_each_birth_date_query()
        print(success + f"BirthDate | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '28':
        data = total_salary_in_same_salary_query()
        print(success + f"Same Salary | Total Salary")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '29':
        data = average_salary_in_same_salary_query()
        print(success + f"Same Salary | Total Average")
        for dat in data:
            print(success + f"{dat[0]} | {dat[1]}")

    elif choice == '30':
        data = show_all_users_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '31':
        data = show_all_companies_query()
        print(success+"ID | Name | CreatedAt")
        for dat in data:
            print(success + f"{dat['id']} | {dat['name']} | {dat['created_at']}")

    elif choice == '32':
        data = show_all_departments_query()
        print(success+"ID | Name | CompanyID | CreatedAt")
        for dat in data:
            print(success + f"{dat['id']} | {dat['name']} | {dat['company_id']} | {dat['created_at']}")

    elif choice == '33':
        data = show_all_roles_query()
        print(success+"ID | Name")
        for dat in data:
            print(success + f"{dat['id']} | {dat['name']}")

    elif choice == '34':
        data = show_all_regions_query()
        print(success + "ID | Name")
        for dat in data:
            print(success + f"{dat['id']} | {dat['name']}")

    elif choice == '35':
        data = sum_of_all_ages_query()
        print(success + f"Sum of All Ages: {data[0]}")

    elif choice == '36':
        data = all_users_by_older_to_younger_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '37':
        data = all_users_by_younger_to_older_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '38':
        data = all_users_by_new_hired_to_old_hired_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '39':
        data = all_users_by_old_hired_to_new_hired_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '40':
        data = all_users_by_starts_with_letter_query('a', 'b', 'c')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '41':
        data = all_users_by_starts_with_letter_query('d', 'e', 'f')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '42':
        data = all_users_by_starts_with_letter_query('g', 'h', 'i')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '43':
        data = all_users_by_starts_with_letter_query('j', 'k', 'l')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '44':
        data = all_users_by_starts_with_letter_query('m', 'n', 'o')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '45':
        data = all_users_by_starts_with_letter_query('p', 'q', 'r')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '46':
        data = all_users_by_starts_with_letter_query('s', 't', 'u')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '47':
        data = all_users_by_starts_with_letter_query('v', 'w', 'x')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '48':
        data = all_users_by_starts_with_letter2_query('y', 'z')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '49':
        data = all_users_by_starts_with_letter_endswith_letter_query('a', 'e')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '50':
        data = all_users_by_starts_with_letter_endswith_letter_query('b', 'e')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '51':
        data = all_users_by_starts_with_letter_endswith_letter_query('c', 'e')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '52':
        data = all_users_by_ends_with_letter_query('a', 'b', 'c')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '53':
        data = all_users_by_ends_with_letter_query('d', 'e', 'f')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '54':
        data = all_users_by_ends_with_letter_query('g', 'h', 'i')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '55':
        data = all_users_by_ends_with_letter_query('j', 'k', 'l')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '56':
        data = all_users_by_ends_with_letter_query('m', 'n', 'o')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '57':
        data = all_users_by_ends_with_letter_query('p', 'q', 'r')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '58':
        data = all_users_by_ends_with_letter_query('s', 't', 'u')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '59':
        data = all_users_by_ends_with_letter_query('v', 'w', 'x')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '60':
        data = all_users_by_ends_with_letter2_query('y', 'z')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '61':
        data = all_users_by_starts_with_letter_endswith_letter_query('a', 'd')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '62':
        data = all_users_by_starts_with_letter_endswith_letter_query('b', 'd')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '63':
        data = all_users_by_starts_with_letter_endswith_letter_query('c', 'd')
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '64':
        data = all_users_by_born_after_2020_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '65':
        data = all_users_by_born_before_2020_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '66':
        data = all_users_by_hired_after_2020_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '67':
        data = all_users_by_hired_before_2020_query()
        print(
            success + "ID | FirstName | LastName | Email | Password | DateOfBirth | Gender | Role ID | Company ID | Salary | HiderDate")
        for dat in data:
            user_printer(dat)

    elif choice == '68':
        data = all_companies_created_after_2020_query()
        print(
            success + "ID | Company Name | Date Created")
        for dat in data:
            company_printer(dat)

    elif choice == '69':
        data = all_companies_created_before_2020_query()
        print(
            success + "ID | Company Name | Date Created")
        for dat in data:
            company_printer(dat)

    elif choice == '70':
        data = all_departments_created_after_2020_query()
        print(
            success + "ID | Department Name | CompanyID | Date Created")
        for dat in data:
            department_printer(dat)

    elif choice == '71':
        data = all_departments_created_before_2020_query()
        print(
            success + "ID | Department Name | CompanyID | Date Created")
        for dat in data:
            department_printer(dat)

    elif choice == '72':
        print("Backing...")
        super_admin_menu()

    else:
        print("Invalid choice. Please try again.")

    return statistics_menu()


def super_admin_menu():
    """
    Handles the admin menu for a specific user.
    """
    print(f"\nWelcome, Super Admin!\n"
          "1. Statistics\n"
          "2. Logout\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        statistics_menu()

    elif choice == '2':
        print("Logging out...")
        return None

    else:
        print("Invalid choice. Please try again.")

    return super_admin_menu()
