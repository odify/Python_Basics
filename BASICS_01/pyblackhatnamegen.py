# CHECKOUT YOUR BLACK HAT NAME =)

import random

ms1 = ["SH4D0W","CHIEF","M4STER","NULL","TOXIC","C4PT41N","EVIL","CYBER","0DARK","ICE","FIRE","PRIV4TE","TRO0L","LIQUID","THE","MAD","ZERO"]
ms2 = ["BET4","ANGEL","WIRE","B4RC0DE","BOT","HYDRA","NINJ4","NIGHT","DELT4","W1ZZARD","SHARK","SAINT","VIRUZ","DESTR0YER","X","CR4CK","L3G3ND","OMICR0N","PH4NT0M"]
ms =random.choice(ms1)
mk =random.choice(ms2)
mks = (ms + " " + mk)
i = len(mks)
def decor(func):
    def wrap():
        print("<"*i)
        func()
        print(">"*i)
    return wrap
def username():
    print(mks)
print("Your name is:")
decorator = decor(username)
decorator()


