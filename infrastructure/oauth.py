from app import app
from authlib.integrations.flask_client import OAuth


CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
google = oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope':'openid profile email'
        },
)