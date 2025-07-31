# 🚦 Smart Traffic Light System using Python & GPIO

A dynamic, intelligent traffic light simulation built in Python that uses **LGPIO** on Raspberry Pi to manage traffic flow based on **randomized vehicle queues**. Designed to mimic real-world traffic lights with red, yellow, and green phases and serve cars in an **adaptive, priority-based order**.

---

## 🎬 Demo

👉 [Watch the demo video here](#)  
<!-- Replace '#' with the actual YouTube or video link -->

---

## 👨‍💻 Developed By

This project was developed by:

- **Anshul Dewangan**
- **Pratyaksh Lodhi**
- **Aaron David Don**
- **Joshua Benchamin**

---

## 🧠 How It Works

- Each of the **3 directions** has a traffic light setup (Red, Yellow, Green).
- The system generates **random queues** of 1–20 cars per direction.
- Directions are **prioritized dynamically** based on the largest queue.
- Up to **10 cars** are served per phase.
- Transitions simulate **realistic yellow-light switching**.
- Uses **GPIO pins** for actual hardware interfacing on a Raspberry Pi.

---

## 🚦 Features

✅ Simulates adaptive traffic light logic  
✅ Hardware interfacing via GPIO  
✅ Real-time LED control for each direction  
✅ Console logs show served vehicles  
✅ Graceful shutdown with Ctrl+C  
✅ Randomized queue generation for dynamic simulation

---

## 🔧 Hardware Requirements

- Raspberry Pi with GPIO access  
- 9 LEDs (3 per direction: Red, Yellow, Green)  
- Resistors (220Ω recommended)  
- Breadboard and jumper wires

---

## 🛠️ Software Requirements

- Python 3.x
- [`lgpio`](https://abyz.me.uk/lg/lgpio.html) library for Raspberry Pi GPIO access

### 📦 Installation

```bash
sudo apt install lgpio
