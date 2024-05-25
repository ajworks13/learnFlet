import flet as ft

# use this class to use the button anywhere in your app.


class MyButton(ft.ElevatedButton):

    def __init__(self, text, on_click):
        super().__init__()
        self.bgcolor = ft.colors.ORANGE_300
        self.color = ft.colors.GREEN_800
        self.text = text
        self.on_click = on_click


def main(page: ft.Page):

    def ok_clicked(e):
        print("OK clicked")

    def cancel_clicked(e):
        print("Cancel clicked")

    # def button_clicked(e):
    #     output_text.value = f"Dropdown value is:  {color_dropdown.value}"
    #     page.update()

    page.add(
        MyButton(text="OK", on_click=ok_clicked),
        MyButton(text="Cancel", on_click=cancel_clicked),
        MyButton(text="Whoa"),
    )

    # output_text = ft.Text()
    # submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    # color_dropdown = ft.Dropdown(
    #     width=100,
    #     options=[
    #         ft.dropdown.Option("Red"),
    #         ft.dropdown.Option("Green"),
    #         ft.dropdown.Option("Blue"),
    #         ft.dropdown.Option("123"),
    #         ft.dropdown.Option("fefew"),
    #         ft.dropdown.Option("Greeeeeeeeeeeeeeen"),
    #         ft.dropdown.Option("rrè"),
    #         ft.dropdown.Option("vć"),
    #         ft.dropdown.Option("Blue"),
    #     ],
    # )
    # page.add(color_dropdown, submit_btn, output_text)


ft.app(target=main)
