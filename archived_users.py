from sqlalchemy import create_engine


def main():
    engine = create_engine(
        "mysql+pymysql://root:tomasz@localhost:3306/company"
    )

    sql_statements = [
        """
        INSERT INTO company.archived_users (id, first_name, last_name, email)
        (
            SELECT * FROM company.users
        );
        """,
        "TRUNCATE company.users;"
    ]

    with engine.connect() as conn:
        for sql in sql_statements:
            conn.execute(sql)


if __name__ == '__main__':
    main()
