from flet import Page, app
from config import config_page
from src.components.appmenu import jumbotron

def main(page: Page):
    config_page(page)
    page.add(jumbotron)

    page.update()

app(target= main)