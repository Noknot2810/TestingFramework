from models.tdata import TestDataObject
from enum import Enum


# Urls of Artnow.ru web pages
class Url(Enum):
    MainPage = 1
    EmbroideredPaintings = 2
    Batic = 3,
    JewellerArt = 4,
    SearchPage = 5,
    Favorites = 6,
    ShoppingCart = 7,
    Gallery = 8


# Configuration for all tests of Artnow.ru
DATA = TestDataObject(
    urls={
        Url.MainPage: "https://artnow.ru/",
        Url.EmbroideredPaintings: "https://artnow.ru/vyshitye-kartiny-kupit.html",
        Url.Batic: "https://artnow.ru/batik-kartiny-kupit.html",
        Url.JewellerArt: "https://artnow.ru/juvelirnye-izdelija-ruchnoj-raboty.html",
        Url.SearchPage: "https://artnow.ru/ru/searchpage.html",
        Url.Favorites: "https://artnow.ru/ru/favorites.html",
        Url.ShoppingCart: "https://artnow.ru/index.html",
        Url.Gallery: "https://artnow.ru/ru/gallery/"
    },
    use_tests={
        1: True,
        2: True,
        3: True,
        4: True,
        5: True
    },
    variables={
        1: {
            "section": "Вышитые картины",
            "genre": "Городской пейзаж",
            "product_name": "Трамвайный путь"
        },
        2: {
            "section": "Вышитые картины",
            "genre": "Городской пейзаж",
            "product_name": "Трамвайный путь",
            "style": "Реализм"
        },
        3: {
            "section": "Батик"
        },
        4: {
            "search_request": "Жираф"
        },
        5: {
            "section": "Ювелирное искусство"
        }
    })
