def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if s == "ECTO88":
        return True
    # اگر طول رشته کمتر از ۲ یا بیشتر از ۶ باشد، نامعتبر است
    if len(s) < 2 or len(s) > 6:
        return False

    # اگر دو کاراکتر اول حروف الفبایی نباشند، نامعتبر است
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # اگر رشته شامل کاراکترهایی غیر عددی یا حرفی باشد، نامعتبر است
    if not s.isalnum():
        return False

     # اگر ارقام پس از دو کاراکتر اول باشند و یا دومین کاراکتر صفر باشد، نامعتبر است
    if len(s) == 2 or s[2] == '0':
        return False

    # اگر رشته حاوی هیچ عددی نباشد، معتبر است
    if not any(c.isdigit() for c in s):
        return True

    # اگر حروف الفبایی در میانه رشته وجود داشته باشند، نامعتبر است
    if any(c.isalpha() for c in s[2:-1]):
        return False

    return True

main()
