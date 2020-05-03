kz = input('\n\n\n\nKackzeit in min pro Tag?')
alter = int(input('wie alt willst du werden?'))
kz_jahr_hrs = 365 * int(kz) / 60
kz_jahr_day = kz_jahr_hrs / 24

kz_lifetime_hrs = kz_jahr_hrs * alter
kz_lifetime_day = kz_jahr_day * alter

print(f"Wow! Pro Jahr verbringst du bei {kz}/Min Tag exakt {kz_jahr_hrs} Stunden oder {kz_jahr_day} Tage aufm Pott!")
print(f"Wenn du wirklich {alter} Jahr wirst, entspricht das {kz_lifetime_hrs} Stunden bzw {kz_lifetime_day} Tage")
print("Stell dir vor du könntest dir aussuchen mehr als ein Arschloch zu haben")
arschl = int(input('Wieviel Arschlöcher möchtest du haben?'))
kz_mod_day = kz_lifetime_day - (kz_lifetime_day / arschl)
print(f"Gute Wahl, damit sparst du dir {kz_mod_day} Tage auf dem Pott!\n\n")

print('''

    (   )
  (   ) (
   ) _   )
    ( \_
  _(_\ \)__
 (____\___))
''')
