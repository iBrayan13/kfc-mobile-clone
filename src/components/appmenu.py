from flet import colors, AppBar, Row, Container, Text, Image, padding, border, border_radius

jumbotron = AppBar(
    toolbar_height= 90,
    bgcolor= "#E3002A",
    title= Row(
        [
            Container(
                padding= padding.all(4),
                border= border.all(3, "white"),
                border_radius= border_radius.all(30),
                content= Text(
                    "Location",
                    color= "white",
                    size= 15
                ),
            ),
            Container(
                content= Image(
                    src="https://raw.githubusercontent.com/bobwatcherx/fletKFCDesign/master/assets/image/kfc.png",
                    width= 100,
                    height= 70
                )
            )
        ],
        alignment= "spaceBetween"
    )
)