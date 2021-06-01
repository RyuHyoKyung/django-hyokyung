from selenium import webdriver
from bs4 import BeautifulSoup
class NaverMovie(object):


    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = '' # 공백으로 하면 input으로 외부에서 값을 받아야 함을 의미함
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    all_div = ()
    # 위 세개가 반드시 필요


    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)  # 크롬 드라이버를 사용할 것이다. (크롬드라이버는 스트링)
        driver.get(self.url)  # URL을 크롬 드라이버에 저장(원래는 내 컴퓨터에 저장, 크롬드라이버를 거쳐가면 안보이는 코드를 보여줄 수 있게 해준다.)
        soup = BeautifulSoup(driver.page_cource, 'html.parser')
        all_div = soup.find_all('div',{"class":self.class_name})  # 제목 뽑아오기, 네임 값은 생략가능 바로 사이트 태그 값을 넣는다. 구조는 맞춰줘야함.

        for i in range(0, len(self.all_div)):
            self.all_div.append(i.find("a").text)
        return self.scrap


        driver.close



if __name__ == '__main__':
    naver = NaverMovie()
    naver.class_name = input('input')
    print()
    naver.scrap()
