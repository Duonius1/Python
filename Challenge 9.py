# Challenge 9
favorite_movies = []

for i in range(3):
    movie = input(f"What's your #{i+1} favorite movie? ") # Basically using an f string you can put
    favorite_movies.append(movie)                         # any variable in curly brackets
print (f"Your favorite movies are: {favorite_movies[0]}, {favorite_movies[1]} and {favorite_movies[2]}")

# There are also other prefixes for strings such as r (ignores backslashes, raw string), b (byte string), 
# \n and \t is newline/tab, """ """ are multi-line strings, same way as ''' '''are multi-line comments 
# Also look into "from string import Template" and .format