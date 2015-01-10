# mila-fw
Python firmware uploader for `mila` project

#USAGE EXAMPLE

`c:\Users\Петр\Documents\GitHub\mila-fw>c:\Python34\python.exe fw.py -P -p COM1 -e -f LED.HEX -V -r`, where:

`-P` - preload bootloader

`-p COM1` - selecting COM port

`-e` - erase chip before flashing

`-f LED.HEX` - upload file `LED.HEX`

`-v` - verify

`-V` - verbose output

`-r` - run code after uploading


Typical log:

```
c:\Users\Петр\Documents\GitHub\mila-fw>c:\Python34\python.exe fw.py -P -p COM1 -e -f LED.HEX -V -r
Opened at 9600
Preparing bootstrap done
Preparing hex file done
Synchronization...
Synchronized successfully
Setting up baudrate...
Sending command
Got respose:  b'Ei\xff'
Cange port baudrate setup on 115200
Baudrate 115200 is set successfully
Uploading bootloader...
Start adress: 30720, lenght: 995
Uploading done
Start code verifying
Bootloader uploaded successfully
Starting bootloader...
bootloader id: b'1986BOOTUART'
Bootloader started successfully
Erasing...
Erasing done
Program 512 byte...
ready to upload
Program 512 byte done!
Run at 0x08000000...
Run at 0x08000000 OK!

c:\Users\Петр\Documents\GitHub\mila-fw>
```


#TODO:



#ISSUES:
