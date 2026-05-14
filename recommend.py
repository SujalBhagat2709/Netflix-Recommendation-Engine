from movies import get_movies

def recommend_movies(genre):
    
    movies = get_movies()
    
    recommendations = []
    
    for movie in movies:
        
        if movie["genre"].lower() == genre.lower():
            recommendations.append(movie)
    
    return recommendations


if __name__ == "__main__":
    
    result = recommend_movies("Sci-Fi")
    
    print(result)