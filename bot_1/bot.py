from instapy import InstaPy


session = InstaPy(username='nikhill_kd',password='Shubhee@123')
session.login()
session.set_do_comment(enabled=True,percentage=100)

# session.set_do_follow(enabled=True,percentage=100)
# session.like_by_tags(['love','alone'],amount=5)
# users = session.target_list("C:\\Users\\......\\users.txt")
# session.follow_user_followers(users, amount=10, randomize=False)
session.like_by_users(['prayas.deshmukh'],amount=5)
session.set_comments(['Nice!','awsome','nicepost!'])

session.end()