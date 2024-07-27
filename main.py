import flet as ft
from parsing import *

def main(page: ft.Page):
    page.title = "Your steam stats"
    page.window.width = 1100
    page.window.height = 700
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def navigate_to_page1(e):
        page.go("page1")
        InputField.value = ""

    def navigate_to_page2(e):
        page.go("page2")
        
    def page1_view():
        return ft.View(
            "page1", [
                ft.Container(
                    content=MainColumn,
                    alignment=ft.alignment.center
                )
            ]
        )
    
    def page2_view():
        steam_link = InputField.value
        
        #Set online status
        online_status_list = [
            ft.Text(
                value = get_is_online(steam_link),
                size = 30,
                color = set_online_color(steam_link)
            )
        ]

        if get_is_online(steam_link) == "Currently In-Game":
            online_status_list.append(
                ft.Text(
                    value = get_is_online(steam_link, return_what_game_playing=True), 
                    size= 30,
                    color = set_online_color(steam_link)
                )
            )


        Avatar = ft.Container(
            content = ft.Stack(
                controls=[
                    #Avatar
                    ft.Container(
                        content=ft.Image(
                            src=get_avatar(steam_link),
                            width=230,
                            height=230
                        ),
                    ),

                    #Avatars border
                    ft.Container(
                        content=ft.Image(
                            src=get_avatar_border(steam_link),
                            width=230,
                            height=230
                        ),
                    )
                ]
            )
        ) 

        UserName = ft.Container(
            content = ft.Text(
                value = get_name(steam_link),
                size = 40
            ),
            padding = ft.Padding(left = 15, right= 0, top = 120, bottom= 0)
        ) 
            
        LevelRow = ft.Row(
            controls=[
                #Level text
                ft.Container(
                    content=ft.Text(
                        value =  "Level",
                        size = 30
                    ), 
                    padding= ft.Padding(left = 0, right = 5, top = 105, bottom = 40)
                ), 

                #Level value
                ft.Text(
                    value =  get_lvl(steam_link),
                    size = 30,
                    color = set_level_color(get_lvl(steam_link))
                )
            ]
        )

        OnlineStatus = ft.Container(
            content=ft.Column(
                controls = online_status_list
            ),
            padding = ft.Padding(left = 0, right= 0, top = 0, bottom= 165),
        )
        
        UserRow = ft.Row(
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls =[Avatar, UserName, LevelRow, OnlineStatus]
        )


        HoursPastText = ft.Container(
            content = ft.Text(
                value=get_hours_past_two_weeks(steam_link),
                size = 30
            ),
            padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
        )

        LastGameText = ft.Container(
            content = ft.Text(
                value= "Last game played:",
                size = 20
            ),
            padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
        )

        LastGameName = ft.Container(
            content=ft.Text(
                value=get_last_game(steam_link, return_str = True),
                size = 35
            ),
            padding= ft.Padding(left = 20, right = 0, top = 25, bottom = 0)
        )


        GameStatsColumnList = [HoursPastText, LastGameText, LastGameName]
        if get_last_game(steam_link, return_str=False) != "No information":
            GameStatsColumnList.append(
                ft.Container(
                    content = ft.Image(
                        src = get_last_game(steam_link, return_str=False),
                        width=276,
                        height=103,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
                )
            )

        GameStatsColumn = ft.Column(
            controls=GameStatsColumnList,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        
        FriendsCountText = ft.Container(
            content=ft.Text(
                value=f"Friends count: {get_friends_count(steam_link)}",
                size = 35
            ),
            padding= ft.Padding(left = 50, right = 0, top = 0, bottom = 0)
        )

        GamesCountText = ft.Container(
            content=ft.Text(
                value=f"Games count: {get_games_count(steam_link)}",
                size = 35
            ),
            padding= ft.Padding(left = 50, right = 0, top = 0, bottom = 0)
        )

        BackButton = ft.Container(
            content=ft.CupertinoButton(
            text = "Back",
            color = "black",
            bgcolor= "#A9A9A9",
            on_click= navigate_to_page1,
            width= 200,
            height=50,
            ),
            padding= ft.Padding(left = 0, right = 0, top = 250, bottom = 0),
        )

        AccountStatsColumn = ft.Column(
            controls= [FriendsCountText, GamesCountText],
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START    
        )

        BottomRow = ft.Row(
            controls=[GameStatsColumn, AccountStatsColumn, BackButton]
        )

        MainColumn = ft.Column(
            controls=[UserRow , BottomRow]
        )

        return ft.View("page2",
        [
            ft.Container(
                content = MainColumn,
                alignment=ft.alignment.center,
                padding = 20
            )
        ])
    

    


   


    MainText = ft.Container(
        content = ft.Text(
            value= "Enter your steam link",
            size = 45
        ),
        padding= ft.Padding(left = 0, right = 0, top = 50, bottom = 0)
    )

    InputField = ft.TextField(
            width = 600,
            height = 50,
            bgcolor="white",
            color = "black"
    )
    
    InputFieldContainer = ft.Container(
        content = InputField,
        padding= ft.Padding(left = 0, right = 0, top = 170, bottom = 0)
    )

    StartButton = ft.Container(
        content = ft.CupertinoButton(
            text = "Press to start",
            color = "black",
            bgcolor = "white",
            min_size = 60,
            alignment = ft.alignment.center,
            on_click = navigate_to_page2,
        ),
        padding= ft.Padding(left = 0, right = 0, top = 0, bottom = 0)
    )

    MainColumn = ft.Column(
        controls=[MainText, InputFieldContainer, StartButton],
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    def route_change(route):
        page.views.clear()
        if page.route == 'page2':
            page.views.append(page2_view())
        else:
            page.views.append(page1_view())
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)