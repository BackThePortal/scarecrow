from instaloader import Instaloader, Profile


# Gets the firsts posts and gets the most recent one, to deal with pins.
def get_last_post():
    dates = []

    L = Instaloader()



    profile = Profile.from_username(L.context, 'thetinmen')

    posts = profile.get_posts()

    i = 0
    for post in posts:
        dates.append(post.date_utc)
        i += 1
        if i == 4:
            break

    post_index = dates.index(max(dates))

    i = 0
    for post in posts:
        if i == post_index:
            print(post)
            break


get_last_post()
