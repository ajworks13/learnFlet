import asyncio
import flet as ft


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


def main(page: ft.Page):
    page.add(Countdown(120), Countdown(60))


ft.app(main)


''''''''''''''''''''''''''''''''''''''


# import flet as ft


# def main(page):

#     page.adaptive = True

#     page.appbar = ft.AppBar(
#         leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
#         title=ft.Text("Adaptive AppBar"),
#         actions=[
#             ft.IconButton(ft.cupertino_icons.ADD,
#                           style=ft.ButtonStyle(padding=0))
#         ],
#         bgcolor=ft.colors.with_opacity(
#             0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
#     )

#     page.navigation_bar = ft.NavigationBar(
#         destinations=[
#             ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
#             ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
#             ft.NavigationDestination(
#                 icon=ft.icons.BOOKMARK_BORDER,
#                 selected_icon=ft.icons.BOOKMARK,
#                 label="Bookmark",
#             ),
#         ],
#         border=ft.Border(
#             top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
#         ),
#     )

#     page.add(
#         ft.SafeArea(
#             ft.Column(
#                 [
#                     ft.Checkbox(value=False, label="Dark Mode"),
#                     ft.Text("First field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Text("Second field:"),
#                     ft.TextField(keyboard_type=ft.KeyboardType.TEXT),
#                     ft.Switch(label="A switch"),
#                     ft.FilledButton(content=ft.Text("Adaptive button")),
#                     ft.Text("Text line 1"),
#                     ft.Text("Text line 2"),
#                     ft.Text("Text line 3"),
#                 ]
#             )
#         )
#     )


# ft.app(target=main)


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
