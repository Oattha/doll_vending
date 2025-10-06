import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os, math

BASE_DIR = os.path.dirname(__file__)
ITEMS_PER_PAGE = 6
COLUMNS = 3

PRODUCTS = [
    {"id": 12,"name": "🐣 เป็ดอุอิอา",     "price": 349, "img": os.path.join(BASE_DIR, "assets", "S__9863185.jpg"),      "stock": 2},
    {"id": 11, "name": "🐻 หมีบราวนี่",   "price": 149, "img": os.path.join(BASE_DIR, "assets", "bear.png"),     "stock": 1},
    {"id": 15, "name": "หมาชิบะ",    "price": 429, "img": os.path.join(BASE_DIR, "assets", "S1.jpg"),  "stock": 3},
    {"id": 15, "name": "แมวขาว",     "price": 399, "img": os.path.join(BASE_DIR, "assets", "S2.jpg"),     "stock": 4},
    {"id": 15, "name": "หมาสามสี",     "price": 399, "img": os.path.join(BASE_DIR, "assets", "S6.jpg"),     "stock": 4},
    {"id": 17, "name": "ไทเก้อ",     "price": 329, "img": os.path.join(BASE_DIR, "assets", "S3.jpg"),     "stock": 2},
    {"id": 18, "name": "ไส้แมว",       "price": 379, "img": os.path.join(BASE_DIR, "assets", "S8.jpg"),      "stock": 3},
    {"id": 19, "name": "แมวดำ",     "price": 459, "img": os.path.join(BASE_DIR, "assets", "S4.jpg"),    "stock": 4},
    {"id": 20, "name": "แมวอ้วน",      "price": 499, "img": os.path.join(BASE_DIR, "assets", "S7.jpg"),   "stock": 5},
    {"id": 21, "name": "โทโท่โร่",     "price": 1999, "img": os.path.join(BASE_DIR, "assets", "S5.jpg"),   "stock": 6},

    {"id": 1, "name": "🐻 ตุ๊กตาหมี",   "price": 149, "img": os.path.join(BASE_DIR, "assets", "bear5.png"),     "stock": 5},
    {"id": 2, "name": "💙 โดเรมอน",    "price": 429, "img": os.path.join(BASE_DIR, "assets", "doraemon.png"),  "stock": 3},
    {"id": 3, "name": "🎀 คิตตี้",     "price": 399, "img": os.path.join(BASE_DIR, "assets", "kitty.png"),     "stock": 4},
    {"id": 4, "name": "🐼 แพนด้า",     "price": 329, "img": os.path.join(BASE_DIR, "assets", "panda.png"),     "stock": 2},
    {"id": 5, "name": "🍯 พูห์",       "price": 379, "img": os.path.join(BASE_DIR, "assets", "pooh.png"),      "stock": 3},
    {"id": 6, "name": "🌸 สติทช์",     "price": 459, "img": os.path.join(BASE_DIR, "assets", "stitch.png"),    "stock": 4},
    {"id": 7, "name": "⚡ ปิกาจู",      "price": 499, "img": os.path.join(BASE_DIR, "assets", "pikachu.png"),   "stock": 5},
    {"id": 8, "name": "🐧 เพนกวิน",     "price": 199, "img": os.path.join(BASE_DIR, "assets", "penguin.png"),   "stock": 6},
    {"id": 9, "name": "🦊 ฟ็อกซี่",    "price": 289, "img": os.path.join(BASE_DIR, "assets", "fox.png"),       "stock": 3},
    {"id": 10,"name": "🦁 ไลอ้อน",     "price": 349, "img": os.path.join(BASE_DIR, "assets", "lion.png"),      "stock": 2},
    {"id": 12,"name": "🐣 เป็ดน้อย",     "price": 349, "img": os.path.join(BASE_DIR, "assets", "S__9863185.jpg"),      "stock": 2},
]

PASTEL_COLORS = ["#FFD6E0", "#D6F0FF", "#FFF3B0", "#E0FFD6", "#F5D6FF"]


class CuteVendingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎁 ตู้ขายตุ๊กตาน่ารักๆ 🎀")
        self.configure(bg="#FAFAFA")
        self.geometry("1200x720")

        self.cart = []
        self.total = 0
        self.page = 0
        self.cash_inserted = 0

        # Layout 2 คอลัมน์
        main_frame = tk.Frame(self, bg="#FAFAFA")
        main_frame.pack(fill="both", expand=True)

        main_frame.grid_columnconfigure(0, weight=3)
        main_frame.grid_columnconfigure(1, weight=1)

        # ซ้าย = สินค้า
        left_frame = tk.Frame(main_frame, bg="#FAFAFA")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # ขวา = ตะกร้า + ชำระเงิน
        right_frame = tk.Frame(main_frame, bg="#FFFFFF", bd=0, highlightbackground="#DDD", highlightthickness=1)
        right_frame.grid(row=0, column=1, sticky="ns", padx=15, pady=15)

        # ========== ซ้าย ==========
        title = tk.Label(left_frame, text="✨ ตู้หยอดเหรียญตุ๊กตา ✨",
                         font=("Segoe UI", 22, "bold"), bg="#FAFAFA", fg="#FF4D8D")
        title.pack(pady=(10, 10))

        self.grid_frame = tk.Frame(left_frame, bg="#FAFAFA")
        self.grid_frame.pack(pady=10)

        nav = tk.Frame(left_frame, bg="#FAFAFA")
        nav.pack(pady=(0, 8))
        self.prev_btn = tk.Button(nav, text="⬅ ก่อนหน้า", command=self.prev_page,
                                  font=("Segoe UI", 10), state="disabled", relief="flat", bg="#E0E0E0")
        self.prev_btn.pack(side="left", padx=6)
        self.page_label = tk.Label(nav, text="หน้า 1/1", font=("Segoe UI", 11, "bold"),
                                   bg="#FAFAFA", fg="#333")
        self.page_label.pack(side="left", padx=6)
        self.next_btn = tk.Button(nav, text="ถัดไป ➡", command=self.next_page,
                                  font=("Segoe UI", 10), relief="flat", bg="#E0E0E0")
        self.next_btn.pack(side="left", padx=6)

        # ========== ขวา ==========
        cart_label = tk.Label(right_frame, text="🛒 ตะกร้าสินค้า",
                              font=("Segoe UI", 16, "bold"),
                              bg="#FFFFFF", fg="#FF1493")
        cart_label.pack(pady=8)

        self.cart_list = tk.Listbox(right_frame, width=40, height=8, bg="#F9F9F9", fg="#333",
                                    font=("Segoe UI", 10), relief="flat", highlightthickness=1, highlightbackground="#DDD")
        self.cart_list.pack(pady=5)

        tk.Button(right_frame, text="❌ ลบสินค้า", command=self.remove_item,
                  font=("Segoe UI", 10, "bold"),
                  bg="#FF4D4D", fg="white", relief="flat").pack(pady=6)

        self.total_var = tk.StringVar(value="💰 รวม: 0 บาท")
        tk.Label(right_frame, textvariable=self.total_var,
                 font=("Segoe UI", 12, "bold"),
                 bg="#FFFFFF", fg="#FF4500").pack(pady=6)

        # ปุ่มหยอดเงิน
        tk.Label(right_frame, text="💵 หยอดเหรียญ / ธนบัตร",
                 font=("Segoe UI", 13, "bold"),
                 bg="#FFFFFF", fg="#006400").pack(pady=10)

        money_frame = tk.Frame(right_frame, bg="#FFFFFF")
        money_frame.pack(pady=10)

        for value in [1000, 500, 100, 50, 20, 10, 5, 2, 1]:
            btn = tk.Button(money_frame, text=f"{value}฿",
                      command=lambda v=value: self.insert_money(v),
                      width=8, font=("Segoe UI", 10, "bold"),
                      bg="#4DA6FF", fg="white", relief="flat", activebackground="#1E90FF")
            btn.pack(pady=2)

        self.cash_var = tk.StringVar(value="💵 เงินที่หยอด: 0 บาท")
        tk.Label(right_frame, textvariable=self.cash_var,
                 font=("Segoe UI", 12, "bold"),
                 bg="#FFFFFF", fg="#000080").pack(pady=10)

        tk.Button(right_frame, text="✅ ชำระเงิน", command=self.pay,
                  font=("Segoe UI", 12, "bold"),
                  bg="#FF69B4", fg="white", relief="flat", activebackground="#FF1493").pack(pady=10)

        # โหลดสินค้า
        self.render_products()
        self.bind("<Delete>", lambda e: self.remove_item())

    # ---------- Pagination ----------
    def total_pages(self):
        return max(1, math.ceil(len(PRODUCTS) / ITEMS_PER_PAGE))

    def next_page(self):
        if (self.page + 1) < self.total_pages():
            self.page += 1
            self.render_products()

    def prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.render_products()

    # ---------- Products ----------
    def render_products(self):
        for w in self.grid_frame.winfo_children():
            w.destroy()

        start = self.page * ITEMS_PER_PAGE
        end = start + ITEMS_PER_PAGE
        products_page = PRODUCTS[start:end]

        for i, p in enumerate(products_page):
            color = PASTEL_COLORS[i % len(PASTEL_COLORS)]
            card = tk.Frame(self.grid_frame, bg=color, bd=0, relief="flat", highlightthickness=0)
            card.grid(row=i // COLUMNS, column=i % COLUMNS, padx=15, pady=15, ipadx=6, ipady=6)

            try:
                img = Image.open(p["img"]).resize((100, 100))
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(card, image=photo, bg=color, bd=0)
                label.image = photo
                label.pack(pady=5)
            except Exception:
                tk.Label(card, text="[ไม่มีรูป]", bg=color).pack()

            tk.Label(card, text=p["name"], font=("Segoe UI", 11, "bold"),
                     bg=color, fg="#333").pack()
            tk.Label(card, text=f"💸 {p['price']} บาท", font=("Segoe UI", 10),
                     bg=color).pack()
            tk.Label(card, text=f"📦 คงเหลือ {p['stock']}", font=("Segoe UI", 9),
                     bg=color, fg="#444").pack()

            btn = tk.Button(card, text="ใส่ตะกร้า 💖",
                            command=lambda pid=p["id"]: self.add(pid),
                            font=("Segoe UI", 9, "bold"),
                            bg="#FF69B4", fg="white", relief="flat", activebackground="#FF1493")
            if p["stock"] <= 0:
                btn.config(state="disabled", text="หมดแล้ว 😢", bg="#CCCCCC")
            btn.pack(pady=6)

        self.page_label.config(text=f"หน้า {self.page + 1}/{self.total_pages()}")
        self.prev_btn.config(state=("normal" if self.page > 0 else "disabled"))
        self.next_btn.config(state=("normal" if end < len(PRODUCTS) else "disabled"))

    # ---------- Cart ----------
    def add(self, pid):
        p = next((x for x in PRODUCTS if x["id"] == pid), None)
        if not p or p["stock"] <= 0:
            return
        p["stock"] -= 1
        self.cart.append({"id": p["id"], "name": p["name"], "price": p["price"]})
        self.refresh_cart()
        self.render_products()

    def refresh_cart(self):
        self.cart_list.delete(0, "end")
        self.total = sum(item["price"] for item in self.cart)
        for item in self.cart:
            self.cart_list.insert("end", f'{item["name"]} - {item["price"]} บาท')
        self.total_var.set(f"💰 รวม: {self.total} บาท")

    def remove_item(self):
        sel = self.cart_list.curselection()
        if not sel:
            messagebox.showinfo("ไม่ได้เลือก", "กรุณาเลือกสินค้าที่จะลบ 💡")
            return
        idx = sel[0]
        removed = self.cart.pop(idx)
        prod = next((x for x in PRODUCTS if x["id"] == removed["id"]), None)
        if prod:
            prod["stock"] += 1
        self.refresh_cart()
        self.render_products()

    # ---------- Money Insert ----------
    def insert_money(self, value):
        self.cash_inserted += value
        self.cash_var.set(f"💵 เงินที่หยอด: {self.cash_inserted} บาท")

    # ---------- Pay ----------
    def pay(self):
        if self.total == 0:
            messagebox.showinfo("ไม่มีสินค้า", "เลือกสินค้าก่อนน้า 💕")
            return
        if self.cash_inserted < self.total:
            messagebox.showerror("เงินไม่พอ", f"💸 ต้องการ {self.total} บาท")
            return
        change = self.cash_inserted - self.total
        messagebox.showinfo("สำเร็จ", f"ขอบคุณที่ซื้อค่ะ 💖 เงินทอน {change} บาท 🎀")
        self.cart.clear()
        self.refresh_cart()
        self.cash_inserted = 0
        self.cash_var.set("💵 เงินที่หยอด: 0 บาท")


if __name__ == "__main__":
    CuteVendingApp().mainloop()