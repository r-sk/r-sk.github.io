# Where are clipboard files located in Ubuntu?

* The clipboard is not stored in the filesystem or even in a particular location in memory.
* When you copy text in an application (whether by selecting text, for the primary selection, or by an explicit 'copy' operation for clipboard selection), the application where you copy alerts the X server that it now owns that particular selection.
* When you paste, the application you paste into sends a request to the X server, which is redirected to the application that owns the selection. 
