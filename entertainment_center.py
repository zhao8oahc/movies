import media
import fresh_tomatoes

"""This file provides the instances of Movie. """

shawshank_redemption = media.Movie(
                        "Shawshank Redemption",
                        "An innocent banker's life in prison.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg# NOQA",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

titanic = media.Movie(
                      "Titanic",
                      "A fictionalized account of the sinking of the Titanic",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg# NOQA",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

life_is_beautiful = media.Movie(
                                "Life is Beautiful",
                                "A Jewish Italian book shop owner shield " +
                                "his son from the horrors of internment in " +
                                "a Nazi concentration camp. ",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg# NOQA",
                                "https://www.youtube.com/watch?v=zqAVwCK4r2Q")


fantasia = media.Movie(
                       "Fantasia 2000",
                       "Fantasia 2000 consists of animated segments set to" +
                       "pieces of classical music.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Fantasia2000_Poster.jpg/220px-Fantasia2000_Poster.jpg# NOQA",
                       "https://www.youtube.com/watch?v=QsNgdYVAv2w")

beauty_and_the_beast = media.Movie(
                                    "Beauty and the beast",
                                    "Beauty and the Beast focuses on the " +
                                    "relationship between the Beast and Belle",
                                    "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg# NOQA",
                                    "https://www.youtube.com/watch?v=tRlzmyveDHE# NOQA")


zootopia = media.Movie(
                       "Zootopia",
                       "It details the unlikely partnership between a " +
                       "rabbit police officer and a red fox con artist, as " +
                       "they uncover a conspiracy involving the " +
                       "disappearance of savage predator inhabitants of " +
                       "a mammalian metropolis.",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg# NOQA",
                       "https://www.youtube.com/watch?v=bY73vFGhSVk")

movies = [
        shawshank_redemption, titanic, life_is_beautiful,
        fantasia, beauty_and_the_beast, zootopia]
fresh_tomatoes.open_movies_page(movies)
