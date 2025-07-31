#!/usr/bin/env python3
import lgpio
import time
import random
from collections import deque

# ----- CONFIGURATION -----
h = lgpio.gpiochip_open(0)  # open gpiochip0

# Map each direction (1, 2, 3) to its red, yellow, and green LEDs.
PIN_MAP = {
    1: {'red': 2,  'yellow': 14, 'green': 3},
    2: {'red': 4,  'yellow': 15, 'green': 17},
    3: {'red': 27, 'yellow': 18, 'green': 22},
}

ALL_PINS = [p for d in PIN_MAP.values() for p in d.values()]

# Setup all pins as outputs and initialize to LOW
for pin in ALL_PINS:
    lgpio.gpio_claim_output(h, pin, 0)

def set_lights(active_dir):
    """
    Turn the green LED on for active_dir,
    and red LEDs on for all others.
    """
    for direction, pins in PIN_MAP.items():
        if direction == active_dir:
            lgpio.gpio_write(h, pins['green'], 1)
            lgpio.gpio_write(h, pins['yellow'], 0)
            lgpio.gpio_write(h, pins['red'], 0)
        else:
            lgpio.gpio_write(h, pins['green'], 0)
            lgpio.gpio_write(h, pins['yellow'], 0)
            lgpio.gpio_write(h, pins['red'], 1)

def transition_yellow(from_dir):
    """
    Briefly turn on yellow before switching from green to red.
    """
    pins = PIN_MAP[from_dir]
    lgpio.gpio_write(h, pins['green'], 0)
    lgpio.gpio_write(h, pins['yellow'], 1)
    time.sleep(0.5)
    lgpio.gpio_write(h, pins['yellow'], 0)
    lgpio.gpio_write(h, pins['red'], 1)

def clear_all():
    """Turn off all LEDs."""
    for pin in ALL_PINS:
        lgpio.gpio_write(h, pin, 0)

def cycle_queues():
    """
    Generate three random queues of 1–20 cars each,
    serve in descending order of size, 10 at a time.
    """
    while True:
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)
        n3 = random.randint(1, 20)

        q1 = deque([1]*n1)
        q2 = deque([1]*n2)
        q3 = deque([1]*n3)

        order = sorted([(1, n1), (2, n2), (3, n3)], key=lambda x: x[1], reverse=True)
        queue_order = deque([d for d, _ in order])

        print(f"Starting cycle with queues: D1={n1}, D2={n2}, D3={n3}")
        prev_dir = None

        while q1 or q2 or q3:
            dir_id = queue_order.popleft()
            q = {1: q1, 2: q2, 3: q3}[dir_id]

            if prev_dir is not None and prev_dir != dir_id:
                transition_yellow(prev_dir)

            set_lights(dir_id)
            prev_dir = dir_id

            served = 0
            for _ in range(10):
                if not q:
                    break
                q.popleft()
                served += 1
                print(f"  Dir{dir_id}: served car #{served}")
                time.sleep(0.3)  # reduced delay for faster simulation

            if q:
                queue_order.append(dir_id)

        print("=== CYCLE COMPLETE, restarting ===\n")
        clear_all()
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        cycle_queues()
    except KeyboardInterrupt:
        pass
    finally:
        clear_all()
        lgpio.gpiochip_close(h)
