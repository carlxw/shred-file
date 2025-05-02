import sys
import os
import random

from threading import Thread
from typing import List 
from io import BufferedRandom

NUM_THREADS = 8

def main():
    """
    argv[1] - File to destroy
    argv[2] - Directory to target, optional
    """
    args: List[str] = sys.argv
    
    if len(args) < 2:
        print("Expected at least one argument.")
        return

    filename: str = args[1]
    cwd = args[2] if len(args) > 2 else os.getcwd()

    destroy_contents(cwd, filename)

    return


def random_byte() -> bytes:
    """
    Generate a random byte by performing elementary
    bitwise operations and a random bit generator 
    """
    output: bytes = 0

    for i in range(8):
        bit = random.randint(0, 1)
        output |= (bit << i)

    return output.to_bytes(1, byteorder="big")


def destroy_contents(dir_uri: str, filename: str):
    """
    Completely destroy the file by overwriting all 
    file contents into a random sequence of bytes,
    effectively destroying the file contents and
    file attributes to an irrecoverable state 
    """
    print(f"Destroying {filename}...")
    try: 
        uri = os.path.join(dir_uri, filename)
        file_length = os.path.getsize(uri)
        start_point = 0
        partition_size = file_length // NUM_THREADS

        # Multithread the file shredding
        threads: List[Thread] = []
        for i in range(NUM_THREADS):
            # Ensure that all bytes are considered
            if i != NUM_THREADS - 1:
                end_point = start_point + partition_size
            else:
                end_point = file_length

            args = (uri, start_point, end_point,)

            thread = Thread(target=write_contents, args=args)
            threads.append(thread)    
            thread.start()

            start_point = end_point

        for thread in threads:
            thread.join()
    except IOError:
        print(f"Failed to open and modify {filename}")

    if delete_file(dir_uri, filename):
        print("File successfully deleted.")
    else:
        print(f"Failed to delete {filename}")

    return


def write_contents(uri: str, start: int, end: int):
    """
    Multithreaded function to subdivide the 
    random file writing into partitions
    """
    fp: BufferedRandom = open(uri, "rb+")
    fp.seek(start)

    for _ in range(start, end):
        byte = random_byte()
        fp.write(byte)

    fp.flush()
    fp.close()
    return


def delete_file(dir_uri: str, filename: str) -> bool:
    """
    Check for file existence and then proceed
    to delete it from the file system 

    Returning False means failure, True means success
    """
    if not os.path.exists(dir_uri):
        return False

    del_uri: str = os.path.join(dir_uri, filename)
    if os.path.exists(del_uri):
        os.remove(del_uri)
    else:
        return False

    return True


if __name__ == "__main__":
    main()
