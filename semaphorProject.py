# فاطمه پاک سیما
# 40006593
# پروژه دوم سیستم عامل:سمافورها
#پروژه پرواز

# فراخوانی کتابخانه های لازم
import time
import datetime
import pandas as pd
import threading

# خوانش فایل اکسل ضمیمه
#خواندن فرودگاه ها از فایل اکسل
def ReadAirports():
    global Airports
    excel_file_path = 'Flight_Data.xlsx'
    df = pd.read_excel(excel_file_path)
    for index, row in df.iterrows():
        row_object = Airport(city=row['City'], airport_capacity=row['Airport capacity'], state=row['State'])
        Airports.append(row_object)

#خواندن پروازها از فایل اکسل
def ReadFlights():
    global Flights
    excel_file_path = 'Flight_Data.xlsx'
    df = pd.read_excel(excel_file_path, sheet_name=1)
    for index, row in df.iterrows():
        row_object = Flight(flight_number=row['flight number'], origin=row['origin'], destination=row['destination'], time_to_move=row['time to move'], flight_time=row['flight time'])
        Flights.append(row_object)

# کلاس برای هواپیما
class Plane:
    def init(self, locate):
        self.locate = locate
        self.flight: Flight = None

#کلاس فرودگاه
class Airport:
    def init(self, city, airport_capacity, state):
        self.city = city
        initialPlane = Plane(self.city)
        self.state = state
        self.planes: list[Plane] = [initialPlane]
        self.airport_capacity = airport_capacity # ظرفیت فرودگاه
        self.CapacityS = threading.Semaphore(self.airport_capacity) #نخهای ظرفیت فرودگاه ها
        self.PlaneS = threading.Semaphore(len(self.planes)) # تعداد هواپیما های موجود در فرودگاه
        self.controltower = ControlTower(self.city)

    def waitP(self):
        return self.PlaneS.acquire(timeout=30)

    def signalP(self):
        self.PlaneS.release()

    def waitC(self):
        self.CapacityS.acquire()

    def signalC(self):
        self.CapacityS.release()
    #چک کردن پروازهای در دسترس
    def chackAvailablePlane(self, f: Flight):
        return self.controltower.checkPlane(self, f)
    #چک کردن ظرفیت
    def checkCapacityAvailable(self):
        self.controltower.checkCapacity(self)
    #چک کردن کامل شدن
    def processcomplete(self, p: Plane):
        self.controltower.increasePlane(self, p)

#کلاس پرواز
class Flight(threading.Thread):

    def init(self, flight_number, origin, destination, time_to_move, flight_time):
        super().init()
        self.flight_number = flight_number # شماره پرواز
        self.origin = origin # فرودگاه مبدا
        self.destination = destination # فرودگاه مقصد
        self.time_to_move = time_to_move # زمان حرکت
        self.flight_time = flight_time # مدت زمان پرواز
        self.status = False #وضعیت

    # تابع اجرای پرواز
    def run(self):

        start_time = datetime.datetime.now().timestamp() #زمان شروع پرواز
        time.sleep(self.time_to_move) 
        print(
            f"Time:{self.time_to_move} | {self.flight_number} request to {self.destination} controls an wait to response\n")
        for a in Airports:
            if a.city == self.origin:
                oairport = a #فرودگاه مبدا
                break
        for b in Airports:
            if b.city == self.destination:
                dairport = b #فرودگاه مقصد
                break
        s = oairport.chackAvailablePlane(self) #در دسترس بودن هواپیما در فرودگاه مبدا
        if self.status:
            dairport.checkCapacityAvailable()
            finish_time = int(datetime.datetime.now().timestamp() - start_time) #زمان پایان
            print(
                f"Time:{finish_time} | {self.flight_number} request accept by {self.destination} controls and fly from {self.origin} to {self.destination}\n")
            time.sleep(self.flight_time)
            dairport.processcomplete(s)


Airports: list[Airport] = [] #لیست فرودگاه ها
Flights: list[Flight] = [] #لیست پروازها

#کلاس برای برج مراقبت
class ControlTower:
    def init(self, city):
        self.city = city
    #چک کردن وضعیت هواپیما
    def checkPlane(self, a: Airport, f: Flight):
        status = a.waitP()
        if status:
            f.status = True
            temp = a.planes.pop()
            temp.locate = f.destination
            temp.flight = f
            return temp
    #چک کردن ظرفیت
    def checkCapacity(self, a: Airport):
        a.waitC()

    #افزایش هواپیما
    def increasePlane(self, a: Airport, p: Plane):
        a.planes.append(p)
        a.signalC()
        a.signalP()
#برای اجرا main  تابع
def main():
    ReadFlights()
    ReadAirports()
    #شروع و جوین پروازها
    for i in Flights:
        i.start() 
    for i in Flights:
        i.join()
    for i in Flights:
        if not i.status:
            print(f"{i.flight_number} failed to take off within 30 hours")


if name == "main":
    main()