import tkinter as tk #창 구성
from tkinter import ttk #콤보 박스
from tkinter import messagebox as msgbox #경고창

# 색상 변수
bg_main = "#e3f2fd"
bg_section = "#BBDEFB"
color_underweight = "#1976d2"
color_normal = "#2e7d32"
color_overweight = "#f57c00"
color_obese = "#d32f2f"
color_button_refresh = "#6495ed"
color_button_exit = "#ef5350"

# 폰트 변수
font_normal = ("맑은고딕", 11)
font_title = ('맑은 고딕', 22, "bold")
font_section = ("맑은 고딕", 12, "bold")
font_result = ("맑은 고딕", 12, "bold")
font_diet = ("맑은 고딕", 10, "bold")

root = tk.Tk()
root.geometry('700x500')
root.title("인바디 시뮬레이터")
root.config(bg=bg_main)


#창 최상단 제목
title_label = tk.Label(root, text="인바디 검사!", font=font_title, bg=bg_main, fg=color_underweight)
title_label.pack(pady=(5, 0))

#사용자 정보 입력 section
top_section = tk.LabelFrame(root, text="사용자 정보 입력", font=font_section, bg=bg_main)
top_section.pack(fill=tk.X, pady=(0, 10), padx=10)

#----------사용자 키,몸무게 정보----------
height_label = tk.Label(top_section, text="키", font=font_normal, bg=bg_main, width=10, anchor="w")
height_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

height_input = tk.Entry(top_section, font=font_normal, width=20)
height_input.grid(row=0, column=1, padx=5, pady=10, sticky="w")

cm_label = tk.Label(top_section, text="cm", font=font_normal, bg=bg_main)
cm_label.grid(row=0, column=2, padx=(0, 10), pady=10, sticky="w")

weight_label = tk.Label(top_section, text="몸무게", font=font_normal, bg=bg_main, width=10, anchor="w")
weight_label.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="w")

weight_input = tk.Entry(top_section, font=font_normal, width=20)
weight_input.grid(row=1, column=1, padx=5, pady=10, sticky="w")

kg_label = tk.Label(top_section, text="kg", font=font_normal, bg=bg_main)
kg_label.grid(row=1, column=2, padx=(0, 10), pady=10, sticky="w")
#--------------------------------------

#---------------중앙 frame--------------
center_frame = tk.Frame(root, bg=bg_main)
center_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
#--------------------------------------

#------------중앙 left_frame option 선택-----------
left_frame = tk.Frame(center_frame, bg=bg_section, relief=tk.RAISED, bd=2)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))

option_title = tk.Label(left_frame, font=font_normal, text="옵션", bg=bg_section)
option_title.pack(pady=5)

options = ['BMI 검사', '체중 관리', '식단 추천']
option_combobox = ttk.Combobox(left_frame, values=options, font=font_normal, width=15, state="readonly")
option_combobox.pack(pady=10)
option_combobox.set("선택해주세요.")

def selected_option():
    if option_combobox.get() == 'BMI 검사':
        bmi_check()
    elif option_combobox.get() == '체중 관리':
        calculate_weight_plan()
    elif option_combobox.get() == '식단 추천':
        dite_plan()

selected_button = tk.Button(left_frame, font=font_normal, text="결과 확인", command=selected_option)
selected_button.pack(pady=10)
#------------------------------------------------

#------------오른쪽 right 결과 확인 frame----------
right_frame = tk.Frame(center_frame, bg="white", relief=tk.RAISED, bd=2)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

right_title = tk.Label(right_frame, text="결과가 입력됩니다.", font=font_title, bg="white")
right_title.pack(pady=5)
result_label = tk.Label(right_frame, text="", font=font_normal, bg="white")
result_label.pack(pady=5)
bmi_info_label = tk.Label(right_frame, text="", font=font_normal, bg="white")
bmi_info_label.pack(pady=25)
#------------------------------------------------

#------------주요 함수----------
#-----키와 체중을 바탕으로 BMI수치 계산 함수-----
def bmi_check():
    try:
        height = float(height_input.get()) / 100
        weight = float(weight_input.get())

        if height <= 0 or weight <= 0:
            msgbox.showwarning("입력 오류", "키와 몸무게를 입력해주세요")
            return
        
        bmi = weight / (height*height)
        if bmi < 18.5: 
            color = color_underweight
            result = "저체중"
        elif 18.5 <= bmi < 23 : 
            color = color_normal
            result = "정상"
        elif 23 <= bmi < 25 : 
            color = color_overweight
            result = "과체중"
        else: 
            color = color_obese
            result = "비만"

        right_title.config(text="BMI 검사", bg="white")
        result_label.config(text=f"BMI: {bmi:.2f}\n결과: {result}", bg="white", fg=color, font=font_result)
        bmi_info_label.config(text="저체중: ~18.4\n정상: 18.5~22.9\n과체중: 23.0~24.9\n비만: 25.0~", bg="white")

    except ValueError:
        msgbox.showerror("입력 오류", "키와 몸무게를 입력해주세요")
#-------------------------------------------

