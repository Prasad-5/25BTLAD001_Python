import random, string, time
 
CHARS = {"1": string.digits,
         "2": string.ascii_uppercase + string.digits,
         "3": string.ascii_letters + string.digits + "!@#$%&*"}
EXPIRY, MAX_TRIES = 60, 3
store = {}   # user -> [otp, time_generated, tries_left, length, type]
 
def log(msg):
    with open("otp_log.txt", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
 
def new_otp(user, length, kind):
    otp = "".join(random.choice(CHARS[kind]) for _ in range(length))
    store[user] = [otp, time.time(), MAX_TRIES, length, kind]
    log(f"OTP generated for {user}: {otp}")
    return otp
 
while True:
    print("\n===== OTP GENERATOR =====")
    ch = input("1.Generate 2.Verify 3.Resend 4.Time left 5.Log 6.Exit: ")
    if ch == "6":
        break
    if ch in ("1", "2", "3", "4"):
        user = input("User ID / email: ").strip()
        rec = store.get(user)
 
    if ch == "1":
        n = input("OTP length (default 6): ")
        kind = input("Type 1.Numeric 2.Alphanumeric 3.Strong: ")
        otp = new_otp(user, int(n) if n.isdigit() else 6,
                      kind if kind in CHARS else "1")
        print(f"OTP: {otp}  (valid for {EXPIRY} seconds)")
    elif ch in ("2", "3", "4") and not rec:
        print("No OTP found for this user.")
    elif ch == "2":
        code = input("Enter OTP: ").strip()
        if time.time() - rec[1] > EXPIRY:
            del store[user]
            print("OTP expired. Request a new one.")
        elif code == rec[0]:
            del store[user]
            log(f"OTP verified for {user}")
            print("OTP verified successfully!")
        else:
            rec[2] -= 1
            log(f"Wrong OTP for {user}, {rec[2]} tries left")
            if rec[2] == 0:
                del store[user]
                print("Too many wrong attempts. OTP invalidated.")
            else:
                print(f"Incorrect OTP. {rec[2]} attempt(s) left.")
    elif ch == "3":
        print("New OTP:", new_otp(user, rec[3], rec[4]))
    elif ch == "4":
        left = round(EXPIRY - (time.time() - rec[1]))
        print(f"{max(0, left)} second(s) left")
    elif ch == "5":
        try:
            print(open("otp_log.txt").read())
        except FileNotFoundError:
            print("No log yet.")
    else:
        print("Invalid choice.")
