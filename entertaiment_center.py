import fresh_tomatoes
import media


# You can add your movies here! Read README.md for instructions!
toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://cdn.collider.com/wp-content/uploads'
                        '/toy-story-poster1.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar', 'A marine on alien planet',
                     'http://www.foxmovies.com/movies/avatar/download-poster'
                     '/251',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

the_green_mile = media.Movie('The Green Mile',
                             'A story about innocent prisoner',
                             'https://upload.wikimedia.org/wikipedia/en'
                             '/thumb/c/ce/Green_mile.jpg/220px-Green_mile.jpg',
                             'https://www.youtube.com/watch?v=Ki4haFrqSrw')

terminator_2 = media.Movie('Terminator 2: Judgement Day',
                           'A story about robot who came in past to save the '
                           'life of one boy',
                           'https://shyfyy.files.wordpress.com/2012/02/t2.jpg',
                           'https://www.youtube.com/watch?v=z6PowtQLGoU')

x_men = media.Movie('X-Men', 'The mutants are trying to save the world',
                    'https://upload.wikimedia.org/wikipedia/en/thumb/8/8c'
                    '/XMen1poster.jpg/220px-XMen1poster.jpg',
                    'https://www.youtube.com/watch?v=Iy5R5_T243w')

alexander = media.Movie('Alexander', 'A story about the young leader of '
                        'the mighty empire',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/a/ae'
                        '/AlexanderPoster.jpg/220px-AlexanderPoster.jpg',
                        'https://www.youtube.com/watch?v=Bh6LKIdxqCU')


movies = [toy_story, avatar, the_green_mile, terminator_2, x_men, alexander]

# Add the titles of your movies here ↑↑↑

fresh_tomatoes.open_movies_page(movies)
