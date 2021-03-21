
config = {
    # Google Cloud Credentials
    'CLIENT_ID': 'XXXXXXXXXXXXXXX.apps.googleusercontent.com',
    'CLIENT_SECRET': 'XXXXXXXXXXXXXXXXXX',
    'OAUTH_SCOPE': ['https://www.googleapis.com/auth/webmasters.readonly', 'https://www.googleapis.com/auth/analytics.readonly'],
    # Email Associated with CLIENT_ID & CLIENT_SECRET
    'GOOGLE_CREDENTIALS': 'exampleemail@gmail.com',

    # GSC data
    'ROW_LIMIT': 25000,
    'DATA_FOLDER': 'data',

    # Proxy Service
    'PROXY_ENDPOINT': 'https://my-project.appspot.com/render/<URL>',

    'RANDOM_SEED': 12345,

}
