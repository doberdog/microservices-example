import psycopg2


# noinspection PyRedundantParentheses
class LogDbWriter:
    def __init__(self):
        pass

    def create_tables(self):
        """ create Tables in the PostgreSQL database"""
        commands = ("CREATE TABLE vendors (vendor_id SERIAL PRIMARY KEY, vendor_name VARCHAR(255) NOT NULL)",)
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            for command in commands:
                cur.execute(command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    if __name__ == '__main__':
        create_tables()
