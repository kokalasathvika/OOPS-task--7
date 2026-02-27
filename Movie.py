class Movie:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display_details(self):
        print(f"Movie: {self.name}")
        print(f"Rating: {self.rating} / 5")


# Input
name = input("Movie Name: ")
rating = input("Rating: ")

# Object creation
movie = Movie(name, rating)

# Display details
movie.display_details()