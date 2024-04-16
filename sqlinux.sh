#!/bin/bash

# https://github.com/kintsugi-programmer/LinuxScripts?tab=readme-ov-file#script-4-sqlinux---a-bash-script-for-mysql-setup-on-linux
# To Run:
# chmod +x sqlinux.sh
# ./sqlinux.sh
# UnStable

echo '
                     /$$ /$$                              
                    | $$|__/                              
  /$$$$$$$  /$$$$$$ | $$ /$$ /$$$$$$$  /$$   /$$ /$$   /$$
 /$$_____/ /$$__  $$| $$| $$| $$__  $$| $$  | $$|  $$ /$$/
|  $$$$$$ | $$  \ $$| $$| $$| $$  \ $$| $$  | $$ \  $$$$/ 
 \____  $$| $$  | $$| $$| $$| $$  | $$| $$  | $$  >$$  $$ 
 /$$$$$$$/|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$/ /$$/\  $$
|_______/  \____  $$|__/|__/|__/  |__/ \______/ |__/  \__/
                | $$                                      
                | $$                                      
                |__/

SQLinux is a bash script designed to facilitate MySQL setup tasks on Linux systems.
Made with ♥ by github.com/kintsugi-programmer/
' 

install_mysql() {
    echo "Installing MySQL..."
    sudo apt-get update
    sudo apt-get install -y mysql-server
    sudo mysql_secure_installation
    echo "MySQL installed successfully."
}

uninstall_mysql() {
    echo "Uninstalling MySQL..."
    sudo systemctl stop mysql
    sudo apt-get purge -y mysql-server mysql-client mysql-common
    sudo apt-get autoremove -y
    sudo apt-get autoclean
    sudo rm -rf /etc/mysql /var/lib/mysql
    echo "MySQL uninstalled successfully."
}

create_cred() {
    read -p "Enter new username: " username
    read -s -p "Enter new password: " password
    echo
    sudo mysql -u root -p -e "CREATE USER '$username'@'localhost' IDENTIFIED BY '$password';" mysql
}

grant_priv() {
    read -p "Enter username to grant privileges: " username
    sudo mysql -u root -p -e "GRANT ALL PRIVILEGES ON *.* TO '$username'@'localhost';" mysql
    echo "Privileges granted successfully."
}

flush_allpriv() {
    sudo mysql -u root -p -e "FLUSH PRIVILEGES;" mysql
    echo "All MySQL privileges flushed."
}

sq_script() {
    read -p "Enter database name: " database
    read -p "Enter path to SQL script: " sql_script
    sudo mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $database;"
    sudo mysql -u root -p $database < $sql_script
    echo "SQL script executed successfully."
}

server_start() {
    sudo systemctl start mysql
    echo "MySQL Server Started"
}

server_stop() {
    sudo systemctl start mysql
    echo "MySQL Server Stopped"
}

mysql_session() {
    echo "Entering MySQL Session. Type 'exit' to return to the menu."
    sudo mysql -u root -p
    echo "Returned to the MySQL Setup Menu."
}

#In Development
mysql_schema() {
    read -p "Enter database name: " database
    echo "Schema of database '$database':"
    sudo mysqlshow -u root -p $database
}

#In Development
mysql_data() {
    read -p "Enter database name: " database
    echo "Data of database '$database':"
    sudo mysql -u root -p -e "USE $database; SHOW TABLES;"
    read -p "Enter table name to view data: " table_name
    sudo mysql -u root -p -e "USE $database; SELECT * FROM $table_name;"
}

while true; do
    echo "MySQL Setup Menu"
    echo "1. Install MySQL"
    echo "2. Uninstall MySQL"
    echo "3. Create MySQL Credentials"
    echo "4. Grant Privileges to a User"
    echo "5. Flush All MySQL Privileges"
    echo "6. Execute SQL Script"
    echo "7. Start MySQL Server"
    echo "8. Stop MySQL Server"
    echo "9. mysql> Session AS root"
    echo "10. See all Scheme of Database"
    echo "11. See all Data of Database"
    echo "12. Exit"
    read -p "Enter your choice: " choice
    case $choice in
        1) install_mysql;;
        2) uninstall_mysql;;
        3) create_cred;;
        4) grant_priv;;
        5) flush_allpriv;;
        6) sq_script;;
        7) server_start;;
        8) server_stop;;
        9) mysql_session;;
        10) mysql_schema;;
        11) mysql_data;;
        12) echo "Exiting."; exit;;
        *) echo "Invalid choice. Please enter a valid option.";;
    esac
done