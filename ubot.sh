#!/bin/bash

function string{} {
        read -e -p "Create String Sessions? [y/n] " -i "n" str
        if [ "$str" = "y" ]; then
                python3.8 /etc/bot/ft/resources/session/str.py

        fi
}
function alat{} {
        echo "ISI NAMA ANDA [JANGAN PAKAI SPASI]"
        read -p USER
        echo "API_KEY"
        read -p API_KEY
        echo "API_HASH"
        read -p API_HASH
        echo "BOT_TOKEN"
        read -p BOT_TOKEN
        echo "BOTLOG_CHATID"
        read -p BOTLOG_CHATID
        echo "STRING_SESSION"
        read -p STRING_SESSION
}
function sql{} {
read -e -p "Install PostgreSQL database? [y/n] " -i "n" installpg
if [ "$installpg" = "y" ]; then
        sudo add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main"
        wget --quiet -O -q - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
        sudo apt-get update
        sudo apt-get install postgresql-9.6 -y
        sudo -u postgres psql postgres

fi

read -e -p "Create Database and user? [y/n] " -i "n" createdb
if [ "$createdb" = "y" ]; then
        sudo -u postgres createuser -D -A -P $USER
        sudo -u postgres createdb -O $USER $USER

fi
}
function defn{} {
        mkdir /etc/bot/
        cd /etc/bot/
        apt update -y
        sudo apt install tree wget2 p7zip-full jq ffmpeg wget git -y
        git clone https://github.com/FighterTunnel/Man-FT.git
        curl -fsSL https://deb.nodesource.com/setup_16.x | sudo bash -
        sudo apt install -y nodejs vim
        wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt install -y ./google-chrome-stable_current_amd64.deb
        rm -rf google-chrome-stable_current_amd64.deb
        wget -q https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/Man-Userbot/requirements.txt
        pip3.8 install --upgrade pip
        pip3.8 install -r requirements.txt
}
function service_ubot{} { 
cat >/etc/bot/config.env <<EOF
API_KEY = "$API_KEY"
API_HASH = "$API_HASH"
STRING_SESSION = "$STRING_SESSION"
BOT_TOKEN = "$BOT_TOKEN"
BOTLOG_CHATID = $BOTLOG_CHATID
DATABASE_URL = ""postgres://$USER:$USER@localhost:5432/$USER""
PM_AUTO_BAN = False
EOF        
cat >/usr/bin/man-ft << END
#!/bin/bash

cd /etc/bot/Man-FT
python3.8 -m userbot
END
chmod +x /usr/bin/man-ft
cat >/etc/systemd/system/man-ft.service <<-END
                                                                                   
[Unit]
Description=bhoikfostyahya bot service
Documentation=FighterTunnel
After=syslog.target network-online.target

[Service]
User=root
NoNewPrivileges=true
ExecStart=/usr/bin/man-ft

[Install]
WantedBy=multi-user.target

END
systemctl daemon-reload
systemctl enable man-ft
systemctl restart man-ft
systemctl status man-ft

}
function main{} {
        defn
        string
        alat
        sql
        service_ubot
}

main "#@"
