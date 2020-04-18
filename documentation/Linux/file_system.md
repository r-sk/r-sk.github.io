# Various directories

## bin
* binaries
* programs and applications are stored here
* eg: ls, pwd, chmod, mkdir, grep etc

## sbin
* System binaries
* System administrator uses
* Standard user not have access wothout permission

## boot
* all files system needs to boot the machine
* boot loader lives here
  
## dev
* devices
* This is where all your devices lives
* eg: mouse, keyboard, monitor, speakers, disks, webcam etc
* Disk will be in : dev/sda
* dev/sda1 , dev/sda2 are partitions
  
## etc
* et-cetera
* all the configuration files of the system 
  
## home
* all user files lives here, shown on side bar
* Personal files and documents
* Each user has their own home folder
* .icons , . themes are here too, which helps in customization
  
## lib, lib32, lib64
* libraies lives here
  
## media, mnt
* mnt = mount
* Other mounted drives
* all the mounted floppydrives, pendrives, external harddrives, network drives, secondary harddrives etc
* D:, E: etc as shown in windows lives here
* OS automatically mount the added drives in media directory
* If you mount drives manually, mount it inside mnt directory

## opt
* optional
* some programs are stored here
* Eg: ROS, googlechrome , teamviwer, virtualbox etc
* this is where we can manually install softwares
  
## proc
* process
* information about system processes and resources
* every process has directory here with directory named with corresponding process ID
* some other files: cpuinfo, uptime etc
* Try looking into these files

## root
* root user's home directory

## run
* runs on RAM
* everything is gone when shutdown or restart
* contains info that needs during boot

## snap
* snap packages are stored
* snap packages are self-contained packages

## srv
* service
* service data are stored
* if you launch web server, ftp server , the files that can be access by external user are stored here
* usually empty if there are no services

## sys
* system
* to interact with kernel
* created everytime the system boots up

## tmp
* temporary
* temporaty files stored, cleared during bootup

## usr
* universal system resources, eg: icons
* User application space
* Application used by user are stored here

## var
* variable
* logs and temp files for system
* constantly grows in size as you use the system


# Some important files

### ~/.bashrc
File that is run every time you open an terminal

### ~/.bash_history
List of all commands typed in terminal

