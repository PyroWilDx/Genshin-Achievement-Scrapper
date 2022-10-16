# Genshin-Achievement-Scrapper

[**Genshin-Achievement-Scrapper**](https://github.com/PyroWilDx/Genshin-Achievement-Scrapper/) is an autonomous tool designed to retrieve a list of all uncompleted achievements in the [Wonders Of The World](https://genshin-impact.fandom.com/wiki/Wonders_of_the_World) and [Memories Of The Heart](https://genshin-impact.fandom.com/wiki/Memories_of_the_Heart) categories of [Genshin Impact 4.4](https://genshin.hoyoverse.com/).

This tool was developed because the game does not provide a way to view incomplete achievements.

## App Set-Up

- To retrieve achievements from [Wonders Of The World](https://genshin-impact.fandom.com/wiki/Wonders_of_the_World), copy the contents of [```res/WondersOfTheWorld.txt```](res/WondersOfTheWorld.txt) into [```res/SrcAchievements.txt```](res/SrcAchievements.txt).

- To retrieve achievements from [Memories Of The Heart](https://genshin-impact.fandom.com/wiki/Memories_of_the_Heart), copy the contents of [```res/MemoriesOfTheHeart.txt```](res/MemoriesOfTheHeart.txt) into [```res/SrcAchievements.txt```](res/SrcAchievements.txt).

## Development Set-Up

<div align="center">

| [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="60"/>](https://www.python.org/) | [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" width="60"/>](https://www.jetbrains.com/pycharm/) | [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/windows8/windows8-original.svg" width="60"/>](https://www.microsoft.com/windows/) |
|---|---|---|

</div>

### How To Use

- Install [Tesseract 5](https://digi.bib.uni-mannheim.de/tesseract/).

- Specify the location where Tesseract is installed by updating line 7 of [```src/Main.py```](src/Main.py).

> [!IMPORTANT]
> If you used the default installation settings for Tesseract, you only need to enter your Windows username when the script runs.

- Install all required Python packages w/ [```Requirements.txt```](./Requirements.txt).

```
pip install -r Requirements.txt
```

- Run [```src/Main.py```](src/Main.py) w/ Python.

> [!IMPORTANT]
> You need to run it as an **Administrator**.

- Click as shown in the picture below.

<img src=".readme/TutoImage.png" width="600">

- The uncompleted achievements will be listed in ```output/NotCompleted.txt```.

---

<div align="center">
  Copyright &#169; 2022 PyroWilDx. All Rights Reserved.
</div>
