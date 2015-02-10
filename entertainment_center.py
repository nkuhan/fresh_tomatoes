import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://shoutitforlife.com/wp-content/uploads/2011/02/Toy-Story-DVD95.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.frontrowreviews.co.uk/wordpress/wp-content/uploads/2010/08/poster_avatar-re-release.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

pappali = media.Movie("Pappali",
                      "Pappali is a tamil comedy film",
                      "http://3.bp.blogspot.com/-46JaCMqAZLg/VARxyvoIaHI/AAAAAAAABE4/cfy9JBbeA-o/s1600/Pappali-2014-Tamil-Full-Movie-Watch-Online-Free-DVDScr%2Bcopy.jpg",
                      "https://www.youtube.com/watch?v=ha58pCSx90c")
                      
kochadiiyaan = media.Movie("Kochadiiyaan",
                           "The Legend, a Soundarya Rajnikanth Ashwin film featuring Superstar Rajinikanth & Deepika Padukone in the lead roles.",
                           "http://www.future2see.com/wp-content/uploads/2013/09/kochadaiiyaan-release-confirmed.jpg",
                           "https://www.youtube.com/watch?v=lbJO8MBCyp4")

tenaliraman = media.Movie("Thenali Raman",
                          "Tenali Raman is an upcoming Tamil historical comedy film",
                          "http://i1.ytimg.com/vi/tE12Y88nmAQ/hqdefault.jpg",
                          "https://www.youtube.com/watch?v=ngGSjd9ctgY")

ghilli = media.Movie("Ghilli",
                     "Tamil super entertainment film",
                     "http://www.einthusan.com/images/covers/ghilli.jpg",
                     "https://www.youtube.com/watch?v=R0y6pSE9Pnw")



movies = [toy_story,avatar,pappali,kochadiiyaan,tenaliraman,ghilli ]
#fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
print "testing"