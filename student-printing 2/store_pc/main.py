#!/usr/bin/env python3
import time

def main():
    print("Store PC agent started. Monitoring print jobs...")
    try:
        while True:
            # Placeholder: poll for jobs or watch a folder
            time.sleep(5)
            print("Heartbeat: agent running")
    except KeyboardInterrupt:
        print("Shutting down agent.")

if __name__ == '__main__':
    main()
