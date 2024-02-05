from pyglet.window import Window  # สำหรับ class Window จาก module pyglet.window 
from pyglet.app import run  # สำหรับใช้ function run จาก module pyglet.app
from pyglet.shapes import Rectangle  # สำหรับใช้ class Rectangle จาก module pyglet.shapes
from pyglet.graphics import Batch  # สำหรับใช้ class Batch จาก module pyglet.graphics
from pyglet import clock  # สำหรับใช้นับเวลา จาก module clock

# แสดงขั้นตอนวิธีการทำ bubble sort
class Renderer(Window):
    # สร้าง method สำหรับใช้ทำ bubble sort = สร้างกราฟแท่ง
    def __init__(self):
        super().__init__(640, 640, "bubble sort")  # ตั้งค่าขนาดหน้าต่างและตั้งชื่อหน้า run code 
        self.batch = Batch()  # สร้าง Batch object สำหรับให้ประมวลลผลได้หลายครั้ง
        self.x = [3, 4, 2, 1, 5]  # สร้าง Array เก็บค่าความสูงของกราฟแท่ง = ค่าที่ต้องนำไป sorting
        self.bars = []  # กำหนดให้เก็บค่าในรูปแบบแท่ง
        for e, i in enumerate(self.x):  # Loop ที่นำค่าจาก Array มาสร้างเป็นกราฟแท่ง
            self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=(255, 255, 255)))  
            # กำหนดให้สร้างเป็นสี่เหลี่ยมผืนผ้า โดยใส่ค่าดังต่อไปนี้ ขนาดความกว้าง ความยาว ระยะห่าง สี และ batch

    # สำหรับแสดงผล(วิธีการทำ)บนหน้าจอ
    def on_update(self, deltatime):  
        n = len(self.x) # รับค่าความยาวของ Array
        for i in range(n - 1):  # กำหนดให้ Loop ทำงานตามจำนวนรอบของ Array
            for j in range(0, n - i - 1):  # Loop ในส่วนที่ยังไม่ถูก sort ใน Array
                if self.x[j] > self.x[j + 1]:  # เปรียบเทียบค่า ถ้าค่าฝั่งซ้ายมีมากกว่าค่าฝั่งขวา
                    self.x[j], self.x[j + 1] = self.x[j + 1], self.x[j]  # ให้สลับเปลี่ยน = เปลี่ยนตำแหน่งกราฟแท่ง
                    self.bars = []  # อัปเดตค่ากราฟแท่งใหม่ใน List
                    for e, i in enumerate(self.x):  # กำหนดให้ Loop ทำงานตามจำนวนรอบของ Array
                        if e == j or e == j + 1:  # กำหนดให้ใส่สีแดงในกราฟแท่ง เมื่อกำลังเปรียบเทียบระหว่าง 2 กราฟแท่ง และหากไม่ใช่กราฟแท่งที่ถูกเปรียบเทียบอยู่จะมีสีขาว
                            color = (255, 0, 0) 
                        else:
                            color = (255, 255, 255)  
                        self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=color))  # อัปเดตค่าสี และตำแหน่งที่สลับ สำหรับสีแดง
                    return
        # เปลี่ยนสีกราฟแท่งทั้งหมดให้กลับเป็นสีขาวหลังจากที่ sort เสร็จสิ้น
        self.bars = [Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch, color=(255, 255, 255)) for e, i in enumerate(self.x)]  # อัปเดตค่าสี และตำแหน่งที่สลับ สำหรับสีขาว

    # สำหรับให้ค่าแสดงผลบนหน้าจอ
    def on_draw(self):
        self.clear()  # ตรวจสอบว่าหน้าจอพร้อมแสดงผล
        self.batch.draw()  # แสดงค่าของ Batch = แสดงผลกราฟแท่ง


renderer = Renderer()  # รวมผลลัพธ์ทั้งหมดจาก class Renderer
clock.schedule_interval(renderer.on_update, 3)  # กำหนดเวลาในการอัปเดตผลลัพธ์ทุก 3 วินาที
run()  # เรียกใช้ Pyglet application = แสดงผลลัพธ์ทั้งหมดบนหน้า run code
