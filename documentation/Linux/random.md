# Where are clipboard files located in Ubuntu?

* The clipboard is not stored in the filesystem or even in a particular location in memory.
* When you copy text in an application (whether by selecting text, for the primary selection, or by an explicit 'copy' operation for clipboard selection), the application where you copy alerts the X server that it now owns that particular selection.
* When you paste, the application you paste into sends a request to the X server, which is redirected to the application that owns the selection. 

# Copy clipboard image to a file

* **xclip** can do this task
  
        sudo apt-get install xclip

* First copy any image to clipboard or Ctrl+Shift+PrintScreen to copy screenshot to a file.
* To see if there is image in clipboard:

        $ xclip -selection clipboard -t TARGETS -o

* It outputs
  
        TIMESTAMP
        TARGETS
        SAVE_TARGETS
        MULTIPLE
        image/png (This is what you are intrested in)
        text/html

* To save this image to a file:

        $ xclip -selection clipboard -t image/png -o > /path/to/dir/filename.png

> Always make sure you donot copy anything else (eg. text) after you have copied image in order to see image/png in target.  
> Else, your clipboard will only have text and you can't find image/png target

# Rename Terminal Tabs

* If there are plenty of Tabs, it is so frustating to find the tab we want.
* It could be handy if each Terminal Tabs have different name.
* Just add following function to .bashrc :
  
        function title()
        {
                if [[ -z "$ORIG" ]]; then
                ORIG=$PS1
                fi
                TITLE="\[\e]2;$*\a\]"
                PS1=${ORIG}${TITLE}
        }

* Now you can easily rename tabs by:
  
        title <name you like>