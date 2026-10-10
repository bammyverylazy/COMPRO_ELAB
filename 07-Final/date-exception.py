months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    user = input("Date: ")
    use = user.split()
    try:
        if use and use[0] in months:
            user = user.replace(",", "").split()
            month = months.index(user[0]) + 1
            year = int(user[2])
            day = int(user[1])
        else:
            user = user.split("/")
            month = int(user[0])
            year = int(user[2])
            day = int(user[1])
        if 0 > month or month >13  or day < 0 or day >31:
          raise ValueError
        else:
          print(f"{year}-{month:02}-{day:02}")
          break
    except (ValueError, IndexError):
        continue