#-----적정 체중을 위해 필요 기간 및 섭취 칼로리 계산-----
def calculate_weight_plan():
    try:
        height = float(height_input.get()) / 100
        weight = float(weight_input.get())

        if height <= 0 or weight <= 0:
            msgbox.showwarning("입력 오류", "키와 몸무게를 입력해주세요")
            return
        
        bmi = weight / (height*height)
        if bmi < 18.5: 
            color = color_underweight
            kcal = 2300
        elif 18.5 <= bmi < 23: 
            color = color_normal
            kcal = 2100
        elif 23 <= bmi < 25: 
            color = color_overweight
            kcal = 1900            
        else: 
            color = color_obese
            kcal = 1900

        standard_weight = height*height*22
        target_months = abs(standard_weight - weight) / 3

        if kcal == 2100:
            bmi_info_label.config(text="현재 체중을 유지하는것이 가장 좋습니다.", bg="white")
        else: 
            bmi_info_label.config(text=f"권장 체중까지 예상 기간: {target_months:.1f}개월", bg="white")
    
        right_title.config(text="체중 관리", bg="white")
        result_label.config(text=f"권장 체중: {standard_weight:.2f}kg\n 하루 권장 칼로리 {kcal}kcal", bg="white", font=font_result, fg=color)

    except ValueError:
        msgbox.showerror("입력 오류", "키와 몸무게를 입력해주세요")
        
#--------------------------------------------------

#-----적정 칼로리를 바탕으로 깨끗한 식단 추천-----
def dite_plan():
    try:
        height = float(height_input.get()) / 100
        weight = float(weight_input.get())

        if height <= 0 or weight <= 0:
            msgbox.showwarning("입력 오류", "키와 몸무게를 입력해주세요")
            return
        diet_plan_1900 = ("⭐️ 체중 감량 유도 (1900kcal) 식단 ⭐️\n1. 아침(400kcal): 현미밥 1/2공기 + 닭가슴살 100g + 브로콜리 50g\n2. 점심(500kcal): 현미밥 3/4공기 + 닭가슴살 100g + 믹스 샐러드 70g + 견과류 10g\n3. 간식(350kcal): 고구마 100g + 프로틴 쉐이크 1/2스쿱 + 방울토마토 50g\n4. 저녁(650kcal): 현미밥 1/2공기 + 닭가슴살 100g + 계란 1개 + 믹스 샐러드 50g")
        diet_plan_2100 = ("⭐️ 현재 체중 유지 (2100kcal) 식단 ⭐️\n1. 아침(500kcal): 현미밥 3/4공기 + 닭가슴살 100g + 브로콜리 50g\n2. 점심(600kcal): 현미밥 1공기 + 닭가슴살 100g + 믹스 샐러드 70g + 견과류\n3. 간식(400kcal): 고구마 100g + 프로틴 쉐이크 1스쿱 + 방울토마토 50g\n4. 저녁(600kcal): 현미밥 3/4공기 + 닭가슴살 100g + 계란 1개 + 믹스 샐러드 50g")
        diet_plan_2300 = ("⭐️ 한 달 1kg 증량 (2300kcal) 식단 ⭐️\n1. 아침(550kcal): 현미밥 1공기 + 닭가슴살 100g + 브로콜리 50g\n2. 점심(700kcal): 현미밥 1.5공기 + 닭가슴살 150g + 믹스 샐러드 50g + 견과류\n3. 간식(450kcal): 고구마 150g + 프로틴 쉐이크 1스쿱 + 방울토마토 50g\n4. 저녁(600kcal): 현미밥 1공기 + 닭가슴살 100g + 계란 1개 + 믹스 샐러드 70g")
        
        bmi = weight / (height*height)
        if bmi < 18.5: 
            color = color_underweight
            result_label.config(text="웨이트 운동을 추천합니다.", font=font_result, fg=color)
            bmi_info_label.config(text=diet_plan_2300, font=font_diet, justify=tk.LEFT)
            
        elif 18.5 <= bmi < 23: 
            color = color_normal
            result_label.config(text="")
            bmi_info_label.config(text=diet_plan_2100, font=font_diet, justify=tk.LEFT)

        elif 23 <= bmi < 25: 
            color = color_overweight
            result_label.config(text="")
            bmi_info_label.config(text=diet_plan_1900, font=font_diet, justify=tk.LEFT)       

        elif 25 <= bmi: 
            color = color_obese
            result_label.config(text="유산소 운동을 추천합니다", font=font_result, fg=color)
            bmi_info_label.config(text=diet_plan_1900, font=font_diet, justify=tk.LEFT)

        right_title.config(text="식단 추천", bg="white")
        

    except ValueError:
        msgbox.showerror("입력 오류", "키와 몸무게를 입력해주세요")
#-------------------------------------------
#-------------------------------------------

#----------하단 기능 버튼 Frame----------
bottom_frame = tk.Frame(root, bg=bg_section, relief=tk.RAISED, bd=2, height=50)
bottom_frame.pack(fill=tk.BOTH, padx=5, pady=5)

#-------사용자 정보 재입력 기능-------
def refresh():
    height_input.delete(0, tk.END)
    weight_input.delete(0, tk.END)
    right_title.config(text="결과가 입력됩니다.", font=font_title)
    result_label.config(text="")
    bmi_info_label.config(text="")

refresh_button = tk.Button(bottom_frame, font=font_normal, text="다시 입력", command=refresh, bg=color_button_refresh)
refresh_button.pack(side=tk.LEFT, padx=10, pady=5)
#----------------------------------

#--------프로그램 종료를 위한 확인 기능--------
def on_exit():
    if msgbox.askyesno("종료", "프로그램을 종료하시겠습니까?"):
        root.destroy()

exit_button = tk.Button(bottom_frame, text="종료", font=font_normal, command=on_exit, bg=color_button_exit, fg="white")
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)
#------------------------------------------
#------------------------------------------

root.mainloop()