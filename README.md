install the requirements

pip install -r requirements.txt

update the src/eda/config.py with appropriate values

- ms_db_config: update MS Sql database values
- bq_config: to connect to BQ export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH" https://cloud.google.com/docs/authentication/getting-started

run the server using

- python src/eda/app.py
