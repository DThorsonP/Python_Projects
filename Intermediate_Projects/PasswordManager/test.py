try:
    file = open("noneFile.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("noneFile.txt", "w")
    file.write("1234")
except NameError as error_message:
    print(f"The key {error_message} does not exist")
    

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")

make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post['Likes']
        except KeyError:
            pass
    return total_likes
        
count_likes(facebook_posts)
