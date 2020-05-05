import pyautogui
import pyperclip
import time
# import cv2

def chat(position):
    while True:
        try:
            location = pyautogui.locateCenterOnScreen("images/chat_window.png",confidence=0.9)
            if location is not None:
                pyperclip.copy(position)
                pyautogui.click(location)
                for i in range(15):
                    pyautogui.hotkey('ctrl','v')
                    time.sleep(0.05)
                    pyautogui.press('enter')
                break
        except OSError:
            pass

def search(champion):
    while True:
        try:
            location = pyautogui.locateCenterOnScreen("images/search_window.png",confidence=0.9)
            if location is not None:
                pyperclip.copy(champion)
                pyautogui.click(location)
                pyautogui.hotkey('ctrl','v')
                break
        except OSError:
            pass

def champ(champion, champions):
    while True:
        location = pyautogui.locateCenterOnScreen("images/champion/"+champions[champion]+".png",confidence=0.9)
        if location is not None:
            pyautogui.click(location)  
            break

def ready():
    while True:
        location = pyautogui.locateCenterOnScreen("images/ready_button.png",confidence=0.9)
        if location is not None:
            pyautogui.click(location)
            break

if __name__ == "__main__":
    champions = {'아트록스':'aatrox','아리':'ahri','아칼리':'akali','알리스타':'alistar','아무무':'amumu','애니비아':'anivia','애니':'annie',
    '아펠리오스':'apheliose','애쉬':'ashe','아지르':'azir','바드':'bard','블리츠크랭크':'blitzcrank','브랜드':'brand','브라움':'braum','케이틀린':'caitlyn',
    '카밀':'camille','카시오페아':'cassiopeia','초가스':'chocath','코르키':'corki','다리우스':'darius','다이애나':'diana','드레이븐':'draven',
    '에코':'ekko','엘리스':'elise','이블린':'evelynn','이즈리얼':'ezreal','피들스틱':'fiddlesticks','피오라':'fiora','피즈':'fizz','갈리오':'galio',
    '갱플랭크':'gangplank','가렌':'garen','나르':'gnar','그라가스':'gragas','그레이브즈':'graves','헤카림':'hecarim','하이머딩거':'heimerdinger',
    '잔나':'janna','자르반':'jarvan','잭스':'jax','제이스':'jayce','진':'jhin','징크스':'jinx','카이사':'kaisa','칼리스타':'kalista',
    '카르마':'karma','카서스':'karthus','카사딘':'kassadin','카타리나':'katarina','케일':'kayle','케인':'kayn','케넨':'kennen',
    '카직스':'khazix','킨드레드':'kindred','클레드':'kled','코그모':'kogmaw','르블랑':'leblanc','리신':'leesin','레오나':'leona',
    '리산드라':'lissandra','일라오이':'illaoi','이렐리아':'irelia','루시안':'lucian','룰루':'lulu','럭스':'lux','아이번':'ivern',
    '말파이트':'malphite','말자하':'malzahar','마오카이':'maokai','마스터이':'masteryi','미스포츈':'missfortune','모데카이저':'mordekaiser',
    '모르가나':'morgana','문도':'mundo','나미':'nami','나서스':'nasus','노틸러스':'nautilus','니코':'neeko','니달리':'nidalee',
    '녹턴':'nocturne','누누':'nunu','올라프':'olaf','오리아나':'orianna','오른':'ornn','판테온':'pantheon','뽀삐':'poppy',
    '파이크':'pyke','키아나':'qiyana','퀸':'quinn','라칸':'rakan','람머스':'rammus','렉사이':'reksai','레넥톤':'renekton','렝가':'rengar',
    '리븐':'riven','럼블':'rumble','라이즈':'ryze','세주아니':'sejuani','세나':'senna','세트':'sett','샤코':'shaco','쉔':'shen',
    '쉬바나':'shyvana','신지드':'singed','사이온':'sion','시비르':'sivir','스카너':'skarner','아우렐리온솔':'sol','소나':'sona','소라카':'soraka',
    '스웨인':'swain','사일러스':'sylas','신드라':'syndra','탐켄치':'tahmkench','탈리야':'taliyah','탈론':'talon','타릭':'taric',
    '티모':'teemo','쓰레쉬':'thresh','트리스타나':'tristana','트런들':'trundle','트린다미어':'tryndamere','트위스티드페이트':'twistedfate',
    '트위치':'twitch','우디르':'udyr','우르곳':'urgot','바루스':'varus','베인':'vayne','베이가':'veigar','벨코즈':'velkoz',
    '바이':'vi','빅토르':'viktor','블라디미르':'vladimir','볼리베어':'volibear','워윅':'warwick','오공':'wukong','자야':'xayah',
    '제라스':'xerath','신짜오':'xinzhao','야스오':'yasuo','요릭':'yorick','유미':'yuumi','자크':'zac','제드':'zed','직스':'ziggs',
    '질리언':'zilean','조이':'zoe','자이라':'zyra'}
    position = pyautogui.prompt(text='Enter position', title='League of Legends AutoPicker' , default='')
    champion = pyautogui.prompt(text='Enter champion', title='League of Legends AutoPicker' , default='')
    while True:
        chat(position=position)
        search(champion=champion)
        time.sleep(1)
        champ(champion=champion, champions=champions)
        time.sleep(3)
        ready()
        break
