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
        input_field.value = ""

    def navigate_to_page2(e):
        page.go("page2")
        
    def page2_view():
        steam_link = input_field.value

        user_avatar = ft.Stack(
            controls=[
            ft.Container(content=ft.Image(src=get_avatar(steam_link), width=230, height=230), width=230, height=230),
            ft.Container(content=ft.Image(src=get_avatar_border(steam_link), width=230, height=230), width=230, height=230)
        ])
        
        user_name = ft.Text(
            value=get_name(steam_link),
            size = 40,
        )

        user_level_text = ft.Text(
            value =  "Level",
            size = 30
        )

        user_level = ft.Text(
            value=  get_lvl(steam_link),
            size = 30,
            color = set_level_color(get_lvl(steam_link))
        )
        
        if get_is_online(steam_link) == "Currently Offline":
            online_color = "#78786D"
        elif get_is_online(steam_link) == "Currently Online":
             online_color = "#5C9DC6"
        else:
            online_color = "#65B144"
            
        user_online_status = ft.Text(
            value = get_is_online(steam_link),
            size = 30,
            color = online_color
        )

        online_status_list = [user_online_status]
        if get_is_online(steam_link) == "Currently In-Game":
            user_ingame_status = ft.Text(
                value= get_is_online(steam_link, return_what_game_playing=True),
                size= 30,
                color = online_color
            )
            online_status_list.append(user_ingame_status)


        online_status_column = ft.Column(
            controls=online_status_list
        )

        level_row = ft.Row(
            controls=[user_level_text, user_level]
        )

        c0 = ft.Container(
            content = user_avatar
        )

        c1 = ft.Container(
            content = user_name,
            padding = ft.Padding(left = 15, right= 0, top = 120, bottom= 0)
        )

        c2 = ft.Container(
            content=level_row,
            padding= ft.Padding(left = 0, right = 5, top = 105, bottom = 40)
        )

        c_online = ft.Container(
            content=online_status_column,
            padding = ft.Padding(left = 0, right= 0, top = 0, bottom= 165),
        )

        username_row = ft.Row(
        controls = [c0, c1, c2, c_online],
        alignment = ft.MainAxisAlignment.START,
        vertical_alignment = ft.CrossAxisAlignment.CENTER
        )
        #--------------------------------------------------------------------

        hours_past_two_weeks = get_hours_past_two_weeks(steam_link)
        if hours_past_two_weeks != "No information":
            hours_past_two_weeks += " hours past 2 weeks "
        
        past_two_weeks_text = ft.Text(
            value=hours_past_two_weeks,
            size = 30
        )

        last_game_text = ft.Text(
            value= "Last game played:",
            size = 20
        )

        last_game_name = ft.Text(
            value=get_last_game(steam_link, return_str = True),
            size = 35
        )

        if get_last_game(steam_link) != "No information":
            last_game_img = ft.Image(
                src = get_last_game(steam_link, return_str=False),
                width=276,
                height=103,
                fit=ft.ImageFit.CONTAIN
            )

            c6 = ft.Container(
            content=last_game_img,
            padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
            )

        c3 = ft.Container(
            content=past_two_weeks_text,
            padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
        )

        c4 = ft.Container(
            content=last_game_text,
            padding= ft.Padding(left = 20, right = 0, top = 0, bottom = 0)
        )

        c5 = ft.Container(
            content=last_game_name,
            padding= ft.Padding(left = 20, right = 0, top = 25, bottom = 0)
        )


        gamestats_column_list = [c3, c4, c5]
        if get_last_game(steam_link, return_str=False) != "No information":
            gamestats_column_list.append(c6)

        gamestats_column = ft.Column(
            controls=gamestats_column_list,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        #--------------------------------------------------------------------

        friends_count_text = ft.Text(
            value=f"Friends count: {get_friends_count(steam_link)}",
            size = 35
        )

        games_count_text = ft.Text(
            value=f"Games count: {get_games_count(steam_link)}",
            size = 35
        )

        back_button = ft.CupertinoButton(
            text = "Back",
            color = "black",
            bgcolor= "#A9A9A9",
            on_click= navigate_to_page1,
            width= 250,
            height=50,
        )


        c7 = ft.Container(
            content=friends_count_text,
            padding= ft.Padding(left = 50, right = 0, top = 0, bottom = 0)
        )

        c8 = ft.Container(
            content=games_count_text,
            padding= ft.Padding(left = 50, right = 0, top = 0, bottom = 0)
        )

        c9 = ft.Container(
            content=back_button,
            padding= ft.Padding(left = 100, right = 0, top = 250, bottom = 0)
        )


        accountstats_column = ft.Column(
            controls= [c7, c8],
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START    
        )

        bottom_row = ft.Row(
            controls=[gamestats_column, accountstats_column, c9]
        )

        main_column = ft.Column(
            controls=[username_row, bottom_row]
        )


        return ft.View("page2",
        [
        ft.Container(
        content = main_column,
        alignment=ft.alignment.center,
        padding = 20)
        ])
    
    def page1_view():
        return ft.View("page1",
        [
        ft.Container(
        content=column,
        alignment=ft.alignment.center)
        ])
    

    main_text = ft.Text(
        value= "Enter your steam link",
        size = 45
    )

    input_field = ft.TextField(
        width = 600,
        height = 50,
        bgcolor="white",
        color = "black"
    )

    start_button = ft.CupertinoButton(
        text = "Press to start",
        color = "black",
        bgcolor= "white",
        min_size=60,
        alignment=ft.alignment.center,
        on_click= navigate_to_page2,
    )


    c1 = ft.Container(
        content=main_text,
        padding= ft.Padding(left = 0, right = 0, top = 50, bottom = 0)
    )

    c2 = ft.Container(
        content=input_field,
        padding= ft.Padding(left = 0, right = 0, top = 170, bottom = 0)
    )

    c3 = ft.Container(
        content=start_button,
        padding= ft.Padding(left = 0, right = 0, top = 0, bottom = 0)
    )

    column = ft.Column(
        controls=[c1, c2, c3],
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    #--------------------------------------------------------------------
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