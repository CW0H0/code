import requests  
from bs4 import BeautifulSoup  
  
# 构造请求URL  
url = 'https://quote.eastmoney.com/us/XPEV.html#fullScreenChart'  
  
# 发送HTTP请求  
headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'  
}  
response = requests.get(url, headers=headers)  
  
# 解析HTML数据  
soup = BeautifulSoup(response.text, 'html.parser')  
  
# 假设OHLC数据以特定的HTML标签形式存在，这里需要根据实际情况修改  
# 例如，使用find_all或select方法查找包含OHLC数据的标签  
ohlc_data = soup.find_all('div', class_='ohlc-data')  # 假设OHLC数据在class为'ohlc-data'的div标签中  
  
# 处理和存储OHLC数据（这里仅作为示例，具体实现方式取决于数据的结构和你的需求）  
for data in ohlc_data:  
    # 提取开盘价、最高价、最低价、收盘价  
    # 注意：这里的提取方式需要根据HTML结构的实际情况进行调整  
    open_price = data.find('span', class_='open').text  
    high_price = data.find('span', class_='high').text  
    low_price = data.find('span', class_='low').text  
    close_price = data.find('span', class_='close').text  
      
    # 打印或存储OHLC数据  
    print(f"Open: {open_price}, High: {high_price}, Low: {low_price}, Close: {close_price}")