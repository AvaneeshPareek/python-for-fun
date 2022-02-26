from bs4 import BeautifulSoup
import requests
import smtplib

URL='https://www.flipkart.com/bkge-rectangular-sunglasses/p/itm8c3cef5cfb5a0?pid=SGLFYTWXXFXBFBVV&lid=LSTSGLFYTWXXFXBFBVVHJRFB7&marketplace=FLIPKART&fm=productRecommendation%2FattachForSwatchProducts&iid=R%3Aas%3Bp%3AWATFN6WFBSBYHTCX%3Bl%3ALSTWATFN6WFBSBYHTCXHUNGJW%3Bpt%3App%3Buid%3A0e944ade-9706-11ec-9dd3-91078d99a205%3B.SGLFYTWXXFXBFBVV&ppt=pp&ppn=pp&ssid=bwkhz3xyh9gqg9vk1645881271487&otracker=pp_reco_Frequently%2BBought%2BTogether_1_Frequently%2BBought%2BTogether_SGLFYTWXXFXBFBVV_productRecommendation%2FattachForSwatchProducts&otracker1=pp_reco_PINNED_productRecommendation%2FattachForSwatchProducts_Frequently%2BBought%2BTogether_NA_productCard_cc_1_NA_view-all&cid=SGLFYTWXXFXBFBVV'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, features='lxml')

title = soup.find("span",{"class":"B_NuCI"}).get_text()

price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()

rating = soup.find("div",{"class":"_3LWZlK _3uSWvT"}).get_text()

