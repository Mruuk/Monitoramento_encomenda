import requests
from bs4 import BeautifulSoup
import hashlib

url_base = 'https://www.linkcorreios.com.br/?id='

def get_scrapping_correios(tracker, data_at):
  result_tracker = ""

  try:
    message = f"Conforme solicitado, segue o status atual do seu objeto #{tracker}: \n"
    response = requests.get(f'{url_base}{tracker}')
    print(f'{url_base}{tracker}')
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')
    
    return_status = soup.find('ul', class_="linha_status m-0")
    result_tracker = f"{message} {return_status.get_text()}"
    print(result_tracker)
  except:
    result_tracker = "Falhou"
    pass
  
  data = return_status.find_all('li')[1]
  print(return_status)
  # Calculate the hash of the new data.
  data = hashlib.sha256(data.encode('utf-8')).hexdigest()
  if data == data_at:
    verifica = True
  else:
    verifica = False

  return result_tracker, verifica, data