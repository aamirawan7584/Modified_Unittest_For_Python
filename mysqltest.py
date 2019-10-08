import mysql.connector
from _mysql_connector import MySQLError
from constants import query_test, host, database, user, password, query_runs_after, query_runs_before


def getname_suite(s):
    s = s.replace(')', '')
    return s.split('(')


def make_connection() -> object:
    # constants.py contains these constants
    conn = mysql.connector.connect(host=host, port=3306, database=database, user=user,
                                   password=password)
    return conn, conn.cursor()


def save_testruns_info_before(start_time, host_name):
    """
    inialize a new test Run in DB and save starttime and host_name
    other info adds to DB after test run completion
    :param start_time:start time of tests
    :param host_name: hostname
    :return:
    """
    conn, cursor = make_connection()
    args = (start_time, host_name)
    cursor.execute(query_runs_before, args)
    conn.commit()


def save_testruns_info_after(runs):
    """
    :param runs: a list containg info about a test
    """
    conn, cursor = make_connection()
    args = tuple(runs)
    cursor.execute(query_runs_after, args)
    conn.commit()


def get_runs_id() -> int:
    """
    this function is helper fucniton for gettign recently added run_id
    :return: recently added id of Runs table
    """
    conn, cursor = make_connection()
    cursor.execute("SELECT MAX(run_id) FROM Runs")
    val = cursor.fetchall()
    x = val[0]
    return x[0]


def save_results(resultss: list) -> None:
    """

    :param resultss: test runner list of results of tests
    :return: NONE
    saves results in DB
    """
    conn, cursor = make_connection()
    try:

        for result in resultss:
            name_suitename = getname_suite(result[0])
            args = (name_suitename[0], name_suitename[1], result[3], result[2],get_runs_id())
            cursor.execute(query_test, args)
            conn.commit()
        print("Results added to DB!!!")
    except MySQLError as error:
        print("Error:", error)
