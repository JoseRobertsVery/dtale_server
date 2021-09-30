from dtale.app import build_app
from dtale.views import startup
import pandas as pd
import pandas_gbq as pd_bq
from MsSql import MsSql
from flask import redirect
from config import ms_db_config
from google.cloud import bigquery


if __name__ == '__main__':
    app = build_app(reaper_on=False)

    @app.route("/mssql-eda")
    def msql_eda():
        qry: str = """select * from bow"""

        ms: MsSql = MsSql(**ms_db_config)
        ms.session_conn()
        qry_results: dict = ms.matrix(qry)
        df: pd = pd.DataFrame(qry_results)
        instance = startup(data=df, ignore_duplicate=True)
        return redirect(f"/dtale/main/{instance._data_id}", code=302)

    @app.route("/bq-eda")
    def bq_eda():
        qry: str = """"""

        bigquery.Client()
        df: pd_bq = pd_bq.read_gbq(qry, dialect='standard')
        instance = startup(data=df, ignore_duplicate=True)
        return redirect(f"/dtale/main/{instance._data_id}", code=302)

    @app.route("/")
    def hello_world():
        return """Hi there, 
    <li> load MS Sql data using create<a href='/mssql-eda'> MsSql eda report</a></li>
    <li> load BQ Sql data using create<a href='/bq-eda'> BQ eda report</a></li>"""

    app.run(host="0.0.0.0", port=8080, debug=True)
