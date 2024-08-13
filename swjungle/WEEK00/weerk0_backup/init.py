import os
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://eun0571:573582@cluster0.kuzvz3p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbjungle
# HTML 파일들이 있는 디렉토리 경로를 설정합니다.
directory_path = './html_files'  # 여기에 실제 디렉토리 경로를 입력하세요.
db['stores'].drop()
# 디렉토리 내의 모든 파일을 반복하여 처리합니다.
for filename in os.listdir(directory_path):
    if filename.endswith('.html'):
        file_path = os.path.join(directory_path, filename)
        
        # HTML 파일 열기
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html_content, 'lxml')
        
        # 필요한 데이터 추출 예시
        # 모든 <a> 태그의 텍스트와 href 속성을 추출합니다.
        
        tag_element = soup.select_one('#_title > div > span.GHAhO')
        name = tag_element.text.strip() if tag_element else "No name available"
        print(f"Name: {name}")  # 디버깅 출력
        tag_element = soup.select_one('#_title > div > span.lnJFt')
        category = tag_element.text.strip() if tag_element else "No category available"
        print(f"Category: {category}")  # 디버깅 출력
        img_src0 = soup.select_one('#ibu_1')
        img_src1 = soup.select_one('#ibu_2')
        img_src2 = soup.select_one('#ibu_3')
        img_src3 = soup.select_one('#ibu_4')
        img_src4 = soup.select_one('#ibu_5')
        img_src_list = soup.select('[id^="연관사진"]')
        
        img_src = [i['src'] for i in [img_src0, img_src1, img_src2, img_src3, img_src4] if i]

        for i in img_src_list:
            if i:
                img_src.append(i['src'])
                
        img_src.sort(reverse=True)
        if len(img_src)>3:
            img_src = img_src[:3]
        for i in img_src:
            print(f"Images: {img_src}")  # 디버깅 출력
        all_elements0 = soup.select('#app-root > div > div > div > div:nth-child(5) > div > div:nth-child(2) > div.place_section_content > div > div.O8qbU.pSavy > div > a > div > div > .A_cdD > .i8cJw')
        all_elements1 = soup.select('#app-root > div > div > div > div:nth-child(5) > div > div:nth-child(2) > div.place_section_content > div > div.O8qbU.pSavy > div > a > div > div > .A_cdD > .H3ua4')
        all_elements1_1 = []
        def get_text_with_linebreaks(element):
            text = ""
            for item in element.contents:
                if isinstance(item, str):
                    text += re.sub(r'\s+', ' ', item)
                    print(item)
                elif item.name == 'span':
                    text += re.sub(r'\s+', ' ', item.get_text())
                elif item.name == 'br':
                    text += '\n'
            return text
        for element1 in all_elements1:
            all_elements1_1.append(get_text_with_linebreaks(element1))

        filtered_elements = [re.sub(r'\n', '@', all_elements0[i].text+"\n"+all_elements1_1[i]) for i in range(len(all_elements0))]
        print(filtered_elements)
        divided_elements = []
        for i in range(len(filtered_elements)):
            a = filtered_elements[i].split('@')
            divided_elements.append(a)

        def weeks_sort(b):
            bc = []
            for i in range(len(b)):
                if '월' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '화' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '수' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '목' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '금' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '토' in b[i][0]:
                    bc.append(b[i])
            for i in range(len(b)):
                if '일' in b[i][0]:
                    bc.append(b[i])
            return bc
        sorted_elements = weeks_sort(divided_elements)   

        # description_element = soup.select_one('#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.Od79H > div > div > div.Ve1Rp > div')  # description 추출
        # description = description_element.text.strip() if description_element else "No description available"
        tag_element = soup.select_one('.T8RFa.CEyr5')
        description = re.sub(r'[ \t]+', ' ', tag_element.text if tag_element else " ")

        store = {
            'name': name,
            'category': category,
            'img_src': img_src,
            'open': sorted_elements,
            'description': description
        }
        # print(store)
        redundancy = db.stores.find_one({'name': name})
        if redundancy:
            pass
        elif (len(img_src)>2):
            db.stores.insert_one(store)  # MongoDB에 저장

            {{'like':3,'name':'a'},{'like':2,'name':'b'}}
