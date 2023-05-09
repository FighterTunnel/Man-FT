#!bin/bash
mkdir /etc/bot/
git clone https://github.com/FighterTunnel/Man-FT.git
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo bash -
sudo apt install -y nodejs vim
sudo apt install tree wget2 p7zip-full jq ffmpeg wget git -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
wget -q https://raw.githubusercontent.com/mrismanaziz/Man-Userbot/Man-Userbot/requirements.txt
pip3.8 install --upgrade pip
pip3.8 install -r requirements.txt

cat >/usr/bin/man-ft << EOF
#!/bin/bash

cd /etc/bot/man-ft
python3.8 -m userbot
EOF
chmod +x /usr/bin/man-ft
cat >/etc/systemd/system/man-ft.service << EOF
                                                                                   
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

EOF
systemctl daemon-reload
systemctl enable man-ft
systemctl restart man-ft
systemctl status man-ft