What is OracleConnCLI?
=======================
OracleConnCLI is an cli application to test oracle database connection through cx_Oracle.

Requires: 
* cx_Oracle
* plumbum

How is it used?
=======================

* password not set
	```
	$ python oracle_conn_cli.py
	login username: oracle
	login password: input_pw
	connect string: oracle/input_pw@127.0.0.1:1521/orcl
	connect result: failed [ORA-12541: TNS:no listener]
	```

* a failed connection
	```
	$ python oracle_conn_cli.py -h 192.168.100.6 --sid orcl -u oracle -p bad_pw
	connect string: oracle/bad_pw@192.168.100.6:1521/orcl
	connect result: failed [ORA-01017: invalid username/password; logon denied]
	```

* a successful connection
	```
	$ python oracle_conn_cli.py -h 192.168.100.6 --sid orcl -u oracle -p oracle
	connect string: oracle/oracle@192.168.100.6:1521/orcl
	connect result: OK [sid: orcl, version: 11.2.0.4.0]
	```

![usage](https://github.com/luoxu34/OracleConnCLI/blob/master/usage.png)
