COLOR_CODE_NAME = dict(absolutezero="#0048ba", acidgreen="#b0bf1a", aliceblue="#f0f8ff", amaranth="#e32636",
                    amber="#ffbf00", amethyst="#9966cc", antiqueWhite="#faebd7", antiqueWhite1="#ffefdb", antiqueWhite2="#eedfcc" )

while True:
    color_name=str(input("Enter Color name:")).lower().strip()
    if color_name=="":
        break
    try:
            print(COLOR_CODE_NAME[color_name])
    except KeyError:
        print("Invalid Colour name")


