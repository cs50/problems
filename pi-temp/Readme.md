# Pi-Temp
My product was created by Raspberry Pi 3 b+ with including a temperature, and humidity sensor.
My product helps encounter multiple temperature problems  that everyday householders counter, for example my product portrays hour to hour temperature fluctuations that prompt the user to adjust the temperature during the different seasons.
I have used a temperature sensor called DHT22 which is a basic temperature that calculates temperature and humidity with multiple functions inside.
Before I started to code I have installed two libraries, which were PIP and Adafruit, I also upgraded setuptools which was required to do.
#####PIP is a standard package-management system used to install and manage software packages written in Python.
###sudo apt-get install python3-pip
#####Adafruit is a cloud service that just means we run it for you and you don't have to manage it.
###sudo pip3 install Adafruit
#####Setuptools is a package development process library designed to facilitate packaging Python projects by enhancing the Python standard library
###sudo python3 - m pip install -- upgrade setuptools wheel
Pi-Temp gives out the current date, current time, current temperature: Celsius, Fahrenheit, it also shows humidity which is an in-built feature in the sensor.
Pi-Temp also gives out dominant information towards the temperature from the current spot like suppose saying "Perfect Room Temperature."

