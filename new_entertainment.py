import media
import fresh_tomatoes

"""list of movie objects"""
# Instance variable.  Brings up information for the movie "Inception" when run
# through the constructor.
inception = media.Movie("Inception",     # Title
                        "Dom Cobb (Leonardo DiCaprio) is a thief with the rare"
                        "ability to enter people's dreams and steal their"
                        "secrets from their subconscious. His skill has made"
                        "him a hot commodity in the world of corporate"
                        "espionage but has also cost him everything he loves."
                        "Cobb gets a chance at redemption when he is offered a"
                        "seemingly impossible task: Plant an idea in someone's"
                        "mind. If he succeeds, it will be the perfect crime,"
                        "but a dangerous enemy anticipates Cobb's every move.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/"
                        "Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")


# Instance variable.  Brings up information for the movie "Iron-Man" when run
# through the constructor.
iron_man = media.Movie("Iron Man",
                       "A billionaire industrialist and genius inventor, Tony"
                       "Stark (Robert Downey Jr.), is conducting weapons tests"
                       "overseas, but terrorists kidnap him to force him to"
                       "build a devastating weapon. Instead, he builds an"
                       "armored suit and upends his captors. Returning to"
                       "America, Stark refines the suit and uses it to combat"
                       "crime and terrorism",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/"
                       "Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")


# Instance variable.  Brings up information for the movie "The Prestige" when
# run through the constructor.
the_prestige = media.Movie("The Presitge",
                           "An illusion gone horribly wrong pits two"
                           "19th-century magicians, Alfred Borden"
                           "(Christian Bale) and Rupert Angier (Hugh Jackman),"
                           "against each other in a bitter battle"
                           "for supremacy. Terrible consequences loom when the"
                           "pair escalate their feud, each seeking not just to"
                           "outwit -- but to destroy -- the other man.",
                           "https://images-na.ssl-images-amazon.com/images/M/"
                           "MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_."
                           "jpg",
                           "https://www.youtube.com/watch?v=bH6CoVlD5xc")

# Instance variable.  Brings up information for the movie "Spirited Away" when
# run through the constructor.
spirited_away = media.Movie("Spirited Away",
                            "In this animated feature by noted Japanese"
                            "director Hayao Miyazaki, 10-year-old Chihiro"
                            "(Rumi Hiiragi) and her parents (Takashi Naitô,"
                            "Yasuko Sawaguchi) stumble upon a seemingly"
                            "abandoned amusement park. After her mother and"
                            "father are turned into giant pigs, Chihiro meets"
                            "the mysterious Haku (Miyu Irino), who explains"
                            "that the park is a resort for supernatural beings"
                            "who need a break from their time spent in the"
                            "earthly realm, and that she must work there to"
                            "free herself and her parents.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcS6MveoDo"
                            "JOg9-wMvtHE4ak_-HDZeYS1egb9PwRcf8lhrtcppMc",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

# Instance variable.  Brings up information for the movie "Point Break" when
# run
# through the constructor.
point_break = media.Movie("Point Break",
                          "After a string of bizarre bank robberies in"
                          "Southern California, with the crooks donning masks"
                          "of various former presidents, a federal agent,"
                          "Johnny Utah (Keanu Reeves), infiltrates the"
                          "suspected gang. But this is no ordinary group of"
                          "robbers. They're surfers -- led by the charismatic"
                          "Bodhi (Patrick Swayze) -- who are addicted to the"
                          "rush of thievery. But when Utah falls in love with"
                          "a female surfer, Tyler (Lori Petty), who is close"
                          "to the gang, it complicates his sense of duty.",
                          "http://t2.gstatic.com/images?q=tbn:"
                          "ANd9GcSg5eJ7B6CSA"
                          "31lD7Fu9RSCbFtyqBm4JezITWtb61sVpbzkwcKq",
                          "https://youtu.be/kPFlUSdse9g")
# Instance variable.  Brings up information for the movie "It Might Get Loud
# when run through the constructor.
it_might_get_loud = media.Movie("It Might Get Loud",
                                "Rock icons -- Jimmy Page, the Edge and Jack"
                                "White -- from three different generations"
                                "come together to discuss the electric guitar"
                                "and their musical influences. The men swap"
                                "stories and crank up their instruments on an"
                                "empty soundstage for a jam session. Along the"
                                "way, they visit the majestic hall where"
                                "Stairway to Heaven was composed, Jack White"
                                "composes a song on-camera at a Tennessee"
                                "farmhouse, and the Edge lays down tracks for"
                                "a U2 single.",
                                "http://www.gstatic.com/tv/thumb/movieposters/"
                                "195467/p195467_p_v8_aa.jpg",
                                "https://www.youtube.com/watch?v=ys2LKKfwTjU")


movies = [inception, iron_man, the_prestige, spirited_away, point_break,
          it_might_get_loud]  # list of movies for the page to open
fresh_tomatoes.open_movies_page(movies)   # open the list of movies
