def printlyrics():
    import time

    lyrics = [
        "Haa maane sambh-sambh rakhte tere jhanjhara ke jode",
        "Meri gali ro-ro ye bhi chhori bawle se hore",
        "Manne aave jaave khyaal tere khaye jaave khyaal tere",
        "Jeene koni deti haye bairi tanhayi manne",
        "Geeta mein gayi kade chhaati ke lagayi manne",
        "Jad bhi gaya re teri yaad khadi payi manne",
        "Sambh sambh rakhi bahut chhaati ke lagayi manne",
        "Jad bhi gaya re teri yaad khadi payi manne"
    ]

    for line in lyrics:
        print(line)
        time.sleep(1)   # 1 second delay

printlyrics()