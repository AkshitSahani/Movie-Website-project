import fresh_tomatoes
import media

#creating various instances of the class Movie:
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "1995",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

three_idiots = media.Movie("3 Idiots",
                           "Student life in India",
                           "2009",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyOTg0ODQ1OF5BMl5BanBnXkFtZTcwNjc0NTMwNQ@@._V1_SX640_SY720_.jpg",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w")

spirited_away = media.Movie("Spirited Away",
                            "Adventure into a different world",
                            "2001",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjYxMDcyMzIzNl5BMl5BanBnXkFtZTYwNDg2MDU3._V1_.jpg",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

top_gun = media.Movie("Top Gun",
                      "Story of a top American fighter pilot",
                      "1986",
                      "http://t2.gstatic.com/images?q=tbn:ANd9GcSVCaXEcuVO3eMn2X0c0_TGdISkfQMfyy1lRkTZ88sfIIj-g-5d",
                      "https://www.youtube.com/watch?v=qAfbp3YX9F0")

pretty_woman = media.Movie("Pretty Woman",
                           "Incredible and romantic love story",
                           "1990",
                           "http://t3.gstatic.com/images?q=tbn:ANd9GcSt9hkzW8Ubjyu-_4fdFK4XSI3BpZ02EPrz8Gxyfo64BiOqvRms",
                           "https://www.youtube.com/watch?v=Wzii8IuL8lk")

rang_de_basanti = media.Movie("Rang De Basanti",
                              "Story of college friends in India who take matter into their own hands when the government doesnt do its job",
                              "2006", 
                              "http://www.gstatic.com/tv/thumb/movieposters/160770/p160770_p_v8_aa.jpg",
                              "https://www.youtube.com/watch?v=9U5gGXvJxO8")

moana = media.Movie("Moana",
                    "Incredible animation of the life in Hawaiian islands",
                    "2016",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

the_martian = media.Movie("The Martian",
                          "Spellbinding story of a astronaut travelling to mars",
                          "2015",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

dr_strange = media.Movie("Doctor Strange",
                         "Spellbinding story of a doctor who loses everything, only to gain more special powers",
                         "2016",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcSmG4ms8wxdnuKOwetpc4qltTv7pHopDLRTi-t98dx-L-kt_b1t",
                         "https://www.youtube.com/watch?v=HSzx-zryEgM")

#appending movies into a list:
movies = [toy_story, three_idiots, spirited_away, top_gun, pretty_woman, rang_de_basanti, moana, the_martian, dr_strange]

#calling the external rendering function that will use the information above to create a movie website:
fresh_tomatoes.open_movies_page(movies)
