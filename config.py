BASE_PATH = 'https://data.fixer.io/api/latest?access_key='
API_KEY = 'ZRV9xshx1LyqZuSEBTDVQ02hdF95N0DJ'

url = BASE_PATH + API_KEY

EMAIL_RECEIVER = 'example@inprobes.com'


# rules = {
#     'archive': True,
#     'send_mail': True,
#     'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD'],
#     'notification': True
# }

rules = {
    'archive': True,
    'email': {
        'receiver': 'example@inprobes.com',
        'enable': True,
        'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'CAD'],
    },
    'notification': {
        'enable': True,
        'receiver': '09123456789',
        'preferred': {
            'BTC': {'min': 0.000101, 'max': 0.000110},
            'IRR': {'min': 45000, 'max': 50000}
        }
    }
}
