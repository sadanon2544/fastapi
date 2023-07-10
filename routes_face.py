import requests
from urllib.parse import urlencode

def facebook_login(app_id, redirect_uri):
    params = {
        'client_id': app_id,
        'redirect_uri': "https://botnoi-atdj.onrender.com/callback",
        'response_type': 'code',
        'scope': 'email'  # Add additional permissions as required
    }
    url = f'https://www.facebook.com/v12.0/dialog/oauth?{urlencode(params)}'
    print('Please open the following URL and login with your Facebook account:')
    print(url)
    code = input('Enter the authorization code from the URL: ')
    return RedirectResponse(url)


def get_user_info(access_token):
    code = request.query_params.get("code")
    params = {
        'client_id': "1300273574255667",
        'redirect_uri': "https://botnoi-atdj.onrender.com/callback",
        'client_secret': "e7c85850d410d960ae41c6554a4c8cdd",
        'code': code
    }
    url = 'https://graph.facebook.com/v12.0/oauth/access_token'
    response = requests.get(url, params=params)
    data = response.json()
    if 'access_token' in data:
        access_token = data['access_token']
    else:
        raise Exception('Access token retrieval failed.')
        
    params = {'access_token': access_token}
    url = 'https://graph.facebook.com/v12.0/me'
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    return data

redirect_uri = 'https://botnoi-atdj.onrender.com/'  # Replace with your own redirect URI

print('User Information:')
print(f"Name: {user_info['name']}")
print(f"Email: {user_info['email']}")
