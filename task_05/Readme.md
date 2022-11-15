## Task: Connect to the PostgreSQL using Python
We will use the `psycopg2` package for connecting and interacting with the PostgreSQL database. For installation of this package in Windows WSL environment, see section `Other Notes`.

In this folder, there are 2 Python scripts:
1. `test_postgres.py` which tests the PostgreSQL & Python connection using simple approach.
2. `test_pg_bestway` shows the best practice for conencting with PostgreSQL using Python 

Also, there are following files:
* `config.py` module which has a `config` function that loads the PostgreSQL database connectivity configuration from the external file `database.ini`.
* `database.ini` which contains database configuration parameters.


### Other Notes
We will use the `psycopg2` package for connecting and interacting with the PostgreSQL database.

Install the psycopg2 module using:

```
pip install psycopg2 
```
 However, since I am using WSL Ubuntu 18.04, there was some issue in the installation. So with the help I tried installing the following packages first:

```
sudo apt-get install python-psycopg2
```

and then:

```
sudo apt-get install libpq-dev
```

Still there was issue. So refered the following post:

https://dev.to/dwmedina/how-to-install-the-psycopg2-python-package-in-wsl-2-11n

As above post suggested, I installed `python-dev`, `python3-dev` using `sudo apt-get install` command followed by `pip3 install wheel` and finally

```
sudo apt-get install python3.9-dev 
```

After above steps, I tried installing the `psycopg2` again using `pip install` command and it was successfully installed.


