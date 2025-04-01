import requests


class BugsSearch:
    def __init__(self, target_date):
        self.target_date = target_date

    def get_webpage(self) -> str:
        url = f"https://music.bugs.co.kr/chart/track/day/total?chartdate={self.target_date}"
        webpage = requests.get(url=url).text
        return webpage
