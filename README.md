# Bitching

## SAMPLE config.py
```pythonimport cloudinary
import cloudinary.api
cloud = cloudinary.config.update = ({
    'cloud_name',
    'api_key',
    'api_secret'
})
from bitching import app
cloudinary.config(cloud_name='cloud_name', api_key='api_key',
                  api_secret='api_secret')
app.secret_key="custom_key" 
```

## setup virtual environment
*from project directory*

```ssh pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
## create database
```ssh 
./db.sh
```
Then you are good to python ```python run.py ```
