import requests
from bs4 import BeautifulSoup


def main_soup(steam_link):
    responce = requests.get(steam_link).text
    soup = BeautifulSoup(responce, "lxml")
    return soup

def get_hours_past_two_weeks(steam_link):
    recentgame_quicklinks_recentgame_recentplaytime_div = main_soup(steam_link).find("div", class_ = "recentgame_quicklinks recentgame_recentplaytime")
    try:
        hours_past_two_weeks = recentgame_quicklinks_recentgame_recentplaytime_div.find("div").text
    except AttributeError:
        hours_past_two_weeks = "No information"
    return hours_past_two_weeks

def get_avatar_border(steam_link):
    profile_avatar_frame_div = main_soup(steam_link).find("div", class_ = "playerAvatarAutoSizeInner")
    border = profile_avatar_frame_div.find_all("img")[0].get("src")
    return border

def get_avatar(steam_link):
    profile_avatar_frame_div = main_soup(steam_link).find("div", class_ = "playerAvatarAutoSizeInner")
    try:
        avatar = profile_avatar_frame_div.find_all("img")[1].get("src")
    except:
        avatar = profile_avatar_frame_div.find("img").get("src")

    return avatar

def get_last_game(steam_link, return_str = True):
    profile_customization_block_div = main_soup(steam_link).find("div", class_ = "recent_game_content")
    try:
        game_img = profile_customization_block_div.find("img", class_ = "game_capsule").get("src")
        game_name = profile_customization_block_div.find("a", class_ = "whiteLink").text
    except:
        return "No information"
    
    if return_str == True:
        return game_name
    else:
        return game_img

def get_is_online(steam_link, return_what_game_playing = False):
    is_online = main_soup(steam_link).find("div", class_ = "profile_in_game_header").text

    if is_online == "Currently In-Game" and return_what_game_playing == True:
        profile_in_game_name_text = main_soup(steam_link).find("div", class_ = "profile_in_game_name").text.split()
        game_name = ""
        for i in profile_in_game_name_text:
            game_name += i
            game_name += " "
        return game_name[:-1]
    return is_online

def set_level_color(level):
    level = int(level)

    while level >= 100:
        level -= 100

    if level >= 0 and level < 10: return "#757575"
    elif level >= 10 and level < 20: return "#9C2424"
    elif level >= 30 and level < 40: return "#E6D61A"
    elif level >= 40 and level < 50: return "#38802D"
    elif level >= 50 and level < 60: return "#3D7EBE"
    elif level >= 20 and level < 30: return "#C66624"
    elif level >= 60 and level < 70: return "#611B8B"
    elif level >= 70 and level < 80: return "#CD3BDF"
    elif level >= 80 and level < 90: return "#6B1A33"
    elif level >= 80 and level < 90: return "#6B1A33"
    elif level >= 90 and level <= 99: return "#6B1A33"

def set_online_color(steam_link):
    if get_is_online(steam_link) == "Currently Offline":
        online_color = "#78786D"
    elif get_is_online(steam_link) == "Currently Online":
        online_color = "#5C9DC6"
    else:
        online_color = "#65B144"
    return online_color
    
def get_friends_count(steam_link):
    profile_friend_links_profile_count_link_preview_ctn_responsive_groupfriends_element_div = main_soup(steam_link).find("div",
    class_ = "profile_friend_links profile_count_link_preview_ctn responsive_groupfriends_element")
    friends_count = profile_friend_links_profile_count_link_preview_ctn_responsive_groupfriends_element_div.find("span", class_ = "profile_count_link_total").text.split()[0]
    return friends_count

def get_games_count(steam_link):
    profile_item_links_div = main_soup(steam_link).find("div", class_ = "profile_item_links")
    try:
        games_count = profile_item_links_div.find("span", class_ = "profile_count_link_total").text.split()[0]
    except IndexError:
        games_count = "No information"
    return games_count

def get_lvl(steam_link):
    steam_lvl = main_soup(steam_link).find("span", class_ = "friendPlayerLevelNum").text
    return steam_lvl

def get_name(steam_link):
    steam_name = main_soup(steam_link).find("span", class_ = "actual_persona_name").text
    return steam_name
