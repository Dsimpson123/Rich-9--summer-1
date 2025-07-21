import CreateClass 
movies = ["Friday", "Friday After the next", "Madea family reunion"]
games = ["GTA,", "Madden", "College Football 26"]


my_collection = CreateClass.Collection(["Inception", "The Matrix"], ["Zelda", "Mario Kart"])
my_collection.SetFavGame("GTA")
my_collection.SetFavMovie("Friday")
my_collection.DisplayCollection()