def __(___, ____):
    _____ = [int(____[_:_+2],10) for _ in range(0,len(____),2)]
    ____ = [___[_] for _ in _____]
    ____ = ''.join(____)
    return ____

def _____(___):
    ____ = []
    for _ in ___:
        ______ = bin(ord(_))[2:].zfill(8)
        ____.append(______)
    return ''.join(____)

def _______(___):
    return ___.replace("0", "O").replace("1", "0")

def ____(___):
    return ___.replace("0", "1").replace("O", "0")

def _________(___):
    ____ = ""
    for _ in range(0, len(___), 8):
        _____ = ___[_:_+8]
        ______ = int(_____, 2)
        _______ = chr(______)
        ____ += _______
    return ____

a = input("\t\t\t\t\tWELCOME TO THE FRIST FLAGCHECKER CHALLENGE!!!!!!!!!!!!!!\n\t\t\t\t\t\t\tPLEASE SUBMIT YOUR FLAG:\n\t\t\t\t\t").ljust(100,'0')
b = "OO00O0O0OO00OOO0OO00OOOOOO00OO0OOO00OO00OO00OOO0OO00OOO0OO00O0OOOO00OOOOOO00O00OOO00OOO0OO000OO0OO00OOO0OO00OOO0OO00OO0OOO00O00OOO00OO0OOO00OO0OOO00OO00OO00O000OO00O0OOOO00OO0OOO00OO00OO00O00OOO00O0OOOO00O0OOOO00OOOOOO000OO0OO00O0OOOO000OOOOO00O0O0OO00O000OO00O0O0OO00OO00OO00O0OOOO00OOO0OO00O00OOO00OO00OO00OOOOOO00OO00OO00O0O0OO00OOOOOO00OOOOOO00OOO0OO00OO00OO000OOOOO00OO0OOO00OOOOOO00O0OOOO00O0O0OO00OO00OO00O0OOOO00OO00OO00OO00OO00OOO0OO000OOOOO00O0O0OO000OO0OO00OOO0OO00OOOOOO00O0O0OO00O0OOOO00OO0OOO00OO00OO00OOO0OO00OO0OOO00O0O0OO00O0O0OO00OOO0OO00O000OO00OOO0OO00OO00OO00OOOOOO00OOOOOO00OOO0OO00O0O0OO00OO0OOO00OOO0OO00O00OOO00OO0OOO00OO0OOO000OOOOO00OOOOOO00O0OOOO00O0O0OO000OOOOO00OO0OOO00O0O0OO00O0O0OO00OO0OOO00OO00OO00OOOOOO00OOO0OO00O00OOO00O0OOOO00O00OOO00O00OOO00OOO0OO00OOOOOO00O0O0OO00OO00OO00OO0OOO00OO0OOO00O000OO00OOOOOO000OOOOO00O0OOOO00OOOOOO00O0OOOO00OO00OO00OO0OOO00O0OOOO00OO00OO000OO0OO00O0OOOO00O000OO00O00OOO00OOOOOO00OO00OO00O0O0OO00O0O0OO00O00OOO00O0OOOO000OO0OO00OOOOOO00O000OO00OO0OOO000OO0"
c = "O0000OO0O0000O00O00O0O00O000O0OOO000OO0OO00OOO00O0O0O00OO00O000OO00O00OOO00OO0OOO00OOO00O0O00000OO00OOO0O000OO00O00O0000O0OOO0O0O000O0O0O00O0OO0O00000O0O0OO0OO0O0O00000OO00OOO0O0OO0OO0O00O0OOOO000O0OOO00O0OO0O0O00000O0O00000O0O00000O00O0OO0O0O00000O00O00OOO00OO0O0O00OO0OOO000OO00O0O00000O0O0O000O0OO0OOOOO00O0OOOO000000O000O0OOO00O00O0O000OO00O0OOO0OOOO00OOOOO00O00O0O00O0OO0O0O00000O000O0OOO0O0OOOOOO00OO00OO0OO000O0O0OO00O00OO00OO000O0O0O0O00000O00OO00OO00OO00OOO00OOO0O0O0O0OOO00O0000O0O0OO0OO00OO0O0O0O00000"

if (_______(_____(__(a,_________(____(b)))))) == c:
    print("\t\t\t\t\t\t\t\tCORRECT!")
else:
    print("\t\t\t\t\t\t\t\tWRONG!")