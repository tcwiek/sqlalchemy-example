from sqlalchemy import create_engine
#
#
# # new*
# def main():
#     engine = create_engine(
#         "mysql+pymysql://root:tomasz@localhost:3306/company"
#         )
#     sql = "SELECT * FROM company.archived_users"
#
#     result = engine.execute(sql)
#     rows = result.fetchall()
#     for row in rows:
#         print(row)
#     # print(result)
#
#
# if __name__ == "__main__":
#     main()
#


# new*
def main():
    login = "root"
    password = "tomasz"
    host = "localhost"
    port = "3306"
    dbname = "company"

    engine = create_engine(
        f"mysql+pymysql://{login}:{password}@{host}:{port}/{dbname}"
        )
    sql = "SELECT * FROM company.archived_users"

    with engine.connect() as conn:
        result = conn.execute(sql)
        for row in result:
            print(row)


if __name__ == "__main__":
    main()