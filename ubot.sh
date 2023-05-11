#!/bin/bash
# FighterTunnel
# Copyright (C) 2023 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

python_up() {
        pkgs='python3.8'
        install=false
        for pkg in $pkgs; do
                status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"
                if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
                        install=true
                        break
                fi
        done
        if "$install"; then
                sudo apt-get install build-essential checkinstall -y
                sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev \
                        libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
                cd /opt
                sudo wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz
                sudo tar xzf Python-3.8.12.tgz
                cd Python-3.8.12
                sudo ./configure --enable-optimizations
                sudo make altinstall
        fi
}
cat >/usr/bin/man-ft <<END
#!/bin/bash
cd /etc/bot/Man-FT
python3.8 -m ft
END
function string() {
        clear
        echo "1. SIAPKAN API_ID/ API_KEY (my.telegram.org)"
        echo "2. SIAPKAN API_HASH (my.telegram.org)"
        echo "3. MASUKAN NOMER TELEGRAM (CONTOH FORMAT +62815768895)"
        echo ""
        read -e -p "Create String Sessions? [y/n] " -i "y" str
        if [ "$str" = "y" ]; then

                python3.8 /etc/bot/Man-FT/ft/resources/session/str.py

        fi
        echo "CEK DI PESAN TELEGRAM STRING ANDA"
        sleep 6
}
function alat() {
        clear
        sec=5
        spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
        while [ $sec -gt 0 ]; do
                echo -ne "\e[33m ${spinner[sec]} Generator UserBoy $sec seconds...\r"
                sleep 1
                sec=$(($sec - 1))
        done
        clear
        echo "MASUKAN BAHAN U-BOT YANG BENAR"
        read -e -p "Input your USERNAME : " USER
        read -e -p "Input your API_KEY : " API_KEY
        read -e -p "Input your API_HASH : " API_HASH
        read -e -p "Input your BOT_TOKEN : " BOT_TOKEN
        read -e -p "Input your BOTLOG_CHATID : " BOTLOG_CHATID
        read -e -p "Input your STRING_SESSION : " STRING_SESSION
        export USER=$USER

}
function sql() {
        sec=5
        spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
        while [ $sec -gt 0 ]; do
                echo -ne "\e[33m ${spinner[sec]} Generator UserBoy $sec seconds...\r"
                sleep 1
                sec=$(($sec - 1))
        done
        clear
        echo "--------------------------------------------"
        echo "    This script will install PostgreSQL."
        echo "      and create database and user."
        echo "  You may be prompted for sudo password."
        echo "--------------------------------------------"
        read -e -p "Install PostgreSQL database? [y/n] " -i "y" installpg
        if [ "$installpg" = "y" ]; then
                #sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main"
                #wget --quiet -O -q - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
                sudo apt-get update
                sudo apt-get install postgresql -y
                sudo su postgres <<EOF

createdb  $USER;

psql -c "CREATE USER $USER WITH PASSWORD '$USER';"

psql -c "grant all privileges on database $USER to $USER;"

echo "Postgres User '$USER' and database '$USER' created."

EOF
        fi

        #read -e -p "Create Database and user? [y/n] " -i "y" createdb
        #if [ "$createdb" = "y" ]; then
        #        sudo -u postgres createuser -D -A -P $USER
        #        sudo -u postgres createdb -O $USER $USER
        #
        #fi
}
function defn() {
        mkdir /etc/bot/
        apt update -y
        sudo apt install python3 -y
        sudo apt install python3-pip -y
        pip3.8 install --upgrade pip
        pip3.8 install telethon
        python_up
        sudo apt install tree wget2 p7zip-full jq ffmpeg wget git -y
        curl -fsSL https://deb.nodesource.com/setup_16.x | sudo bash -
        sudo apt install -y nodejs vim
        wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt install -y ./google-chrome-stable_current_amd64.deb
        rm -rf google-chrome-stable_current_amd64.deb
        cd /etc/bot/
        git clone https://github.com/FighterTunnel/Man-FT.git
        wget -q https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/Man-Userbot/requirements.txt
        pip3.8 install --upgrade pip
        pip3.8 install -r requirements.txt
}

function service_ubot() {
        cat >/etc/bot/Man-FT/config.env <<END
API_KEY = "$API_KEY"
API_HASH = "$API_HASH"
STRING_SESSION = "$STRING_SESSION"
BOT_TOKEN = "$BOT_TOKEN"
BOTLOG_CHATID = $BOTLOG_CHATID
DATABASE_URL = "postgres://$USER:$USER@localhost:5432/$USER"
PM_AUTO_BAN = False
END   


wget -q -O /usr/bin/man-ft "https://github.com/FighterTunnel/Man-FT/raw/main/ft/man-ft" ; chmod +x /usr/bin/man-ft
wget -q -O /etc/systemd/system/man-ft.service "https://github.com/FighterTunnel/Man-FT/raw/main/ft/service.man-ft"

        systemctl daemon-reload
        systemctl enable man-ft
        systemctl restart man-ft
        systemctl status man-ft

}
function main() {
        defn ; string ; alat ; sql ; service_ubot
}


main "#@"

