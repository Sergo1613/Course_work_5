from utils import get_data_vacancies, get_employers_data
from db_manager import DBManager
import psycopg2
from settings import HOST, DATABASE, DB_NAME, USER, PASSWORD, PORT

db_manager = DBManager(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)

db_manager.create_database("hh")  # создание БД с названием HH
db_manager.create_tables()  # создание таблиц

vacancies_data = get_data_vacancies()
employers_data = get_employers_data()

db_manager.save_employers_to_db(employers_data)
db_manager.save_vacancies_to_db(vacancies_data)

db_manager.get_companies_and_vacancies_count()
db_manager.get_avg_salary()
db_manager.get_all_vacancies()
db_manager.get_vacancies_with_higher_salary()
db_manager.get_vacancies_with_keyword("python")