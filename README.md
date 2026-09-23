# ✈️ Airport Threading Simulator

A Python-based simulation of an airport flight control system using **threading** and **semaphores** to manage concurrent flights between airports. Developed as a university Operating Systems course project.

---

## ✨ Features

- 🧵 **Multithreading** — Each flight runs as an independent thread
- 🔒 **Semaphore-based Synchronization** — Controls airport capacity and available planes
- 🛫 **Concurrent Flight Handling** — Multiple flights take off and land simultaneously
- 📊 **Excel Input** — Airports and flights are loaded from an Excel file
- 🗼 **Control Tower Logic** — Each airport has its own control tower managing requests
- ⏱️ **Real-time Simulation** — Uses `time.sleep()` to simulate flight and ground delays
- 📝 **Detailed Logging** — Every request, acceptance, and completion is printed with timestamps

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:**
  - `threading` — for concurrent flight execution
  - `datetime` & `time` — for timing and delays
  - `pandas` — for reading Excel data
- **Concepts:** OOP, Threads, Semaphores, Mutual Exclusion, Deadlock Prevention

---

## 📂 Project Structure

- `semaphorProject.py` — Main program (entry point)
- `Flight_Data.xlsx` — Input data (airports & flights)
- `Paksima-Project2-Report.docx` — Full project documentation

---

## 🧩 Core Classes

| Class | Responsibility |
|-------|----------------|
| `Plane` | Represents an aircraft and its current location |
| `Airport` | Manages capacity, planes, and its own control tower |
| `Flight` | A thread that simulates a flight from origin to destination |
| `ControlTower` | Handles synchronization between planes and airports |

---

## 🚀 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/FatemehPaksima/Airport-Threading-Simulator.git
```

### 2. Navigate into the folder:
```bash
cd Airport-Threading-Simulator
```

### 3. Install dependencies:
```bash
pip install pandas openpyxl
```

### 4. Run the simulation:
```bash
python semaphorProject.py
```

---

## 📊 Sample Output

```
Time:0 | flight-01 request to Houston controls and wait to response
Time:0 | flight-02 request to San Antonio controls and wait to response
Time:1 | flight-02 request accept by San Antonio control and fly from Houston to San Antonio
Time:1 | flight-01 request accept by Houston control and fly from Dallas to Houston
Time:2 | flight-12 request to Santa Fe controls and wait to response
...
All Flights done
```

---

## 📌 Rules & Constraints

1. Each airport has a **capacity limit** controlled by a semaphore.
2. Each flight is a **separate thread** and must wait for approval from the control tower.
3. Mutual exclusion is enforced between origin and destination airports.
4. If a flight cannot take off within **30 seconds**, it is reported as failed.
5. All data is loaded dynamically from the attached Excel file.

---

## 📜 License

This project was developed as part of a university Operating Systems course.  
Free to use for learning purposes.

---

## 👨‍💻 Author

**Fatemeh Paksima**
Operating Systems Course Project
