# Backup me, dear uncle Python
An application for quickly creating backups on your computer  

<img src="image/backup_uncle.png">  

## About this app
It allows you to quickly create an archive with a backup copy of the specified directory and put it in the right place on your hard disk.  

The name of the archive being created contains the date and time of its creation, if necessary, you can specify a prefix to the archive name

It is possible to write a text note, which is placed in the archive, in the form of a txt file.

You also can upload your backup file on Google Drive storage.

## How to install

```bash
git clone https://github.com/Vadimmmz/backup-me-dear-uncle-python.git
python -m venv env

# Activate virtual environment for Windows
source env/Scripts/activate

# Activate virtual environment fo for Linux
source env/bin/activate

# install all the libraries that are needed to work
pip install -r requirements.txt
```

## Used packages
The library was used to compile the file:
- auto-py-to-exe==2.27.0
- PyDrive~=1.3.1
- google-api-python-client==1.8.0
- 
## License

MIT License