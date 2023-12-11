from user_info import user_info

email = input("Masukkan Email: ")

for i,y in user_info.items():
  if email == i:
    print(f"Password anda adalah: {y}")