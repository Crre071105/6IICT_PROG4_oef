poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}
nieuwe_dict = {}
for deelnemers in poll_talen:
    if deelnemers in favorite_languages:
            print(f"{deelnemers} Bedankt voor uw deelnamen ")
    else:
            x = input(f"{deelnemers} zou u willen deelnemen ")
            if len(x)>=1:
                nieuwe_dict[deelnemers] = x
favorite_languages.update(nieuwe_dict)
print(favorite_languages)