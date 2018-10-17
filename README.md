import cloudinary
import cloudinary.api
cloud = cloudinary.config.update = ({
    'user',
    'key',
    'where4'
})
from bitching import app
cloudinary.config(cloud_name='df7hg9q6i', api_key='639662597519516',
                  api_secret='cC2ak5GbxVWkbr9qg4UphZOBrw4')
app.secret_key="custom_key"
