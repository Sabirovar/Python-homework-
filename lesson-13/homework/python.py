# 1. Age Calculator
def calculate_age(birthdate):
    today = datetime.today()
    delta = today - birthdate
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    print(f"You are {years} years, {months} months, and {days} days old.")

# 2. Days Until Next Birthday
def days_until_birthday(birthdate):
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    delta = next_birthday - today
    print(f"Days until next birthday: {delta.days}")

# 3. Meeting Scheduler
def meeting_end_time(start_str, duration_h, duration_m):
    start = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
    end = start + timedelta(hours=duration_h, minutes=duration_m)
    print(f"Meeting will end at: {end}")

# 4. Timezone Converter
def convert_timezone(dt_str, from_tz_str, to_tz_str):
    from_zone = pytz.timezone(from_tz_str)
    to_zone = pytz.timezone(to_tz_str)
    dt = from_zone.localize(datetime.strptime(dt_str, "%Y-%m-%d %H:%M"))
    converted = dt.astimezone(to_zone)
    print(f"Converted time: {converted.strftime('%Y-%m-%d %H:%M')} ({to_tz_str})")

# 5. Countdown Timer
def countdown_timer(target_str):
    target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        if now >= target:
            print("Countdown complete!")
            break
        remaining = target - now
        print(f"Time remaining: {remaining}", end='\r')
        time.sleep(1)

# 6. Email Validator
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if re.match(pattern, email):
        print("Valid email.")
    else:
        print("Invalid email.")

# 7. Phone Number Formatter
def format_phone(number):
    digits = re.sub(r"\D", "", number)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print(f"Formatted number: {formatted}")
    else:
        print("Invalid phone number.")

# 8. Password Strength Checker
def check_password_strength(password):
    strength = "Weak"
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Moderate"
    print(f"Password strength: {strength}")

# 9. Word Finder
def find_word_in_text(word, text):
    positions = [m.start() for m in re.finditer(re.escape(word), text, re.IGNORECASE)]
    print(f"Found '{word}' at positions: {positions}")

# 10. Date Extractor
def extract_dates(text):
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    dates = re.findall(pattern, text)
    print(f"Extracted dates: {dates}")
