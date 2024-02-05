from pyglet.window import Window  # สำหรับ class Window จาก module pyglet.window 
from pyglet.app import run  # สำหรับใช้ function run จาก module pyglet.app
from pyglet.shapes import Rectangle  # สำหรับใช้ class Rectangle จาก module pyglet.shapes
from pyglet.graphics import Batch  # สำหรับใช้ class Batch จาก module pyglet.graphics
from pyglet import clock  # สำหรับใช้นับเวลา จาก module clock

# แปลงรหัสสีฐาน 16 เป็นแบบ RGB
def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16), 255

# แสดงขั้นตอนวิธีการทำ merge sort
class Renderer(Window):
    # สร้าง method สำหรับใช้ทำ bubble sort = สร้างกราฟแท่ง
    def __init__(self):
        super().__init__(800, 700, "Merge Sort") # ตั้งค่าขนาดหน้าต่างและตั้งชื่อหน้า run code 
        self.batch = Batch() # สร้าง Batch object สำหรับให้ประมวลลผลได้หลายครั้ง
        self.x =  [3, 4, 2, 1, 5, 6, 4] # สร้าง Array เก็บค่าความสูงของกราฟแท่ง = ค่าที่ต้องนำไป sorting
        self.bars = [] # กำหนดให้เก็บค่าในรูปแบบแท่ง
        for e, i in enumerate(self.x): # Loop ที่นำค่าจาก Array มาสร้างเป็นกราฟแท่ง
            self.bars.append(Rectangle(80 + e * 100, 80, 60, i * 100, batch=self.batch, color=(255, 255, 255)))
            # กำหนดให้สร้างเป็นสี่เหลี่ยมผืนผ้า โดยใส่ค่าดังต่อไปนี้ ขนาดความกว้าง ความยาว ระยะห่าง สี และ batch
        self.merge_generator = self.merge_sort_generator(self.x.copy())

        clock.schedule_once(self.start_merge_sort, 2) # หน่วงเวลา 2 วินาที เพื่อแสดงกราฟแท่งทั้งหมดก่อนการ sorting

    def start_merge_sort(self, dt):
        self.update_bars()

    # สำหรับแสดงผล(วิธีการทำ)บนหน้าจอ
    def merge_sort_generator(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            yield left_half.copy()
            yield right_half.copy()

            yield from self.merge_sort_generator(left_half)
            yield from self.merge_sort_generator(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            yield arr.copy()

    def update_bars(self):
        try:
            intermediate_state = next(self.merge_generator)
            self.bars = []

            for e, i in enumerate(intermediate_state):
                self.bars.append(Rectangle(80 + e * 100, 80, 60, i * 100, batch=self.batch, color=(255, 255, 255)))

        except StopIteration:
            clock.unschedule(self.on_update)

    def on_update(self, deltatime):
        self.update_bars()

    # สำหรับให้ค่าแสดงผลบนหน้าจอ
    def on_draw(self):
        self.clear()  # ตรวจสอบว่าหน้าจอพร้อมแสดงผล
        self.batch.draw()  # แสดงค่าของ Batch = แสดงผลกราฟแท่ง

renderer = Renderer()  # รวมผลลัพธ์ทั้งหมดจาก class Renderer
clock.schedule_interval(renderer.on_update, 3)  # กำหนดเวลาในการอัปเดตผลลัพธ์ทุก 3 วินาที
run()  # เรียกใช้ Pyglet application = แสดงผลลัพธ์ทั้งหมดบนหน้า run code
