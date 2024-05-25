
import flet as ft


def main(page):

    page.adaptive = True

    page.appbar = ft.AppBar(
        leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
        title=ft.Text("Adaptive AppBar"),
        actions=[
            ft.IconButton(ft.cupertino_icons.ADD,
                          style=ft.ButtonStyle(padding=0))
        ],
        bgcolor=ft.colors.with_opacity(
            0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Bookmark",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Checkbox(value=False, label="Dark Mode"),
                    ft.Text("First field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Text("Second field:"),
                    ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
                    ft.Switch(label="A switch"),
                    ft.FilledButton(content=ft.Text("Adaptive button")),
                    ft.Text("Text line 1"),
                    ft.Text("Text line 2"),
                    ft.Text("Text line 3"),
                ]
            )
        )
    )


ft.app(target=main)


''''''''''''''''''''''''''''''''''''''''''''


# import flet as ft

# # use this class to use the button anywhere in your app.


# class MyButton(ft.ElevatedButton):

#     def __init__(self, text, on_click):
#         super().__init__()
#         self.bgcolor = ft.colors.ORANGE_300
#         self.color = ft.colors.GREEN_800
#         self.text = text
#         self.on_click = on_click


# def main(page: ft.Page):

#     def ok_clicked(e):
#         print("OK clicked")

#     def cancel_clicked(e):
#         print("Cancel clicked")

#     # def button_clicked(e):
#     #     output_text.value = f"Dropdown value is:  {color_dropdown.value}"
#     #     page.update()

#     page.add(
#         MyButton(text="OK", on_click=ok_clicked),
#         MyButton(text="Cancel", on_click=cancel_clicked),
#         MyButton(text="Whoa"),
#     )

#     # output_text = ft.Text()
#     # submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
#     # color_dropdown = ft.Dropdown(
#     #     width=100,
#     #     options=[
#     #         ft.dropdown.Option("Red"),
#     #         ft.dropdown.Option("Green"),
#     #         ft.dropdown.Option("Blue"),
#     #         ft.dropdown.Option("123"),
#     #         ft.dropdown.Option("fefew"),
#     #         ft.dropdown.Option("Greeeeeeeeeeeeeeen"),
#     #         ft.dropdown.Option("rrè"),
#     #         ft.dropdown.Option("vć"),
#     #         ft.dropdown.Option("Blue"),
#     #     ],
#     # )
#     # page.add(color_dropdown, submit_btn, output_text)


# ft.app(target=main)
