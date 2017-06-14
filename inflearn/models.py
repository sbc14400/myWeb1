class Text:
    def __init__(self,str):
        self.text=str

    def __str__(self):
        return "Object overrided to str: " + self.text

    def getLength(self):
        return len(self.text)



# Text class로부터 상속받는 Article class 작성
# Text : Parent Class, Super class
# Article : Child Class, Sub class
# Article extends to Text
class Article(Text):
    def __init__(self, title, text):
        self.title=title
        self.text=text

    def __str__(self):
        return "Article : %s %s" % (self.title, self.text)



class User:
    numbers=0
    # numArticle=0 (요기다 쓰면 모든 instance마다 초기화된다.)
    def __init__(self,name):
        self.numArticle = 0
        self.name=name
        self.articles=[]
        User.numbers += 1

    def write(self, text):
        self.articles.append(text)
        self.numArticle += 1

    def __str__(self):
        return "User : %s %s" % (self.name, self.articles)


t=Text("This is some text.")
t2=Text("This is some text2.")
user=User("sbc14400")
user.write(t)
user.write(t2)
print(t, t.getLength())
print(t2, t2.getLength())
print(user, user.numArticle)


t=Article("Hello", "This is some text.")
t2=Article(title="world", text="This is some text2.")
user=User("sbc14400")
user.write(t)
user.write(t2)
print(t, t.getLength())
print(t2, t2.getLength())
print(user, user.numArticle)

# 실행을 위해서는 ctrl+shift+B 사용한다. (at atom)
# 실행 명령어 : ctrl+Shift+F10 (at Pycharm)
