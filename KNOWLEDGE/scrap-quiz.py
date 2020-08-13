from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
from urllib.request import Request
import re

questions=open('QUESTIONS/demo.csv','a')

def markQuA(sols,ans):
    refer={"A":0 , "B":1 , "C":2 ,"D":3}
    i=refer[ans]
    answer=sols[i]
    answers=[]
    answers.append(answer)
    sols.remove(answer)
    answers.extend(sols)
    return answers


def writeData(containers):
    for container in containers:

        question = container.find("div",{"class":"wp_quiz_question testclass"}).text
        question = question.replace("   ","")
        question = re.sub(r'^.*?.',"",question)
        question = re.sub(r'[0-9.]',"",question)
        question = question.strip()

        try:
            answer=container.find("div",{"class":"wp_quiz_question_options"}).text
            chrs=["[A]","[B]","[C]","[D]","    ","\n"]
            answers =[]
            answers = answer.split("[C]")
            answers.extend(answers[0].split("[B]"))
            answers.remove(answers[0])
            answers.extend(answers[0].split("[D]"))
            answers.remove(answers[0])
            for i in range(len(answers)):
                for j in chrs:
                    if j in answers[i]:
                        answers[i]=answers[i].replace(j,"")
                answers[i]=answers[i].strip()
        except AttributeError:
            return 0


        ans = container.find("div",{"class":"ques_answer"}).text
        ans = ans.split(":")[1]
        ans = re.sub(r"[\[\]]","",ans).strip().split(" ",1)[0]

        answers = markQuA(answers,ans)
        sentance = "|".join(answers)

        questions.write("\""+question+"\""+",")
        questions.write("\""+sentance+"\""+",")
        questions.write("\""+"Technology"+"\""+",")
        questions.write("\""+"Hard"+"\"")
        questions.write("\n")


# https://www.indiabix.com/general-knowledge/technology/015001
# https://www.indiabix.com/general-knowledge/technology/016001

for i in range(1,11):
    url="https://www.gktoday.in/quizbase/indian-geography-mcqs?pageno={}".format(i)

    # uClient=uReq(url)
    # page_html=uClient.read()
    # uClient.close()
    req=Request(url, headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'})
    page_html=uReq(req).read()
    page_soup=soup(page_html,"html.parser")

    containers=page_soup.findAll("div",{"class":"sques_quiz"})
    writeData(containers)
    # answer=containers[8].find("div",{"class":"wp_quiz_question_options"}).text
    # print(answer)
    # question = containers[8].find("div",{"class":"wp_quiz_question testclass"}).text
    # print(question)
    # break








questions.close()