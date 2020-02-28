Web Youtube downloader source files. 

These are just the web interface files and not the youtube-dl tool itself.

This also contains a youtube-dl updater service.

Note: This code only works if you're using apache2 on ubuntu 18.04 unless you're willing to go through all the files and change the file paths.

File and directory structure: 
-   /var/www/youtube-backend/: 
    -   download.py - owner:www-data - permissions: 775
    -   audiodownload.py - owner:www-data - permissions: 775
    -   /* create two empty log files here, log.txt and loga.txt*/
    -   log.txt - owner:www-data - permissions: 666
    -   loga.txt - owner:www-data - permissions: 666
    -   /* add an empty directory here named "file"*/
    -   file/ - owner:www-data - permissions: 775
-   /var/www/(where ever you want to put the frontend files):
    -   index.html - owner:www-data - permissions: 664
    -   submit.php - owner:www-data - permissions: 775
    -   audiosubmit.php - owner:www-data - permissions: 775
    -   title.php - owner:www-data - permissions: 775
    -   exist.php - owner:www-data - permissions: 775
        
Make sure to install youtube-dl from source files and not apt package manager, and make sure it's located in "/usr/local/bin/youtube-dl".

Youtube-dl updater - optional:
Put youtubedlup.py in /usr/local/bin/ with owner as root and permissions to 755.
Edit root crontab and add a line for executing script, for example:
-   @daily /usr/local/bin/youtubedlup.py
    
Script for deleting old downloaded files coming soon.
