# Capstone
Capstone Class Raspberry Pi High Quality Camera and Raspberry Pi 4 Model B 

#Add in how to set up the Raspberry Pi 4 Model B 
Setting up the Raspberry Pi 4 Model B normally 
Before you can use the Raspberry Pi High-Quality Camera, you'll need to set up the Raspberry Pi 4 Model B. Here are the general steps:

Obtain a Raspberry Pi 4 Model B and the necessary accessories, such as a power supply, microSD card, and any additional peripherals you plan to use.
Download the latest version of the Raspberry Pi OS (previously Raspbian) from the official Raspberry Pi website and flash it onto the microSD card using a tool like Raspberry Pi Imager.
Insert the microSD card into the Raspberry Pi 4 Model B and connect the power supply.
Connect the Raspberry Pi to a display, keyboard, and mouse, and follow the on-screen instructions to complete the initial setup.
Once the Raspberry Pi is set up, you can proceed to configure the Raspberry Pi High-Quality Camera.

Setting up the Raspberry Pi High-Quality Camera
After connecting the camera module to the Raspberry Pi's CSI port, you'll need to enable the camera interface in the Raspberry Pi's configuration settings.
You can do this by running the `sudo raspi-config` command in the terminal and navigating to the "Interface Options" menu, then selecting "Camera" and enabling it.
Save the changes and exit the configuration tool.
You can now start using the Raspberry Pi High-Quality Camera by running Python scripts or utilizing the built-in camera command-line tools, such as `raspistill` and `raspivid` (Can use rpicam as well for this as it is the same concept).


By following these steps, you will have a fully functional Raspberry Pi 4 Model B setup with the Raspberry Pi High-Quality Camera connected and ready for use in your projects.


#Add in how to set up the Raspberry Pi 4 Model B Headless 
A "headless" setup refers to a Raspberry Pi configuration where you don't need a physical monitor, keyboard, or mouse connected to the device. This is particularly useful for scenarios where the Raspberry Pi is placed in a remote location or is intended to run as a server or a dedicated application.

Here are the detailed steps to set up the Raspberry Pi 4 Model B as a headless system:
Prepare the microSD Card:
Download the latest Raspberry Pi OS (previously Raspbian) image from the official Raspberry Pi website.
Use a tool like Raspberry Pi Imager or balenaEtcher to flash the OS image onto the microSD card.

2. Enable SSH (Secure Shell) Access:
After the image has been flashed, insert the microSD card into your computer.
Create an empty file named "ssh" (without any file extension) in the root directory of the microSD card. This will enable SSH access to the Raspberry Pi during the initial setup.

3. Configure Wi-Fi Connectivity (optional):
If you want the Raspberry Pi to connect to your wireless network, create a file named "wpa_supplicant.conf" in the root directory of the microSD card.
Open the file with a text editor and add the following content, replacing the placeholders with your Wi-Fi network's SSID (name) and password:

      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
      update_config=1

      network={
          ssid="your_wifi_ssid"
          psk="your_wifi_password"

4. Insert the microSD Card and Power On the Raspberry Pi:
Insert the prepared microSD card into the Raspberry Pi 4 Model B.
Connect the power supply to the Raspberry Pi.

5. Connect to the Raspberry Pi via SSH:
Determine the IP address of your Raspberry Pi. If you've configured it to connect to your Wi-Fi network, you can find the IP address using your router's admin interface or a network scanning tool.
Open a terminal or command prompt on your computer and connect to the Raspberry Pi using the SSH protocol. The command will look like this:

      ssh pi@your_raspberry_pi_ip_address

When prompted, enter the default Raspberry Pi password, which is "raspberry".

6. Update and Upgrade the System:
Once connected, run the following commands to update and upgrade the Raspberry Pi's software:

      sudo apt-get update
      sudo apt-get upgrade -y

7. Optionally, Change the Default Password:
For security reasons, it is recommended to change the default password for the "pi" user. You can do this by running the following command:

      sudo passwd pi

Enter a new, secure password when prompted.

8. Configure the Raspberry Pi for Headless Operation:
If you want to use the Raspberry Pi without a monitor, keyboard, and mouse, you can configure it to boot directly into the command-line interface (CLI) mode.
Run the following command to edit the Raspberry Pi's configuration file:

      sudo raspi-config

Navigate to the "Boot Options" menu and select "Desktop / CLI" -> "Console Autologin".
Save the changes and exit the configuration tool.




By following these steps, you have successfully set up your Raspberry Pi 4 Model B as a headless system, allowing you to manage and interact with it remotely using SSH. This setup is particularly useful for running server applications, automating tasks, or deploying the Raspberry Pi in remote or unattended locations. For example, the following was after I set up the SSH from my MAC to the RPI using the router's IP as you can see. And you know that I am actually connected to the RPI due to the “ayan@raspberrypi”


#Add in how to set up the Raspberry Pi High Quality Camera 
Take out the IR-Cut Filter and insert the ribbon cable in the 4 model b. Thats it, super simple.

#Add in anything else that you may want people to know
