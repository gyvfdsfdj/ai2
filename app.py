from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming 台灣ID)
def validate_id_number(id_number):
    # 1. 確認身份證號碼長度是否為10。
    if len(id_number) != 10:
        return "身分證號碼應該為10碼", 400
    
    # 2. 確認第一個字元是否為英文字母
    if not id_number[0].isalpha():
        return "第一個字元應該為英文字母", 400
        
    # 3. 確認後九個字元是否為數字
    if not id_number[1:].isdigit():
        return "身分證號碼後九碼應為數字", 400
    
    # 4. 將第一個英文字母轉換為對應的數字（A為10，B為11，C為12，...，Z為33）
    first_letter_value = ord(id_number[0].upper()) - ord('A') + 10
    # 5. 將轉換後的兩位數字分別乘以1和9。
    checksum = first_letter_value // 10 * 1 + first_letter_value % 10 * 9
    
    # 6. 將第二個到第九個數字分別乘以8, 7, 6, 5, 4, 3, 2, 1。
    weights = [8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, 9):
        checksum += int(id_number[i]) * weights[i - 1]
    
    # 7. 將以上所有乘積相加，並加上最後一個數字。
    checksum += int(id_number[-1])
    
    # 8. 如果最後的結果可以被10整除，則這個身份證號碼就是正確的。
    if checksum % 10 == 0:
        return None, 200
    else:
        return "身份證號碼驗證失敗", 400

# 測試
id_number = "A123456789"
error_message, status_code = validate_id_number(id_number)
if error_message:
    print(error_message)
else:
    print("身分證號碼驗證通過！")

   
    
    
    
    
    # Validate name (assuming it's alphabetic)                  
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "第一個字元應該為英文字母碼", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "身份證號碼應該為10碼", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80

