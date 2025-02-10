import sqlite3
from contextlib import closing


class Database:
    def __db_name(self):
        return 'hr.db'

    def fetch_employees(self):
        with sqlite3.connect(self.__db_name()) as con:
            con.row_factory = sqlite3.Row
            with closing(con.cursor()) as cursor:
                cursor.execute('SELECT employee_id, firstname, lastname FROM employees')
                return [dict(row) for row in cursor.fetchall()]


def main():
    db = Database()
    employees = db.fetch_employees()
    print('list of employees'.capitalize())
    print('--------------------------------')
    for emp in sorted(employees, key=lambda x: x['firstname']):
        print(f'{emp.get('firstname')} {emp.get('lastname')}'.title())


if __name__ == '__main__':
    main()
