import instaloader as insta #pip install instaloader

mod = insta.Instaloader()

user = input("enter:")

mod.download_profile(user,profile_pic_only=True)

input()