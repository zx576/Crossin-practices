import json
import re
from collections import Counter
# def unpack():
#     with open('alltracks.txt','r',errors='ignore',encoding='utf-8')as f:
#         all_data = f.read()
#     print(all_data)
#     all_data[300:310]
#     content = re.sub('\'', '\"', all_data)
#     print(content)
#     data = json.loads(content)
#     print(data)
#
# unpack()


# def main():
#     data = unpack()
#
# if __name__ == '__main__':
#     main()

# string = [('a',1),('b',2),('c',3)]
# for i in string:
#     if 1 in i:
#         print(i)
#
l = ['Liekkas', 'Heart of Courage', 'Vishnu - Original', "I'm Yours", 'Croatian Rhapsody', 'Sugar', 'Cyberworld', 'Counting Stars', 'For The Win', 'Memories Of You', 'Coming Home', 'So:Lo', 'Intro - intro', 'The New Earth', 'Photograph', 'Conquest of Paradise', 'Centuries', 'A Little Story', "Hero's Theme", 'Mind Heist', 'Breath and Life', 'Battle Without Honor or Humanity', 'String Tek', 'Purple Passion', 'End Credits', 'Rock House Jail', 'You', 'Oceanside', 'Palladio', "It's Our Fight", 'Immortal', 'Here Comes the King', 'The Mass', 'Viva La Vida', 'El Dorado', 'Becoming a Legend', 'Time', 'Refrain', 'Intro: The Dawn', 'Dragon Rider - Original', 'El Dorado Dubstep (Remix) - remix', 'The truth that you leave', 'I Want My Tears Back', 'Pacific Rim', 'To Glory', 'Epica', 'Go Time', 'Traveling Light', 'Moon Flow', 'Yeah!']
l2 = ['Arrival to Earth', 'Memories Of You', 'Heart of Courage', 'Onward to Freedom', 'To Glory', 'Gotta Have You', 'Somebody That I Used To Know', 'A Little Story', 'Rags To Rings', 'Time Will Tell', 'Cornfield Chase', 'Epica', 'Say Hello', 'Croatian Rhapsody', 'The truth that you leave', 'End Credits', 'November Sky', 'Liekkas', 'I Want My Tears Back', 'Battle Without Honor or Humanity', 'The Mass', 'String Tek', 'Bila', 'In Silent Repose', 'Because of You', 'Uptown Funk', 'Yeah!', 'The Monster (feat. Rihanna)', 'Pacific Rim', 'Dragon Rider - Original', 'Intro - intro', 'Soldiers Arrive', "Hero's Theme", 'Go Time', 'For The Win', "It's My Life", 'Human Legacy', '七剑战歌', 'Palladio', 'Centuries', 'Look At Me Now', 'Inspire', 'Breath and Life', 'The New Earth', 'Intro: The Dawn', 'Fade', 'Cyberworld', 'Best Day Of My Life', 'Counting Stars', 'Flemington', 'Main Title', 'Mind Heist', 'Becoming a Legend', 'The Phoenix', 'Rock House Jail', 'End Of May', 'So:Lo', 'Traveling Light', "It's Our Fight", 'Einaudi: Nuvole Nere', 'Refrain', 'Time', 'Conquest of Paradise', '夜空中最亮的星', 'Sleepyhead', 'Oceanside', 'Prometheus Rising', 'Serenata Immortale', 'New Soul', 'Autobots', '太阳照常升起', "I'm Not the Only One", 'My Songs Know What You Did In The Dark (Light Em Up)', 'Viva La Vida', '往事只能回味', 'Luv Letter', '3 AM', 'All of Me', 'Immortal', 'Hope', 'Here Comes the King', "He's a Pirate", 'Sugar', 'Coming Home', 'El Dorado', "See What I've Become", 'Moon Flow', 'You', 'Vishnu - Original', 'Highscore', "I'm Yours", 'A Faint Memory', 'Purple Passion', 'Requiem For A Tower', 'Photograph', 'Valder Fields', 'Everybody', 'Ringtone (MetroGnome Remix)', 'El Dorado Dubstep (Remix) - remix']
for i in l:
    if i in l2:
        l2.remove(i)
print(len(l2))
for j in l2:
    print(j)
# for i in l:
#     print(i)