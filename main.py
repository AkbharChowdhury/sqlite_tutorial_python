import sqlite3
from contextlib import closing


class Database:
    def __db_name(self):
        return 'hr.db'

    def fetch_employees(self):
        with sqlite3.connect(self.__db_name()) as con:
            con.row_factory = sqlite3.Row
            with closing(con.cursor()) as cur:
                cur.execute('SELECT employee_id, firstname, lastname FROM employees')
                return [dict(row) for row in cur.fetchall()]

    def add_employees(self, data: list[tuple['str', 'str']]):
        with sqlite3.connect(self.__db_name()) as con:
            with closing(con.cursor()) as cur:
                cur.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", data)

    def add_employees_dict(self, data: list[dict['str', 'str']]):
        with sqlite3.connect(self.__db_name()) as con:
            with closing(con.cursor()) as cur:
                cur.executemany("INSERT INTO employees(firstname, lastname) VALUES(:firstname, :lastname)", data)


def main():
    db = Database()
    # db.add_employees([
    #     ('John','Smith'),
    #     ('Joe','Smith')
    # ])

    # db.add_employees_dict([
    #     {'firstname': 'Barry', 'lastname': 'Smith'},
    #     {'firstname': 'Amy', 'lastname': 'Larson'},
    # ])
    print(db.fetch_employees())
    employees = db.fetch_employees()
    print('list of employees'.capitalize())
    print('--------------------------------')
    for emp in sorted(employees, key=lambda x: x['firstname']):
        print(f'{emp.get('firstname')} {emp.get('lastname')}'.title())


if __name__ == '__main__':
    main()
# con = sqlite3.connect("tutorial.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())
# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# print(res.fetchone() is None)
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# con.commit()
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.
# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)
# con.close()
# new_con = sqlite3.connect("tutorial.db")
# new_cur = new_con.cursor()
# res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC LIMIT 1")
# title, year = res.fetchone()
# print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
