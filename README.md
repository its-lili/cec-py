# cec-py

```
sudo apt-get install libcec-dev build-essential python-dev
```

## Virtual environment
Create a virtual environment with:
```shell
python3 -m venv ./venvs/cec_py
```
Activate it with:
```shell
. ./venvs/cec_py/bin/activate
```
Install requirements:
```shell
pip install -r requirements.txt
```


## Serial connection


Give permission:
```shell
sudo chmod 666 /dev/tty0

# or 

sudo chmod 666 /dev/ttyAMA0
```

1. Enable serial connection
2. CMD `dmesg | grep tty`


### Run
Run USB serial reading command with:
```shell
python usb_cec.py <port_name>

# Raspberry PI:
python usb_cec.py /dev/ttyAMA0

# or 
python usb_cec.py /dev/tty0
```

### Connect PC with RPI4 for serial communication
[USB serial PC to RPI4](https://electropeak.com/learn/raspberry-pi-serial-communication-uart-w-arduino-pc/)

```shell
sudo vi /boot/config.txt

# Add the following lines to the end of the file.
Enable UART
enable_uart=1

sudo reboot
```