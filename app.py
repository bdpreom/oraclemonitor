from flask import Flask, render_template
from config import app_config
import cx_Oracle
from queries import con, basic_info, system_info, temp_tbs, tbs_detail, default_tbs, space_usage, tbs_quota, fra_status, \
    reco_usage, datafile_usage, rman_time, rman_current, rman_history, log_locations, alert_log_View, ddl_locks, \
    dml_locks, asm_usage, asm_stat, sga_info, sga_pga, mem1, mem2

import os
import sys


def create_app(env_name):

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    # Index
    @app.route('/')
    def index():
        try:
            cur1 = con.cursor()
            statement = basic_info
            cur1.execute(statement)
            res1 = cur1.fetchall()
            print(res1)
            cur1.close()

            cur2 = con.cursor()
            statement = system_info
            cur2.execute(statement)
            res2 = cur2.fetchall()
            print(res2)
            cur2.close()


        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(sys.stderr, "Oracle-Error-Code:", error.code)
            print(sys.stderr, "Oracle-Error-Message:", error.message)

        return render_template('home.html', data=res1, data1=res2)

    # Tablespace
    @app.route('/tablespace')
    def tablespace():

        try:
            cur1 = con.cursor()
            statement = temp_tbs
            cur1.execute(statement)
            res1 = cur1.fetchall()
            print(res1)
            cur1.close()

            cur2 = con.cursor()
            statement = tbs_detail
            cur2.execute(statement)
            res2 = cur2.fetchall()
            print(res2)
            cur2.close()

            cur3 = con.cursor()
            statement = default_tbs
            cur3.execute(statement)
            res3 = cur3.fetchall()
            print(res3)
            cur3.close()

            cur5 = con.cursor()
            statement = space_usage
            cur5.execute(statement)
            res5 = cur5.fetchall()
            print(res5)
            cur5.close()

            cur6 = con.cursor()
            statement = tbs_quota
            cur6.execute(statement)
            res6 = cur6.fetchall()
            print(res6)
            cur6.close()


        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(sys.stderr, "Oracle-Error-Code:", error.code)
            print(sys.stderr, "Oracle-Error-Message:", error.message)

        return render_template('tablespace.html', data=res1, data1=res2, data2=res3, data3=res5, data4=res6)

    # File Recovery Area
    @app.route('/frandata')
    def frandata():

        try:
            cur1 = con.cursor()
            statement = fra_status
            cur1.execute(statement)
            res1 = cur1.fetchall()
            print(res1)
            cur1.close()

            cur2 = con.cursor()
            statement = reco_usage
            cur2.execute(statement)
            res2 = cur2.fetchall()
            print(res2)
            cur2.close()

            cur3 = con.cursor()
            statement = datafile_usage
            cur3.execute(statement)
            res3 = cur3.fetchall()
            print(res3)
            cur3.close()




        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(sys.stderr, "Oracle-Error-Code:", error.code)
            print(sys.stderr, "Oracle-Error-Message:", error.message)

        return render_template('frandata.html', data=res1, data1=res2, data2=res3)

    # Tablespace
    @app.route('/rman')
    def rman():

        try:
            cur1 = con.cursor()
            statement = rman_time
            cur1.execute(statement)
            res1 = cur1.fetchall()
            print(res1)
            cur1.close()

            cur2 = con.cursor()
            statement = rman_current
            cur2.execute(statement)
            res2 = cur2.fetchall()
            print(res2)
            cur2.close()

            cur3 = con.cursor()
            statement = rman_history
            cur3.execute(statement)
            res3 = cur3.fetchall()
            print(res3)
            cur3.close()



        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(sys.stderr, "Oracle-Error-Code:", error.code)
            print(sys.stderr, "Oracle-Error-Message:", error.message)

        return render_template('rman.html', data=res1, data1=res2, data2=res3)

    # AlertLogs
    @app.route('/alertlogs')
    def alertlogs():

        cur2 = con.cursor()
        statement = log_locations
        cur2.execute(statement)
        res2 = cur2.fetchall()
        print(res2)
        cur2.close()

        cur1 = con.cursor()
        statement = alert_log_View
        cur1.execute(statement)
        res1 = cur1.fetchmany(100)
        print(res1)
        cur1.close()

        return render_template('alertlogs.html', data1=res2, data2=res1)

    # Locks

    @app.route('/locks')
    def locks():

        cur1 = con.cursor()
        statement = ddl_locks
        cur1.execute(statement)
        res1 = cur1.fetchmany(100)
        print(res1)
        cur1.close()

        cur2 = con.cursor()
        statement = dml_locks
        cur2.execute(statement)
        res2 = cur2.fetchall()
        print(res2)
        cur2.close()

        return render_template('locks.html', data1=res1, data2=res2)

    # memory

    @app.route('/memory')
    def memory():

        cur1 = con.cursor()
        statement = asm_usage
        cur1.execute(statement)
        res1 = cur1.fetchall()
        print(res1)
        cur1.close()

        cur2 = con.cursor()
        statement = asm_stat
        cur2.execute(statement)
        res2 = cur2.fetchall()
        print(res2)
        cur2.close()

        cur3 = con.cursor()
        statement = sga_info
        cur3.execute(statement)
        res3 = cur3.fetchall()
        print(res3)
        cur3.close()

        cur4 = con.cursor()
        statement = sga_pga
        cur4.execute(statement)
        res4 = cur4.fetchall()
        print(res4)
        cur4.close()

        cur5 = con.cursor()
        statement = mem1
        cur5.execute(statement)
        res5 = cur5.fetchall()
        print(res5)
        cur5.close()

        cur6 = con.cursor()
        statement = mem2
        cur6.execute(statement)
        res6 = cur6.fetchall()
        print(res6)
        cur6.close()

        return render_template('memory.html', data1=res1, data2=res2, data3=res3, data4=res4, data5=res5, data6=res6)

    return app