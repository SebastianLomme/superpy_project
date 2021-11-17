def won_golden_globe(movie_name):
    globe_winners = ['Star Wars: Episode IV – A New Hope', 'Jaws','E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']
    return [movie for movie in movie_name if movie in globe_winners]

movie_list = ['Star Wars', 'Superman', 'Indiana Jones', 'Jaws', 'Jurassic Park', 'E.T. the Extra-Terrestrial', 'Schindler"s List', 'Home Alone', 'Harry Potter']

print("List: ", won_golden_globe(movie_list))

# Python code for implementation of lower()

# Checking for lowercase characters
