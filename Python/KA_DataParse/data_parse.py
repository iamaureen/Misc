import requests

#api end point
summary_URL = "https://www.khanacademy.org/api/internal/user/discussion/summary?casing=camel&email=alligator.modelbook%40areejm.com&kaid=kaid_282640918659561675890687&lang=en&_=200304-0923-c0033a5f7adb_1583350492063"

ques_URL = "https://www.khanacademy.org/api/internal/user/questions?casing=camel&email=alligator.modelbook%40areejm.com&kaid=kaid_282640918659561675890687&limit=10&page=0&sort=1&subject=all&lang=en&_=200304-1052-3e7713433dba_1583352503339"

r = requests.get(url = ques_URL)

data = r.json()

print(data)

dict = {}
questions = data

for q in questions:
  question_content = q['content']
  print (question_content)