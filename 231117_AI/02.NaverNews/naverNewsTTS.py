# 네이버 뉴스로부터 웹크롤링하기 위헤 requests 활용
import requests
import pyttsx3

# 네이버 뉴스 HTML 소스의 내용을 가져오기 위해 활용
from bs4 import BeautifulSoup

# 네이버는 정상적인 접근(사용자 직접 네이버 접속)이 아닌 웹 크롤링 등 비정상적인 접근을 방지 하게 위해 HTTP 헤더 정보를 요구함
# HTTP 헤더는 웹URL에 접속할 때, 네이버 서버에 제공하는 헤더 정보
# 네이버는 HTTP 헤더 정보 중 User-Agent 값의 유무를 체크함
# 따라서 네이버에 임의의 값을 넣어줌
headers = {
    "User-Agent": "Seoul Gangseo Campus of Korea Polvtechnics College. Dept. of Data Analvsis / Python Education"
}

# 수집할 신문기사 URL
webpage = requests.get("https://entertain.naver.com/read?oid=009&aid=0004968578", headers=headers)

# URL로부터 읽은 HTML 내용을 파이썬에서 처리할 수 있게 파싱하기
soup = BeautifulSoup(webpage.content, "html.parser")

# 신문기사 본문 내용을 문자열로 저장하기
# naver_news = soup.select_one("#dic_area").get_text().strip()
naver_news = soup.select_one("#articeBody").get_text().strip()

# 신문기사 출력
print(soup)
print(naver_news)

# 문자를 음성으로 변환하기는 TTS 라이브러리 가져오기
import pyttsx3

# TTS 사용하기 위해 초기화
tts = pyttsx3.init()

# 말하기 속도 조절(기본값 : 200 / 값이 클수록 말속도가 빠르며, 작으면 느림)
tts.setProperty("rate", 100)

# 문자를 음성으로 변환하기
tts.say(naver_news)

# 문자를 음성으로 다 읽어주기까지 파이썬 실행을 종료하지 않고 기다리기
tts.runAndWait()

# 문자를 모두 다 읽었으면, 실행종료하기
tts.stop()