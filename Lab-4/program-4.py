singers_input = input("Enter names of singers : ").split()
dancers_input = input("Enter names of dancers : ").split()


singers = {singer for singer in singers_input}
dancers = {dancer for dancer in dancers_input}

print(f"Singers: {singers}")
print(f"Dancers: {dancers}")


all_artists = singers | dancers
print(f"All artists: {all_artists}")


allrounders = singers & dancers
print(f"Allrounders: {allrounders}")

dancers_not_singers = dancers - singers
print(f"Dancers but not singers: {dancers_not_singers}")

singers_not_dancers = singers - dancers
print(f"Singers but not dancers: {singers_not_dancers}")

exclusive = dancers ^ singers
print(f"Dancers but not singers cum Singers but not dancers: {exclusive}")