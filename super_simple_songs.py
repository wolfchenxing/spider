import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time


def songs_data_spider():
    titles = []
    songs = []

    # 爬取标题及链接，并写入数组
    url = 'https://supersimple.com/super-simple-songs/'
    soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
    song_tags = soup.select('ul[class="all-songs"] a[class="thumbLinkAllsongs"]')
    for item in song_tags:
        # 获取每个Song的链接
        url = item.attrs.get('href')
        print(url)
        song_soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
        try:
            # 标题
            title = song_soup.select('h1[class="single-title custom-post-type-title"]')[0].text
            print(title)
            # YouTube链接
            song_url = song_soup.select('div[class="videoWrapper"] iframe')[0].attrs.get('src') \
                .replace('?rel=0&showinfo=0', '')
            print(song_url)
            titles.append(title)
            songs.append(song_url)
        except:
            logging.error('遇到异常，url: {}', url)

    # 输出到excel
    data = {"标题": titles, "链接": songs}
    dataframe = pd.DataFrame(data)
    writer = pd.ExcelWriter('/Users/chenyuting/Desktop/songs.xlsx')
    dataframe.to_excel(writer, index=False)
    writer.save()


def get_all_songs_website():
    url = 'https://supersimple.com/super-simple-songs/'
    soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
    song_tags = soup.select('ul[class="all-songs"] a[class="thumbLinkAllsongs"]')
    for item in song_tags:
        # 获取每个Song的网址
        url = item.attrs.get('href')
        print(url)


def fill_songs_excel(filepath):
    # 读取excel，爬取每个网址下的YouTube链接，并回填到excel中
    df = pd.read_excel(filepath)
    for index, row in df.iterrows():
        time.sleep(10)
        if pd.isna(row['链接']) and row['网址'] != '':
            web_url = row[0]
            song_soup = BeautifulSoup(requests.get(url=web_url, headers=headers).text.encode("utf-8"), 'lxml')
            try:
                # 标题
                title = song_soup.select('h1[class="single-title custom-post-type-title"]')[0].text
                print(title)
                # YouTube链接
                song_url = song_soup.select('div[class="videoWrapper"] iframe')[0].attrs.get('src') \
                    .replace('?rel=0&showinfo=0', '')
                print(song_url)
                # 回填excel
                df.loc[index, '标题'] = title
                df.loc[index, '链接'] = song_url
                df.to_excel(filepath, index=False)
            except:
                logging.error('遇到异常，index: {}', index)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.1 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    get_all_songs_website()
    # file = '/Users/xxx/Desktop/songs.xlsx'
    # fill_songs_excel(file)
