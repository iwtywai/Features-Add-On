#/bin/bash
sudo su
pwd > $add
cd /bin
touch RandomDataGenerator
chmod +x RandomDataGenerator
echo "python3 "+$add+"/main.py" > RandomDataGenerator