#Импорт библиотек и инициализация
from yandex_music import Client
from tqdm import tqdm
import json
import time

client = Client('YANDEX_MUSIC_TOKEN').init()
print("Инициализация пройдена")

#Составляем список из id трека и id исполнителя
print("Собираю информацию о любимых треках...")
number_tracks = len(list(client.users_likes_tracks()))
track = 0
liked_tracks = []
with tqdm(total = number_tracks) as pbar:  
    while True:
        try:
            liked_tracks.append(str(client.users_likes_tracks()[track].id)+":"+str(client.users_likes_tracks()[track].album_id))
            track += 1
            pbar.update(1)
        except:
            break
print("Найдено треков: "+str(len(liked_tracks)))

#Отфильтровываем пользовательские треки
print("Отфильтровываю пользовательские треки...")
filtered_tracks = []
for track in tqdm(liked_tracks):
    if "None" not in track:
        filtered_tracks.append(track)
print(len(filtered_tracks))        
print("Треков после фильтрации: "+str(len(filtered_tracks)))

#Составляем список из полных названий треков (Временно с 1 по счету исполнителем)
print("""Составляю список из "Правильных" названий...""")
number_tracks = len(filtered_tracks)
track_names = []
for track in tqdm(filtered_tracks):
    track_names.append(str(client.tracks([track])[0].artists[0].name)+" "+str(client.tracks([track])[0].title))
        
print('Список треков для экспорта готов')
time.sleep(3)
print(track_names)