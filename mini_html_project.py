from horoscope_myvers import create_prophecies
from datetime import datetime as dt

paragraphs = create_prophecies()

def generate_head():
    head = f"""<head>
        <meta charset='utf-8'>
        <title>Гороскоп на сегодня</title>
    </head>"""
    return head
head = generate_head()

def generate_body(paragraphs):
    header = 'Что день готовит' + str(dt.now().date())
    body = f"   <h1>{header}</h1>"          #indentation for html readability
    for p in paragraphs:
        body += f'''
            <p>{p}</p>'''
    return f'''<body>
    {body}
    </body>'''
body = generate_body(paragraphs)

def generate_page(head,body):
    own_page =  f'''<html>
    {head}
    {body}
    </html>'''
    return own_page
page = generate_page(head,body)

def save_page(page):
    fp = open("index.html", "w")
    print(page, file=fp)
    fp.close()

save_page(page)
