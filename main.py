import RPi.GPIO  as GPIO   
import spidev 
import time
import os 

#generic setup 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#PIR SENSOR
pir = 29 
GPIO.setup(pir,GPIO.IN)


#motor / sanitiser pump setup 
pump1= 18
pump2 = 22
GPIO.setup(pump1,GPIO.OUT)
GPIO.setup(pump2,GPIO.OUT)

#the final opening of barrier 
barrier1= 32
barrier2 = 33
GPIO.setup(barrier1,GPIO.OUT)
GPIO.setup(barrier2,GPIO.OUT)

#spi communication
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Define sensor channels
temp_channel  = 0

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005
delay = 1

# LCD setup 
LCD_RS = 15
LCD_E  = 16
LCD_D4 = 7
LCD_D5 = 11
LCD_D6 = 12
LCD_D7 = 13

GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

'''
Function Name :lcd_init()
Function Description : this function is used to initialized lcd by sending the different commands
'''
def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
'''
Function Name :lcd_byte(bits ,mode)
Fuction Name :the main purpose of this function to convert the byte data into bit and send to lcd port
'''
def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
    GPIO.output(LCD_RS, mode) # RS
 
  # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
    lcd_toggle_enable()
 
  # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)
 
  # Toggle 'Enable' pin
    lcd_toggle_enable()

'''
Function Name : lcd_toggle_enable()
Function Description:basically this is used to toggle Enable pin
'''

def lcd_toggle_enable():
  # Toggle enable
   time.sleep(E_DELAY)
   GPIO.output(LCD_E, True)
   time.sleep(E_PULSE)
   GPIO.output(LCD_E, False)
   time.sleep(E_DELAY)
  
'''
Function Name :lcd_string(message,line)
Function  Description :print the data on lcd 
'''
def lcd_string(message,line):
  # Send string to display
    message = message.ljust(LCD_WIDTH  ," ") 
    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)
    
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

 
# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))
  temp = round(temp,places)
  return temp
 
 
delay = 5
lcd_init()
lcd_string("welcome ",LCD_LINE_1)
time.sleep(2) 

def hand_present():
#pir sensor 
  if GPIO.input(pir) :
   return True
   
  else:
   return False 
  
   
def detect_mask():
  return False
      
def main():

  while(True): # the whole instrument turns on only when there is a presence of hand 
    
    if hand_present():
      #temp sensor sending readings 
      lcd_string("Sanitiser pumping",LCD_LINE_1)
      temp_level = ReadChannel(temp_channel) 
      temp       = ConvertTemp(temp_level,2)

      #turn on the pump  
      GPIO.output(pump1,GPIO.HIGH)
      GPIO.output(pump2,GPIO.LOW)
      time.sleep(5)
      lcd_string(" ",LCD_LINE_1)
      
      #check the temperature
      if temp >38:
        lcd_string("Temp high ",LCD_LINE_1)
        lcd_string(str(temp),LCD_LINE_2)
        time.sleep(2)

      else:
        #activate the camera 
        lcd_string("Camera on",LCD_LINE_1)
        lcd_string("Temp "+str(temp),LCD_LINE_2)
        time.sleep(2)

        if detect_mask():
          #Entry allowed 
          lcd_string("Mask worn",LCD_LINE_2)
          GPIO.output(barrier1,GPIO.HIGH)
          GPIO.output(barrier2,GPIO.LOW)
          time.sleep(5)
        else:
          lcd_string("NO mask",LCD_LINE_1)
          time.sleep(7)
        
   
    
if __name__ == '__main__':
    main()
