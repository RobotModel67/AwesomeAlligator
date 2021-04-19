# ESP32 Workshop

## Lab configuration

### 1. Starting with esp-idf
(2021-04-18) Reference: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/  
a. Descargar el software e instalar sin usar espacios en el path  
b. El instalador tiene integrado cu python y git. Dejar todo por defecto  
c. Copiar los ejemplos a la carpeta de trabajo. Compilar y ejecutar  
d. Usar el monitor para testear  

#### Stage-001 HelloWorld

#### Stage-002 Blink

### 2. Starting with Mycropython
(2021-04-18) Reference: 
https://docs.micropython.org/en/latest/index.html
https://github.com/espressif/esptool
a. Instalar python  
b. Instalar esptools. pip install esptool  
c. Erase flash: esptool.py --port COM4 erase_flash  
d. Download micropython firmware. (https://micropython.org/download/esp32/)  
e. flashear firmware:
esptool.py --chip esp32 --port com4 --baud 115200 write_flash -z 0x1000 esp32-20210418-v1.15.bin  
f. Configure Putty  serial connection. Open Micropython REPL
https://problemsolvingwithpython.com/12-MicroPython/12.03-MicroPython-REPL/  
g. Tets some commands over REPL  
h. **Load python scripts: ** Install ampy.  
pip install adafruit-ampy  
i. Load script to device:  
ampy --port COM4 put .\blink.py main.py  
or run form terminal:  
ampy --port COM4 run .\blink.py  
j. Smile!

Practice: 
https://www.youtube.com/watch?v=gaOU1XtEKRg&list=PL4p-0ajxHfb2Y1gOHA2fSjUU9uFaYQ9i4  

https://randomnerdtutorials.com/micropython-programming-basics-esp32-esp8266/

#### Stage-003 Micropython Blink