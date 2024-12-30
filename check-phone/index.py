import re

def is_valid_vietnam_phone_number(phone_number):
    # Regex pattern to match Vietnam phone numbers
    pattern = re.compile(r'^(?:\+84\d{9}|0\d{9})$')
    return pattern.match(phone_number) is not None

# Example usage
phone_number = input("Nhập SDT cần kiểm tra: ")
if is_valid_vietnam_phone_number(phone_number):
    print("Đây là số điện thoại VN.")
else:
    print("Đây không phải số điện thoại VN.")