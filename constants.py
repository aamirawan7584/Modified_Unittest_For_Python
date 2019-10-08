query_test = "INSERT INTO Results(test_name, suite_name,std_out,status, run_id)" \
            "VALUES (%s,%s, %s,%s,%s)"

query_runs_before = "INSERT INTO Runs(start_time, host_name)" \
            "VALUES (%s,%s)"
query_runs_after = "UPDATE Runs SET end_time = %s, total_Tests = %s, Pass = %s, Fail = %s," \
                   "Error = %s,Browser =%s, Link =%s"\
                    "WHERE run_id=%s"
host = '172.18.0.2'
database = 'testing'
password = 'mysql123'
user = "root"