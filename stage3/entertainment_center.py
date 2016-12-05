import media
import fresh_tomatoes


hacksaw_ridge = media.Movie(movie_title = 'Hacksaw Ridge',
                   movie_storyline = 'WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people and becomes the first Conscientious Objector in American history to be awarded the Medal of Honor.',
                   poster_image = 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1NjM3MTUxNV5BMl5BanBnXkFtZTgwMDc5MTY5OTE@._V1_SY1000_CR0,0,647,1000_AL_.jpg',
                   trailer_youtube = 'https://www.youtube.com/watch?v=s2-1hz1juBI')

dr_strange = media.Movie(movie_title = 'Dr. Strange',
                         movie_storyline = 'A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.',
                         poster_image = 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2ODA4MTM0M15BMl5BanBnXkFtZTgwNzE5OTYxMDI@._V1_SY1000_CR0,0,683,1000_AL_.jpg',
                         trailer_youtube = 'https://www.youtube.com/watch?v=Lt-U_t2pUHI')

girl_on_the_train = media.Movie(movie_title = 'The Girl on the Train',
                                movie_storyline = 'A divorcee becomes entangled in a missing persons investigation that promises to send shockwaves throughout her life.',
                                poster_image = 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwNDU4NTQwMl5BMl5BanBnXkFtZTgwMzQ2MjIwMDI@._V1_SY1000_CR0,0,631,1000_AL_.jpg',
                                trailer_youtube = 'https://www.youtube.com/watch?v=y5yk-HGqKmM')

# hacksaw_ridge.show_trailer()

movies = [hacksaw_ridge, dr_strange, girl_on_the_train]

fresh_tomatoes.open_movies_page(movies = movies)