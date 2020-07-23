import glob
import io
import os
import time

import concurrent.futures

start = time.perf_counter()
cd = os.chdir('/storage/emulated/0/Download/')
cd = os.getcwd()

files = glob.glob(cd + "/*.csv")


def read_file(file):
    with io.open(file, "r", encoding="utf-8")as f1:
        data = f1.read()
        data = data.split("\n")[1:]
        data1 = "\n".join(row for row in data)
        with io.open("output.csv", "a", encoding="utf-8") as f2:
            f2.write(data1)
            f2.close()
        f1.close()


# ===============================================================================
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     output=executor.map(read_file,files)
# ===============================================================================
with concurrent.futures.ProcessPoolExecutor() as executor:
    output = executor.map(read_file, files)

# ===============================================================================
# for i in range(len(files)):
#     read_file(files[i])
end = time.perf_counter()
# ===============================================================================

print(f"time taken {round(end - start, 2)} seconds")
