# Работа с базами данных

### В рамках проекта получаем данные о компаниях и вакансиях с сайта hh.ru, проектируем таблицы в БД PostgreSQL и загружаем полученные данные в созданные таблицы.
 
### Для работы с БД нужно указать свои значения, а именно хост, саму БД, название новой БД, имя и пароль пользователя, а также порт.

---
| **Название файла** | **Содержание файла**                                                                                                        |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| utils.py           | <li>Подключение к апи hh.ru. <li>Получение данных о работодателях и их вакансиях. <li>Функции заполняйщие данные в БД       |
| db_manager.py      | <li>Cодержит в себе одноименный класс. <li>Осуществление взаимодействий с БД. <li>Подключение и выбор необходимых вакансий. |
| main.py            | <li>Взаимодействие с пользователем                                                                                          |
 | queries.sql        | <li>SQL запросы для портала                                                                                                 | 
 | settings.py        | <li>Файл с переменными окружения для подключения к БД                                                                       |
