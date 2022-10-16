from Normalize import *
import Scrap

SRC_ACHIEVEMENTS_PATH = "..\\res\\SrcAchievements.txt"
ALL_ACHIEVEMENTS_PATH = "..\\res\\AllAchievements.txt"
NOT_COMPLETED_ACHIEVEMENTS_PATH = "..\\output\\NotCompleted.txt"
ALL_TEXT_PATH = "..\\output\\AllText.txt"


def getAchievementsTitleOnly(text):
    titles = ""
    is_title = True
    for i in range(0, len(text)):
        if is_title is True:
            titles += text[i]
        if text[i] == "\n" and text[i - 1] == "\n":
            if is_title is True:
                is_title = False
            else:
                is_title = True
        elif text[i] == "\n":
            if i + 1 != len(text) and text[i + 1] == "\n":
                continue
            else:
                if is_title is True:
                    is_title = False

    return normalizeString(titles)


def convertSrcAchievements():
    string = ""
    with open(SRC_ACHIEVEMENTS_PATH, encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        st = line.replace(" (view source)", "")
        st = st.replace(" (Achievement)", "")
        st = st.replace(" (Wonders of the World)", "")
        st = st.replace(" (Memories of the Heart)", "")
        st = st.split("	")
        st = st[0] + "\n"
        if "/Change History" in line:
            continue
        if "(Tier " in line:
            index = line.find("(Tier ")
            if line[index + 6] == "1":
                string += (st[:index - 1] + "\n")
        else:
            string += st

    with open(ALL_ACHIEVEMENTS_PATH, "w+", encoding="utf-8") as file:
        file.write(string)


def getNotCompletedAchievements(path):
    with open(ALL_ACHIEVEMENTS_PATH, encoding="utf-8") as file:
        all_achievements = file.readlines()
    with open(path, encoding="utf-8") as file:
        achievements = file.readlines()

    not_completed_achievements = ""
    for a_achievement in all_achievements:
        exist = False
        for y_achievements in achievements:
            if similar(a_achievement, y_achievements) > 0.88:
                exist = True
                break
        if exist is False:
            not_completed_achievements += a_achievement

    with open(NOT_COMPLETED_ACHIEVEMENTS_PATH, "w+", encoding="utf-8") as file:
        file.write(not_completed_achievements)


def getNotCompletedAchievementsV2(path):
    with open(ALL_ACHIEVEMENTS_PATH, encoding="utf-8") as file:
        all_achievements = file.readlines()
    with open(path, encoding="utf-8") as file:
        achievements = file.readlines()

    with open(ALL_TEXT_PATH, 'w'):
        pass

    not_completed_achievements = ""
    last_line = ""
    failed_scrap = ""
    for a_line in all_achievements:
        exist = False
        for y_line in achievements:
            if similar(a_line, y_line) > 0.88 or similar(a_line, last_line + y_line) > 0.88:
                exist = True
                break
            last_line = y_line
        if exist is False:
            not_completed_achievements += a_line

            print(f"Scrapping {a_line}")
            with open(ALL_TEXT_PATH, "a", encoding="utf-8") as file:
                file.write(a_line)
                file.write("\n")
                url = a_line.replace("\n", "")
                url = url.replace(" ", "_")
                url = url.replace("?", "%3F")
                url = url.replace("'", "%27")
                url = "https://genshin-impact.fandom.com/wiki/" + url
                txt = Scrap.getAllTextWeb(url)
                if txt is None:
                    print("\n\n=========================")
                    print(f"Failed To Scrap {a_line}")
                    print("=========================\n\n")
                    failed_scrap += a_line + "\n"
                else:
                    file.write(txt)
                file.write("\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n")
                file.write("=================================\n\n\n\n")

    with open(NOT_COMPLETED_ACHIEVEMENTS_PATH, "w+", encoding="utf-8") as file:
        file.write(not_completed_achievements)

    if failed_scrap == "":
        print("Failed Scrap : None")
    else:
        print("Failed Scrap :\n")
        print(failed_scrap)
