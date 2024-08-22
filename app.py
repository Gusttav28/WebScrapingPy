import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/-/es/hz/mobile/mission/?_encoding=UTF8&p=HoLwnus9Z0A3Pu69g52DCdeZiq2CEXsQi%2F6%2FHi3MDAAevUD2CUoojCX0GCbb3mq5hiqzBgUj3kDkIcL2VGxwLjIma2WfiKTlKg2MLufyLQ4fWVPWkTAZrllyd0qAg5qPiddRWmigH%2F86UgjRjy02X53UMNAHk74e4C2FkTgJX2Is34Pv7b%2BQP%2Fp%2FHkegG8j%2FZ%2FSZQO7EsMN6thsupspj8%2B6vMomFO3vYaLUKEONiJ8SJlWqCrhTGAyCGtiUnMycEOvYKkGwbGrsnRt5VwAILE7YdYTA5KcTUHMZQx%2BecAoqI81bes%2Fbb2pREUprYl3UrA3YqceerXnkKXsPFhmVYnbzimL7VfZI2uE5l2WYTNXqg0kCD%2BCjT93Saj%2B%2FjNnoYExrYb95CgKaRoad%2BdoyIzSqAFUSW0VQQ5VtiWAZT31A%3D&pd_rd_w=oi8xy&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=CBFNM5CZ76VQ1VYTDWFM&pd_rd_wg=FGjjC&pd_rd_r=5830dc4c-1aea-4d91-903a-6b34f568cd2d&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"


response = requests.get(url)

if response.status_code == 200:
    print("it works")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    products = soup.find_all('div', class_="a-section _p13n-mission-desktop-carousel_style_productContainer__3p81X")
    # print(products)
    
    
    for product in products:
        title = product.find('div', class_="a-section a-spacing-none _p13n-mission-desktop-carousel_style_bottomContainer__3H7zq")
        if title:
            print(title.text.strip())
            
else:
    print("it does'nt work: ", response.status_code)