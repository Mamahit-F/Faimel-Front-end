import re

# Input text
text = "Hallo students, email berikut (semmy@gmail.com, jian@yahoo.com, budi@start.com, tommy23@unklab.co.id) adalah student yang belum tuntas class ini. Diharapkan agar dapat memasukan tugas pada 22 Juni 2024, jam 2 PM. Thank you :)"

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
date_pattern = r'\b(?:\d{1,2}\s)?(?:Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\s\d{4}\b'
time_pattern = r'\b\d{1,2}\s?(?:AM|PM)\b'

emails = re.findall(email_pattern, text)

dates = re.findall(date_pattern, text)

times = re.findall(time_pattern, text)

print("Output:")
print(",\n".join(emails) + ",")
print(",\n".join(dates) + ",")
print(",\n".join(times))
