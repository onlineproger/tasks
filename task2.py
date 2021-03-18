import bs4
import requests
import time

class WikiParser:
	def __init__(self):
		self.session = requests.session()
		self.session.headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
		'Accept-Language': 'ru',
		}

	def parse_block(self, item):		
		letter = item.select('div.mw-category-group h3')[0].string.strip()	

		li_blocks = item.select('div.mw-category-group ul li')
		animals_count = len(li_blocks)

		dic = [letter, animals_count]		
		return dic

	def get_page(self, url, dct):
		r = self.session.get(url)
		text = r.text
		soup = bs4.BeautifulSoup(text, 'lxml')		

		container = soup.select('div.mw-category-group')		
		for item in container:	
			block = self.parse_block(item=item)

			value = dct.setdefault(block[0])
			if not value:
				dct.update({block[0]: block[1]})
			else:
				value+= block[1]
				dct.update({block[0]: value})			

		next_page = soup.select('#mw-pages > a:nth-child(7)')
		if next_page:			
			new_url = next_page[0].get('href')	# Ссылка на следующую страницу
			new_url = 'https://ru.wikipedia.org' + new_url			
			time.sleep(5)
			self.get_page(new_url, dct)		
		
		return "\n".join("{}: {}".format(k, v) for k, v in dct.items())

def main():
	p = WikiParser()
	dct = {}
	url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90'
	
	p.get_page(url, dct)	

if __name__ == '__main__':
	main()

# Результат полученный во время создания. 
# {'А': 1090, 'Б': 1504, 'В': 489, 'Г': 937, 'Д': 706, 'Е': 102, 'Ж': 381, 'З': 583, 'И': 325, 'Й': 3, 'К': 2078, 'Л': 665, 'М': 1183,
# 'Н': 433, 'О': 729, 'П': 1645, 'Р': 527, 'С': 1662, 'Т': 914, 'У': 227, 'Ф': 171, 'Х': 253, 'Ц': 206, 'Ч': 627, 'Ш': 259, 'Щ': 141,
# 'Э': 195, 'Ю': 125, 'Я': 194, 'A': 2589, 'B': 802, 'C': 2086, 'D': 888, 'E': 853, 'F': 187, 'G': 610, 'H': 886, 'I': 284, 'J': 75,
# 'K': 200, 'L': 881, 'M': 1495, 'N': 709, 'O': 726, 'P': 2289, 'Q': 36, 'R': 379, 'S': 1510, 'T': 1023, 'U': 127, 'V': 159, 'W': 82,
# 'X': 125, 'Y': 39, 'Z': 206}