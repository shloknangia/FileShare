# Fileshare
a simple python file upload/download web server

Uploaded files will be placed in the `uploads` directory and displayed in reverse order of creation time
# Change port

`filesserver.py` : chang the `port` as you like

modify port
```py
if __name__ == "__main__":
    # server start up
    app.run(host='0.0.0.0', port=8080, debug=True)
```

# Start Server

Dependency package: `flask`
```bash
# Install dependency packages such as flask
$ python -m pip install -r requirements.txt
```

start the service
```bash
# start server
$ python filesserver.py
```

# Make this command
To run in any directory

create a file fileshare.bat with following code
```bash 
$ python D:\*custom_path*\filesserver.py
```

Now add `D:\*custom_path*` under `path` variable for the user under environment variables

Now you can run this server anywhere to activate this server in any folder
```bash 
$ fileshare
```

# Snapshot

[browser access: 127.0.0.1:8080](http://127.0.0.1:8080/)

![]()


