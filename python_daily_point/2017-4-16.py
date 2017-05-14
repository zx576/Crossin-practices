import base64

string = 'upC1pkfV-rv*ZXMXUf6g2wZAm3leKpyr8News9KIyOddbd1b380rMD8dxyfIKFtdjKoRoBGqE84ylqCvcibilV0U5-1hRgyvWi7qnIu2-qGpJI2A3irc2ebdEpHV11Iw2sO95boUA4Nb9pRBdHnO6-ePrdSAtD5HXBd9BQuul-A='



af = base64.decodebytes(string.encode('utf-8'))

print(af)
