'''class Details:
      def __init__(self,name,mail,pwd):
        self.name=name
        self._mail=mail
        self.__pwd=pwd

      def getpassword(self):
        return self.__pwd

      def setpassword(self):
        self.__pwd=new_password

sumanth= Details("Sumanth","sumanth@gmail","Sumanth@123")

print(sumanth.name)
sumanth.name="Sanjay"
print(sumanth.name)

print(sumanth._mail)
sumanth._mail="Sanjay@gmail'''



'''class Bank:
    def __init__(self):
        self.name="xyz"
        self._balance=0
    
    @property
    def noresbalance(self):
        self._balance

    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount

b=Bank()

print(b.noresbalance)
b.noresbalance=3000
print(b.noresbalance)

print(b.name)
b.name="abc"
print(b.name)'''




'''name="Vijayawada is a Royal City"
print(name[21:26] ,name[0:10],name[15:21],name[10:13])'''

'''name="Vijayawada is a Royal City"
print(name[-5:26],name[-26:-16],name[-11:-5],name[-16:-13])'''





'''#Multi-level Inheritance
#single Inheritance
class Status:
    def uploadImage(self,image):
        self.image = image
        print(f"{self.image} is uploaded to your status")
class StatusV1(Status):
    def addCaption(self,text=None):
        self.caption = text
        print(f"{self.caption} is added to yout status")

class StatusV2(Status):
    def like(self):
        print(f'You can like status')

class StatusV3(StatusV1,StatusV2):
    def addmusic(self,music):
        self.music=music
        print(f'{self.music}... is added to your status')

class StatusV4(StatusV3):
    def Videolength(self,video):
        self.video=video
        print(f'{self.video} is uploaded to your status')
        

ramya = Status()
ramya.uploadImage('Good Morning.png')

hema = StatusV1()

hema.uploadImage('God.png')
hema.addCaption('Om Sai ram..!')

vaishnavi=StatusV2()
vaishnavi.uploadImage("Coffee.png")
vaishnavi.like()

deepika=StatusV3
deepika.uploadImage("Mountains_and_Trees.png")
deepika.addCaption('no wifi')
deepika.like()
deepika.addMusic("Nature.mp3")

nikitha=StatusV4
nikitha.uploadImage("Car.png")
nikitha.addCaption("Nothing")
nikitha.like()
nikitha.addMusic("Music")
nikitha.videolength("Somevideo.mp4") '''
        

class  Instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,'-')}")

    def uploadPost(self,image):
        self.post.append(image)
        print(f"{image} is posted")
        
class InstagramV1(Instagram):
    def __init__(self,username,bio):
        super(). __init__ (username)
        self.bio=bio
        print(f'bio uploaded')

    def uploadPost(self,post,music):
        super().uploadPost(post)
        self.music=music
        print(f'{self.music} is added')


gopal=Instagram("Gundu Gopal")
gopal.uploadPost("NTR.png")


Sanjay=InstagramV1("Kphb Sanjay","KPHB King")
Sanjay.uploadPost("KPHB metro Station.png","Aatagadu.mp3")