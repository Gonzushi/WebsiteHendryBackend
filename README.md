The backend is hosted in Microsfoft Azure Function. Therefore, the function_app.py is required as entry to reun the API. 

Quick start to run the API in local machine:
1. Run the following code "pip install -r requirements.txt"
2. Create a file with a name of ".env". This will be used to store enviroment variable. In this case, the variable needed for MS SQL Server are:
   1. SQL_SERVER=******
   2. SQL_USERNAME=******
   3. SQL_PASSWORD=******
   4. SQL_DATABASE_NAME=******
   5. SQL_ODBC_VERSION=17
4. Your computer will need Microsoft ODBC driver to connect with MS SQL Server
5. Then, you can run the API by running the following command "uvicorn main:app --reload"
