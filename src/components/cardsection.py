from flet import Page, Container, Column, Row, Card, Text, Image, ImageFit, IconButton, padding, margin, border_radius
from src.utils.data import menu_kfc

cardmenu = Row()

for i in menu_kfc:
    cardmenu.controls.append(
        Card(
            elevation= 20,
            content= Container(
                bgcolor= "white",
                width= 150,
                height= 260,
                border_radius= border_radius.all(30),
                content= Column([
                    Image(
                        src=i["image"],
                        border_radius= border_radius.all(30),
                        width= 150,
                        height= 110,
                        fit= ImageFit.CONTAIN
                    ),
                    Container(
                        padding= padding.all(10),
                        content= Column(
                            [
                                Text(i["title"], size= 16, weight= "bold"),
                                Text(i["title"], size= 13),
                                Row([
                                    Text(i["price"], size= 23, weight= "bold"),
                                    IconButton(icon= "add")
                                ],
                                alignment= "spaceBetween"
                                )
                            ]
                        )
                    )
                ],alignment= "spaceBetween")
            )
        )
    )

def sectioncard(page: Page):
    return Container(
        padding= padding.only(top= 20),
        bgcolor= "#E3002A",
        content= Column([
            Container(
                content= Text(
                    "In Restaurant",
                    color= "white",
                    size= 30,
                    weight= "bold"
                ),
                margin= margin.only(left= 10)
            ),
            Row(
                [
                    cardmenu
                ],
                scroll= "auto"
            )
        ])
    )