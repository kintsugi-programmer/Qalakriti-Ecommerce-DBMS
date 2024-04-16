-- run?
-- sql run? 
-- mysql run trial ?
-- mysql -u root -p < Data/schema.sql
-- mysql -u root -p Qalakriti < Data/schema.sql

-- relationship check
-- DEFAULT NULL WHERE ?


balinux@balinux-ASUS-TUF-Gaming-F15-FX507ZE-FX577ZE:~$ tldr mysql
Cache is out of date. You should run "tldr --update"

  mysql

  The MySQL command-line tool.
  More information: https://www.mysql.com/.

  - Connect to a database:
    mysql database_name

  - Connect to a database, user will be prompted for a password:
    mysql -u user --password database_name

  - Connect to a database on another host:
    mysql -h database_host database_name

  - Connect to a database through a Unix socket:
    mysql --socket path/to/socket.sock

  - Execute SQL statements in a script file (batch file):
    mysql -e "source filename.sql" database_name

  - Restore a database from a backup created with mysqldump (user will be prompted for a password):
    mysql --user user --password database_name < path/to/backup.sql

  - Restore all databases from a backup (user will be prompted for a password):
    mysql --user user --password < path/to/backup.sql


See also: mysqldump


It looks like the MySQL server installation was successful. Some key points:

1. The mysql-server package and its dependencies were installed. This includes the main mysql server packages.

2. Some optional dictionary packages were installed as dependencies - mecab-ipadic etc. These are for full text search capability in MySQL.

3. The mysql server was started successfully and is running with pid 44413.

4. A systemd service was created to manage MySQL on boot.

5. No errors were reported.

6. At the end, the man-db and libc-bin packages were triggered to update some system caches.

So in summary, MySQL is now installed and running on your system. You can now connect to it and create databases, tables etc as needed.










Those "Cannot stat file" messages appear to be harmless warnings from MySQL.

When the MySQL server starts up, it tries to check if there are any active client connections already established that it needs to clean up. To do this, it scans the /proc filesystem for open file descriptors belonging to the mysqld process.

The "Cannot stat file" warnings indicate that the MySQL process does not have permission to access those particular file descriptors under /proc. This is expected and normal behavior - MySQL is just scanning through a range of FDs blindly trying to close any open sockets. The permission denied errors are fine.

So in summary:

- MySQL is checking for open client sockets on startup by looking at /proc
- It doesn't have access to scan all FDs, but tries anyway
- The permission errors are normal and expected
- As long as mysqld successfully started in the end, these messages can be ignored

They are just informing you that the FD cleanup attempts were partially unsuccessful, but it has no negative impact on MySQL operations.



balinux@balinux-ASUS-TUF-Gaming-F15-FX507ZE-FX577ZE:~$ mysql
ERROR 1045 (28000): Access denied for user 'balinux'@'localhost' (using password: NO)
balinux@balinux-ASUS-TUF-Gaming-F15-FX507ZE-FX577ZE:~$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.36-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 


local host has no local host and no password
mysql -n root -n sql.myserver.com - P - password // command for sql server connect
