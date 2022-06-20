import os
from pickle import TRUE

import dotenv

dotenv.load_dotenv('/Users/pk/Documents/GitHub/Invest-o-matic/.env')


GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
DATABASE_URL = os.getenv('DATABASE_URL')


