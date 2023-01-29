# CNAB code back-end challenge

This is a [Django](http://www.djangoproject.com) project, which consists of uploading a CNAB file, which contains financial information, parsing the information and storing it in a database.

## CNAB documentation

| Field description | Start | End | Size | Comment                                                                                                                |
| ------------------ | ------ | --- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| Type               | 1      | 1   | 1       | Transition type                                                                                                        |
| Date               | 2      | 9   | 8       | Date of occurrence                                                                                                      |
| Value              | 10     | 19  | 10      | Value of the movement. The value found in the file needs to be divided by one hundred(value / 100.00) to normalize it. |
| CPF                | 20     | 30  | 11      | CPF of the beneficiary                                                                                                       |
| Card               | 31     | 42  | 12      | Card used in the transaction                                                                                             |
| Hour               | 43     | 48  | 6       | Time of occurrence given the UTC-3 zone                                                                             |
| Store owner        | 49     | 62  | 14      | Name of store representative                                                                                              |
| Store name          | 63     | 81  | 19      | Store Name                                                                                                             |

## Documentation on transaction types

| Type | Description            | Nature   | Signal|
| ---- | ---------------------- | -------- | ----- |
| 1    | Debit                  | Input    | +     |
| 2    | Boleto                 | Output   | -     |
| 3    | Financing              | Output   | -     |
| 4    | Credit                 | Input    | +     |
| 5    | Receiving Loan         | Input    | +     |
| 6    | Sales                  | Input    | +     |
| 7    | TED receiving          | Input    | +     |
| 8    | DOC receiving          | Input    | +     |
| 9    | Rent                   | Output   | -     |

## File CNAB example

`3201903010000012200000000000006777****1313172712PERSON NAME   STORE NAME EXAMPLE`
`1201903010000014200000000000004753****3153153453PERSON NAME   STORE NAME`
`3201903010000012200000000000006777****1313172712PERSON NAME   STORE NAME EXAMPLE`
`3201903010000012200000000000006777****1313172712PERSON NAME   STORE NAME EXAMPLE`
`1201903010000014200000000000004753****3153153453PERSON NAME   STORE NAME`
`3201903010000012200000000000006777****1313172712PERSON NAME   STORE NAME EXAMPLE`

## Requirements

- [Python](https://www.python.org/)
- [Django](http://www.djangoproject.com)
- [Docker(optional)](https://www.docker.com/)

## Running project using Sqlite3

1. Clone this repository:

    ```shell
    git clone https://github.com/leandroschillreff/cnab-code-back-end-challenge.git
    cd cnab-code-back-end-challenge
    ```

2. Create your virtual environment:

    ```shell
    python -m venv venv
    ```

3. Activate your venv:

    ```bash
    # linux:
    source venv/bin/activate

    # windows:
    .\venv\Scripts\activate
    ```

4. Then install the dependencies:

    ```shell
    pip install -r requirements.txt
    ```

5. Run the makemigrations:

    ```shell
    TEST=TEST ./manage.py makemigrations
    ```

6. Run the migrate:

    ```shell
    TEST=TEST ./manage.py migrate
    ```

7. Run the project

    ```shell
    TEST=TEST ./manage.py runserver
    ```

8. Accessing the routes:
    1. <http://127.0.0.1:8000/api/cnab/upload/>, to submit the CNAB.txt file.
    2. <http://127.0.0.1:8000/api/cnab/list/>, to view all information that has been saved to the database.
    3. <http://127.0.0.1:8000/api/cnab/balance/>, to view the balance of each store.
    4. <http://127.0.0.1:8000/api/docs/>, to see documentation of the routes.

## Running project using Docker

1. Clone this repository:

    ```shell
    git clone https://github.com/leandroschillreff/cnab-code-back-end-challenge.git
    cd cnab-code-back-end-challenge
    ```

2. Configure .env:

    ```text
    Create an .env file in the project root, copy the contents of .env.example and add the database name, user and password information
    ```

3. Settings for running docker:
    1. To start and restart all services defined in docker-compose.yml

        ```shell
        docker-compose up

        or

        sudo docker-compose up
        ```

    2. To stop all services defined in docker-compose.yml

        ```shell
        docker-compose stop

        or

        sudo docker-compose stop
        ```

    3. To restart the previously stopped containers

        ```shell
        docker-compose start

        or

        sudo docker-compose start
        ```

    4. To stop container execution, and will remove stopped containers

        ```shell
        docker-compose down

        or

        sudo docker-compose down
        ```

4. Accessing the routes:
    1. <http://0.0.0.0:8000/api/cnab/upload/>, to submit the CNAB.txt file.
    2. <http://0.0.0.0:8000/api/cnab/list/>, to view all information that has been saved to the database.
    3. <http://0.0.0.0:8000/api/cnab/balance/>, to view the balance of each store.
    4. <http://0.0.0.0:8000/api/docs/>, to see documentation of the routes.
