from pyglet.window import Window  # สำหรับ class Window จาก module pyglet.window 
from pyglet.app import run  # สำหรับใช้ function run จาก module pyglet.app
from pyglet.shapes import Rectangle  # สำหรับใช้ class Rectangle จาก module pyglet.shapes
from pyglet.graphics import Batch  # สำหรับใช้ class Batch จาก module pyglet.graphics
from pyglet import clock  # สำหรับใช้นับเวลา จาก module clock
import math  # สำหรับใช้คำนวณ จาก module math

# แปลงรหัสสีฐาน 16 เป็นแบบ RGB
def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

# แสดงขั้นตอนวิธีการทำ merge sort
class Renderer(Window):
    # สร้าง method สำหรับใช้ทำ bubble sort = สร้างกราฟแท่ง
    def __init__(self):  
        super().__init__(800, 600, "Merge Sort")  # ตั้งค่าขนาดหน้าต่างและตั้งชื่อหน้า run code 
        self.batch = Batch()  # สร้าง Batch object สำหรับให้ประมวลลผลได้หลายครั้ง
        self.x = [3, 4, 2, 9, 5, 3, 4, 6, 1, 5, 7, 4, 6, 1, 8]  # สร้าง Array เก็บค่าความสูงของกราฟแท่ง = ค่าที่ต้องนำไป sorting
        self.bars = []  # กำหนดให้เก็บค่าในรูปแบบแท่ง
        for e, i in enumerate(self.x):  # Loop ที่นำค่าจาก Array มาสร้างเป็นกราฟแท่ง
            self.bars.append(Rectangle(20 + e * 50, 50, 40, i * 50, batch=self.batch, color=(255, 255, 255)))
            # กำหนดให้สร้างเป็นสี่เหลี่ยมผืนผ้า โดยใส่ค่าดังต่อไปนี้ ขนาดความกว้าง ความยาว ระยะห่าง สี และ batch
        self.merge_sort_step = None  # เริ่มขึ้นตอนการทำ merge sort

    # ฟังก์ชั่น และวิธีการทำ merge sort
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]: 
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    # สำหรับแสดงผล(วิธีการทำ)บนหน้าจอ
    def on_update(self, deltatime):
        if self.merge_sort_step is None: #เตรียมค่าสำหรับ merge sort
            self.merge_sort_step = 0  # กำหนดค่าเริ่มต้นเป็น 0
            self.merge_sort(self.x.copy())

        if self.merge_sort_step < len(self.x):  # กำหนดเงื่อนไข หากจำนวนรอบที่สนน้อยกว่าค่าความยาว Array ให้วนรอบต่อ
            min_idx = self.merge_sort_step  # กำหนดขั้นต่ำในการวนรอบ
            for j in range(self.merge_sort_step + 1, len(self.x)):  # Loop เพื่อหาค่าที่ยังไม่ถูก sort
                if self.x[j] < self.x[min_idx]:
                    min_idx = j
            self.x[self.merge_sort_step], self.x[min_idx] = self.x[min_idx], self.x[self.merge_sort_step]  # ให้สลับเปลี่ยน = เปลี่ยนตำแหน่งกราฟแท่ง

            self.bars = []  # อัปเดตค่ากราฟแท่งใหม่ใน List
            for e, i in enumerate(self.x):  # กำหนดให้ Loop ทำงานตามจำนวนรอบของ Array
                if e == min_idx or e == self.merge_sort_step:  # กำหนดให้ใส่สีแดงในกราฟแท่งที่กำลังถูกพิจารณา และสีขาวในกราฟแท่งที่ไม่ถูกพิจารณา
                    color = (255, 0, 0)
                else:
                    color = (255, 255, 255)
                self.bars.append(Rectangle(20 + e * 50, 50, 40, i * 50, batch=self.batch, color=color))  # อัปเดตค่าสี และตำแหน่งที่สลับ สำหรับสีแดง
            self.merge_sort_step += 1  # เพิ่มรอบครั้งละ 1 สำหรับวน Loop
        else:
            # เปลี่ยนสีกราฟแท่งทั้งหมดให้กลับเป็นสีขาวหลังจากที่ sort เสร็จสิ้น
            self.bars = [Rectangle(20 + e * 50, 50, 40, i * 50, batch=self.batch, color=(255, 255, 255)) for e, i in enumerate(self.x)] # อัปเดตค่าสี และตำแหน่งที่สลับ สำหรับสีขาว

    # สำหรับให้ค่าแสดงผลบนหน้าจอ
    def on_draw(self):
        self.clear()  # ตรวจสอบว่าหน้าจอพร้อมแสดงผล
        self.batch.draw()  # แสดงค่าของ Batch = แสดงผลกราฟแท่ง


renderer = Renderer()  # รวมผลลัพธ์ทั้งหมดจาก class Renderer
clock.schedule_interval(renderer.on_update, 3)  # กำหนดเวลาในการอัปเดตผลลัพธ์ทุก 3 วินาที
run()  # เรียกใช้ Pyglet application = แสดงผลลัพธ์ทั้งหมดบนหน้า run code
