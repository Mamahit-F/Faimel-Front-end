def hitung_rata_rata(data):
    total = sum(data)
    rata_rata = total / len(data)
    return rata_rata

def input_array():
    input_str = input("Masukkan nilai untuk array (pisahkan dengan spasi): ")
    return list(map(int, input_str.split()))

def input_dict():
    input_str = input("Masukkan nilai untuk dictionary (pisahkan key dan value dengan spasi, dan setiap pasangan dengan koma): ")
    data_dict = dict((x.strip(), int(y.strip())) for x, y in (item.split() for item in input_str.split(',')))
    return list(data_dict.values())

def input_list():
    input_str = input("Masukkan nilai untuk list (pisahkan dengan spasi): ")
    return list(map(int, input_str.split()))

def input_recursive():
    n = int(input("Masukkan jumlah nilai: "))
    if n == 0:
        return []
    else:
        value = int(input("Masukkan nilai: "))
        return [value] + input_recursive()

def input_sorting():
    input_str = input("Masukkan nilai untuk sorting (pisahkan dengan spasi): ")
    return sorted(map(int, input_str.split()))

def main():
    data_array = input_array()
    data_dict = input_dict()
    data_list = input_list()
    data_recursive = input_recursive()
    data_sorting = input_sorting()

    rata_rata_array = hitung_rata_rata(data_array)
    rata_rata_dict = hitung_rata_rata(data_dict)
    rata_rata_list = hitung_rata_rata(data_list)
    rata_rata_recursive = hitung_rata_rata(data_recursive)
    rata_rata_sorting = hitung_rata_rata(data_sorting)

    print("Rata-rata dari semua input:", (rata_rata_array + rata_rata_dict + rata_rata_list + rata_rata_recursive + rata_rata_sorting) / 5)

if __name__ == "__main__":
    main()