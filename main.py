from flet import Page, app
from config import config_page
from src.components.appmenu import app_bar
from src.components.cardsection import sectioncard
from src.components.tabsmenu import tabs_menu

def main(page: Page):
    config_page(page)
    page.add(
        app_bar(page),
        sectioncard(page),
        tabs_menu(page)
    )

    page.update()

app(target= main)