import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# 初始化 tkinter（不顯示主視窗）
root = tk.Tk()
root.withdraw()

# 讓使用者輸入要取代的文字
placeholder = simpledialog.askstring("" \
    "輸入頁",
    "請輸入要取代的文字")
if not placeholder:
    messagebox.showerror("錯誤", "未輸入要取代的文字")
    exit()

# 選擇 template 檔案
messagebox.showinfo("選取原始文字檔", "選一個檔案")
template_path = filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt")]
)
if not template_path:
    messagebox.showerror("錯誤", "未選取原始文字檔")
    exit()

# 選擇 words 檔案
messagebox.showinfo("選取替換字檔案", "選一個檔案")
words_path = filedialog.askopenfilename(
    filetypes=[("Text Files", "*.txt")]
)
if not words_path:
    messagebox.showerror("錯誤", "未選取替換字檔案")
    exit()

# 建立輸出資料夾
output_dir = "替換文字"
os.makedirs(output_dir, exist_ok=True)

# 讀取模板內容
with open(template_path, 'r', encoding='utf-8') as file:
    template = file.read()

if placeholder not in template:
    messagebox.showerror("錯誤", f"原始文字檔中找不到要替換的詞「{placeholder}」，請檢查是否輸入錯誤。")
    exit()


# 讀取替換詞列表
with open(words_path, 'r', encoding='utf-8') as file:
    replacements = [line.strip() for line in file if line.strip()]

# 替換並寫入檔案
for i, word in enumerate(replacements, start=1):
    replaced_text = template.replace(placeholder, word)
    output_file = os.path.join(output_dir, f"output_{i}.txt")
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(replaced_text)

# 顯示完成提示
messagebox.showinfo("完成", f"共產生 {len(replacements)} 個檔案，輸出於資料夾：{output_dir}")
