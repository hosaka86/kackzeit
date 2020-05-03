kz = input('\n\nHow much time in minutes you spend on the shithole per day?')
alter = int(input('Whats your desired age?'))
kz_jahr_hrs = 365 * int(kz) / 60
kz_jahr_day = kz_jahr_hrs / 24

kz_lifetime_hrs = kz_jahr_hrs * alter
kz_lifetime_day = kz_jahr_day * alter

print(f"Wow! You spend with {kz}/Min Day exactly {kz_jahr_hrs} hours {kz_jahr_day} days on the toilet per year!")
print(f"If you get {alter} years that makes {kz_lifetime_hrs} hours or ~ {round(kz_lifetime_day)} days")
print("Imagine you could have more then one asshole!")
arschl = int(input('How much you\'d like to have?'))
kz_mod_day = kz_lifetime_day - (kz_lifetime_day / arschl)

print(f"Nice! That will save you ~ {round(kz_mod_day)} days on the shithole!!\n\n")

print('''

    (   )
  (   ) (
   ) _   )
    ( \_
  _(_\ \)__
 (____\___))
''')
