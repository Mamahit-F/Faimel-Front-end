import collections

data_umum = {'Nama': 'faimel', 'alamat': 'mapanget', 'timggi': '164 cm', 'Umur': '18', 'Kota': 'Manado'}

data_khusus = {'Kegiatan': 'Mahasiswa', 'jumlah_matkul': '9', 'Hobi': 'main game', 'berkuliah di': 'Unklab', 'fakultas': 'Ilmu komputer'}

res = collections.ChainMap(data_khusus, data_umum)

print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
    print()

# Find a specific value in the result
print('Nama in res: {}'.format(('kegiatan' in res)))
print('Kota in res: {}'.format(('jumlah_matkul' in res)))