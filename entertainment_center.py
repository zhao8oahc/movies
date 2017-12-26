import media
import fresh_tomatoes

"""This file provides the instances of Movie. """

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the Stephen King novella Rita Hayworth and Shawshank Redemption. It tells the story of banker Andy Dufresne, who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence. Over the following two decades, he befriends a fellow prisoner, contraband smuggler Ellis \"Red\" , and becomes instrumental in a money laundering operation led by the prison warden Samuel Norton",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

titanic = media.Movie("Titanic",
                      "A fictionalized account of the sinking of the RMS Titanic, it stars Leonardo DiCaprio and Kate Winslet as members of different social classes who fall in love aboard the ship during its ill-fated maiden voyage.",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

life_is_beautiful = media.Movie("Life is Beautiful",
                                "Life Is Beautiful is a 1997 Italian comedy-drama film directed by and starring Roberto Benigni, who co-wrote the film with Vincenzo Cerami. Benigni plays Guido Orefice, a Jewish Italian book shop owner, who employs his fertile imagination to shield his son from the horrors of internment in a Nazi concentration camp. ",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg",
                                "https://www.youtube.com/watch?v=zqAVwCK4r2Q")


fantasia = media.Movie("Fantasia 2000",
                       "Fantasia 2000 consists of animated segments set to pieces of classical music.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Fantasia2000_Poster.jpg/220px-Fantasia2000_Poster.jpg",
                       "https://www.youtube.com/watch?v=QsNgdYVAv2w")

beauty_and_the_beast = media.Movie("Beauty and the beast",
                     "Beauty and the Beast focuses on the relationship between the Beast, a prince who is magically transformed into a monster and his servants into household objects as punishment for his arrogance, and Belle, a young woman whom he imprisons in his castle. To become a prince again, Beast must learn to love Belle and earn her love in return before the last petal from the enchanted rose that the enchantress who cursed the Beast had offered falls, or else the Beast will remain a monster forever. ",
                     "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",
                     "https://www.youtube.com/watch?v=tRlzmyveDHE")


zootopia = media.Movie("Zootopia",
                       "It details the unlikely partnership between a rabbit police officer and a red fox con artist, as they uncover a conspiracy involving the disappearance of savage predator inhabitants of a mammalian metropolis.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")

movies = [shawshank_redemption, titanic, life_is_beautiful, fantasia, beauty_and_the_beast, zootopia]
fresh_tomatoes.open_movies_page(movies)
