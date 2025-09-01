'''class NormalUser:
      def playvideo(self,name):
            print(f"\n is playing video with :\n1.Normal Quality\n2.Ads run\n3.No Background play\n4. limited Download \n5.Music with Ads")
      def likes(self):
            pass
      def comments(self):
            pass
      def share(self):
            pass
      def title(self):
            pass
      def subscribe(self):
            pass
      
class premiumUser(NormalUser):
      def playvideo(self,name):
            print(f"\n is playing video with :\n1.High Quality\n2.No Ads \n3.Background play\n4.Download anything\n5.Music without Ads")

dinesh=NormalUser()
sanjay=premiumUser()

dinesh.playvideo("Dinesh")
sanjay.playvideo("Sanjay")'''


class NormalUser:
      def playvideo(self,name):
            print(f"\n is playing video with :\n1.Normal Quality\n2.Ads run\n3.No Background play\n4. limited Download \n5.Music with Ads")
      
class premiumUser(NormalUser):
      def playvideo(self,name):
            print(f"\n is playing video with :\n1.High Quality\n2.No Ads \n3.Background play\n4.Download anything\n5.Music without Ads")

def play_video(user,username):
    user.playvideo(username)

dinesh=NormalUser()
sanjay=premiumUser()
tarak=premiumUser()
mohith=NormalUser()

play_video(dinesh,"dinesh")
play_video(sanjay,"sanjay")
play_video(tarak,"tarak")
play_video(mohith,"mohith")

