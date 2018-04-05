import datetime
# import msvcrt
import os
import subprocess
import threading
import time

class Global:
    buffer_size = 10
    folder = datetime.datetime.fromtimestamp(time.time()).strftime("%Y_%m_%d_%H_%M_%S")

def logging_thread_func(device, type):
    try:
        filePath = Global.folder + "\\" + device + "-" + type + ".log"
        print("Start recording " + type + " log, path=" + filePath)
        output = open(filePath, "w+")
        subprocess.call("adb -s " + device + " logcat -v time -b " + type, stdout=output, bufsize=Global.buffer_size)
        output.close
        print("Stop recording " + type + " log")
    except:
        handle_exception()

def get_devices():
    devices = []
    adb_output = subprocess.check_output(["adb", "devices"])
    output_list = adb_output.decode("utf-8").split("\r\n")
    for i in range(1, len(output_list), 1):
        split_data = output_list[i].split()
        if len(split_data) > 0:
            devices.append(split_data[0])
    return devices

def handle_exception():
    print("exception occur..." + traceback.format_exc())
    a, b, c = sys.exc_info()
    logger.e(a)
    logger.e(b)
    logger.e(c)

    print("\npress any key to exist")
    msvcrt.getch()

def main():
    try:
        print("connecting to the device...")
        subprocess.call("adb wait-for-device")

        devices = get_devices()
        for device in devices:
            print("device [" + device + "] is connected")

        directory = os.path.dirname(Global.folder + "\\text.txt")
        if not os.path.exists(directory):
            os.makedirs(directory)

        print("")
        threads = [];
        for device in devices:
            threads.append(threading.Thread(target=logging_thread_func, args=(device, "main")))
            threads.append(threading.Thread(target=logging_thread_func, args=(device, "radio")))
            threads.append(threading.Thread(target=logging_thread_func, args=(device, "events")))
            threads.append(threading.Thread(target=logging_thread_func, args=(device, "system")))
            threads.append(threading.Thread(target=logging_thread_func, args=(device, "crash")))

        for thread in threads:
            thread.start()

        time.sleep(1)
        print("\nPress \"Ctrl + C\" to stop recording")

        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        time.sleep(1)
        print("\nshutdown by user")
    except:
        handle_exception()

if __name__ == "__main__":
    main()
