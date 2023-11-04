from flet import Page, Tabs, Tab, Column, Row, Container, Image, Text, Icon, padding, border, border_radius
from src.utils.data import data_burger, data_twister, data_drinks

burguer_list = Column(scroll= "auto")
twister_list = Column(scroll= "auto")
drinks_list = Column(scroll="auto")

for i in data_burger:
    burguer_list.controls.append(
        Row([
            Image(
                src= i["images"],
                width= 110,
                height= 80
            ),
            Container(
                Column([
                    Text(i["title"], size= 16, weight= "bold"),
                    Row([
                        Container(
                            padding= padding.all(10),
                            border= border.all(3, "red"),
                            border_radius= border_radius.all(30),
                            content= Text(f" + {i['price']}")
                        ),
                        Column([
                            Text(i["weight"], size= 13, color= "gray", weight= "bold"),
                            Row(
                                [
                                    Icon(name= "favorite", color= "gray"),
                                    Text(f"{i['like']} fav", size= 15)
                                ],
                                alignment= "start"
                            )
                        ])
                    ])
                ])
            )
        ])
    )

for i in data_twister:
    twister_list.controls.append(
        Row([
            Image(
                src= i["images"],
                width= 110,
                height= 80
            ),
            Container(
                Column([
                    Text(i["title"], size= 16, weight= "bold"),
                    Row([
                        Container(
                            padding= padding.all(10),
                            border= border.all(3, "red"),
                            border_radius= border_radius.all(30),
                            content= Text(f" + {i['price']}")
                        ),
                        Column([
                            Text(i["weight"], size= 13, color= "gray", weight= "bold"),
                            Row(
                                [
                                    Icon(name= "favorite", color= "gray"),
                                    Text(f"{i['like']} fav", size= 15)
                                ],
                                alignment= "start"
                            )
                        ])
                    ])
                ])
            )
        ])
    )

for i in data_drinks:
    drinks_list.controls.append(
        Row([
            Image(
                src= i["images"],
                width= 110,
                height= 80
            ),
            Container(
                Column([
                    Text(i["title"], size= 16, weight= "bold"),
                    Row([
                        Container(
                            padding= padding.all(10),
                            border= border.all(3, "red"),
                            border_radius= border_radius.all(30),
                            content= Text(f" + {i['price']}")
                        ),
                        Column([
                            Text(i["weight"], size= 13, color= "gray", weight= "bold"),
                            Row(
                                [
                                    Icon(name= "favorite", color= "gray"),
                                    Text(f"{i['like']} fav", size= 15)
                                ],
                                alignment= "start"
                            )
                        ])
                    ])
                ])
            )
        ])
    )

menu = Tabs(
    selected_index= 0,
    animation_duration= 300,
    tabs= [
        Tab(
            text= "Burguers",
            content= burguer_list
        ),
        Tab(
            text= "Twisters",
            content= twister_list
        ),
        Tab(
            text= "Drinks",
            content= drinks_list
        )
    ]
)

def tabs_menu(page: Page):
    return Container(
        border_radius= border_radius.only(top_left= 30, top_right= 30),
        width= page.window_width,
        expand= True,
        bgcolor= "white",
        content= menu
    )