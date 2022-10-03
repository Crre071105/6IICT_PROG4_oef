engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

vertaal = []
key_v = list(engels_nederlands.items())
zin = input().split()
for woord in zin:
    for key,value in key_v:
        if woord == value:
            vertaal.append(key)
    vertaal.append(woord)
nederlands_zin = " ".join(vertaal)
print(nederlands_zin)
