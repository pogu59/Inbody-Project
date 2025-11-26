import tkinter as tk #창 구성
from tkinter import ttk #콤보 박스
from tkinter import messagebox as msgbox #경고창

root = tk.Tk()
root.geometry('700x500')
root.title("인바디 시뮬레이터")
root.config(bg="#e3f2fd")
font = ("맑은고딕", 11)

title_label = tk.Label(root, text="인바디 검사!", font=('맑은 고딕', 22, "bold"), bg="#e3f2fd", fg="#1976D2")
title_label.pack(pady=(5, 0))

top_section = tk.LabelFrame(root, text="사용자 정보 입력", font=("맑은 고딕", 12, "bold"), bg="#e3f2fd")
top_section.pack(fill=tk.X, pady=(0, 10), padx=10)

# ---- 수직 배치: 레이블 위, 입력칸+단위 아래 ----
# 키
height_label = tk.Label(top_section, text="키", font = font, bg="#e3f2fd")
height_label.pack(anchor="w", pady=(8, 0))
height_row = tk.Frame(top_section, bg="#e3f2fd")
height_row.pack(anchor="w", pady=(2, 6))
height_input = tk.Entry(height_row, font=font, width=30)
height_input.pack(side=tk.LEFT)
cm_label = tk.Label(height_row, text="cm", font=font, bg="#e3f2fd")
cm_label.pack(side=tk.LEFT, padx=(6,0))

# 몸무게
weight_label = tk.Label(top_section, text="몸무게", font = font, bg="#e3f2fd")
weight_label.pack(anchor="w", pady=(4, 0))
weight_row = tk.Frame(top_section, bg="#e3f2fd")
weight_row.pack(anchor="w", pady=(2, 8))
weight_input = tk.Entry(weight_row, font=font, width=30)
weight_input.pack(side=tk.LEFT)
kg_label = tk.Label(weight_row, font=font, text="kg", bg="#e3f2fd")
kg_label.pack(side=tk.LEFT, padx=(6,0))

# 중앙·좌우 프레임
center_frame = tk.Frame(root, bg="#e3f2fd")
center_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

left_frame = tk.Frame(center_frame, bg="#BBDEFB", relief=tk.RAISED, bd=2)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
right_frame = tk.Frame(center_frame, bg="white", relief=tk.RAISED, bd=2)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

option_title = tk.Label(left_frame, font=font, text = "옵션", bg="#BBDEFB")
option_title.pack(pady=5)

options = ['BMI 검사', '체중 관리']
option_combobox = ttk.Combobox(left_frame, values=options, font=font, width=15, state="readonly")
option_combobox.pack(pady=10)
option_combobox.set("선택해주세요.")

right_title = tk.Label(right_frame, text="결과가 입력됩니다.", font=("맑은 고딕", 22, "bold"), bg="white")
right_title.pack(pady=5)
result_label = tk.Label(right_frame, text="", font=font, bg="white")
result_label.pack(pady=5)
standard_label = tk.Label(right_frame, text="", font=font, bg='white')
standard_label.pack(pady=25)

def selected_option():
    if option_combobox.get() == 'BMI 검사':
        bmi_check()
    elif option_combobox.get() == '체중 관리':
        calculate_weight_plan()

selected_button = tk.Button(left_frame, font=font, text="결과 확인", command=selected_option)
selected_button.pack(pady=10)

def bmi_check():
    try:
        height = float(height_input.get()) / 100
        weight = float(weight_input.get())

        if height <= 0 or weight <= 0:
            msgbox.showwarning("입력 오류", "키와 몸무게를 입력해주세요")
            return
        
        bmi = weight / (height*height)
        if bmi < 18.5: 
            color = "#1976d2"
            result = "저체중"
        elif 18.5 <= bmi < 23 : 
            color = "#2e7d32"
            result = "정상"
        elif 23 <= bmi < 25 : 
            color = "#f57c00"
            result = "과체중"
        else: 
            color = "#d32f2f"
            result = "비만"

        right_title.config(text="BMI 검사", bg="white")
        result_label.config(text=f"BMI: {bmi:.2f}\n결과: {result}", bg="white", fg=color, font=("맑은 고딕", 12, "bold"))
        standard_label.config(text="저체중: ~18.4\n정상: 18.5~22.9\n과체중: 23.0~24.9\n비만: 25.0~", bg="white")

    except ValueError:
        msgbox.showerror("입력 오류", "키와 몸무게를 입력해주세요")

def calculate_weight_plan():
    try:
        height = float(height_input.get()) / 100
        weight = float(weight_input.get())

        if height <= 0 or weight <= 0:
            msgbox.showwarning("입력 오류", "키와 몸무게를 입력해주세요")
            return
        
        bmi = weight / (height*height)
        if bmi < 18.5: 
            kcal = 2300
        elif 18.5 <= bmi < 23: 
            kcal = 2100
        elif 23 <= bmi < 25: 
            kcal = 1900            
        else: 
            kcal = 1900

        standard_weight = height*height*22
        target_months = abs(standard_weight - weight) / 3

        if kcal == 2100:
            standard_label.config(text="현재 체중을 유지하는것이 가장 좋습니다.", bg="white")
        else: 
            standard_label.config(text=f"권장 체중까지 예상 기간: {target_months:.1f}개월", bg="white")
    
        right_title.config(text="체중 관리", bg="white")
        result_label.config(text=f"권장 체중: {standard_weight:.2f}kg\n 하루 권장 칼로리 {kcal}kcal", bg="white")

    except ValueError:
        msgbox.showerror("입력 오류", "키와 몸무게를 입력해주세요")
        
bottom_frame = tk.Frame(root, bg="#BBDEFB", relief=tk.RAISED, bd=2, height=50)
bottom_frame.pack(fill=tk.BOTH, padx=5, pady=5)
bottom_frame.pack_propagate(False)

def refresh():
    height_input.delete(0, tk.END)
    weight_input.delete(0, tk.END)
    right_title.config(text="결과가 입력됩니다.", font=("맑은 고딕", 22, "bold"))
    result_label.config(text="")
    standard_label.config(text="")

refresh_button = tk.Button(bottom_frame, font=font, text="다시 입력", command=refresh, bg="#6495ed")
refresh_button.pack(side=tk.LEFT, padx=10, pady= 5)

def on_exit():
    if msgbox.askyesno("종료", "프로그램을 종료하시겠습니까?"):
        root.destroy()

exit_button = tk.Button(bottom_frame, text="종료", font=("맑은 고딕", 11), command=on_exit, bg="#ef5350", fg="white")
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
