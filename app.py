import time
import sys

print("Hello from ArgoCD deployed Python app!", flush=True)
print("Staying alive to avoid CrashLoopBackOff...", flush=True)

while True:
    time.sleep(60)
