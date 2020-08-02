def book_parser(book):
    volume_info = book["volumeInfo"]
    book_data = {
        "title": volume_info["title"],
        "authors": volume_info["authors"],
        "published_date": volume_info["publishedDate"],
        "categories": volume_info.get("categories", []),
        "average_rating": volume_info.get("averageRating", 0),
        "ratings_count": volume_info.get("ratingsCount", 0),
        "thumbnail": volume_info["imageLinks"]["thumbnail"]
    }
    return book_data