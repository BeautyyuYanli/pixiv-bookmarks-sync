from main import *
if not os.path.exists('download'):
    os.makedirs('download')
if not os.path.exists('download/imgs'):
    os.makedirs('download/imgs')
if not os.path.exists('download/info'):
    os.makedirs('download/info')
if (login(refresh_token) == 1):
    initDown()
    # appendDown()