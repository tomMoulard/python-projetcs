#!/usr/bin/env python3

import subprocess
import shutil # cp/mv files
import os.path # check file exist
import glob # ls *
import threading
import sys
import argparse

sem = threading.Semaphore()

class Compression():
    """Compression is a wrapper class of a compression algorithm"""

    def __init__(self, command, input_file, output_file, replace, temp=False):
        """Init the compress algorithm

        :command: The command to build the output file
        :input_file: Input file name
        :output_file: Output file name
        :replace: Does the command remove the input

        """
        self.command = command
        self._input_file = input_file
        self.output_file = output_file
        self._replace = replace
        self._output = ""
        self._execed = False
        self._temp = temp
        self.fs = 0
        self.return_code = 0

    def format_command(self, input_file):
        return self.command.format(input_file, self.output_file)

    def exe(self):
        self._execed = True
        if not os.path.isfile(self._input_file):
            raise FileNotFoundError(f"No such file or directory: '{self._input_file}'")
        if self._replace:
            shutil.copyfile(self._input_file, self._input_file+".bak")
        input_file = self._input_file
        if self._temp:
            sem.acquire()
            input_file = "temp.temp"
            shutil.copyfile(self._input_file, input_file)
        self._process = subprocess.Popen(
            [self.format_command(input_file)],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.return_code = self._process.wait()
        self.stdout, self.stderr = self._process.communicate()
        if self._temp:
            files = glob.glob("temp.temp.*")
            shutil.move(files[0], self.output_file)
            if not self._replace:
                os.remove("temp.temp")
            sem.release()
        self.fs = os.path.getsize(self.output_file)
        if self._replace:
            shutil.move(self._input_file+".bak", self._input_file)

    def __str__(self):
        if self._execed:
            c = self.command.split(' ')[0]
            return f"{c},'{self.output_file}',{self.fs},{self.return_code},"
        return f"The command '{self.format_command(self._input_file)}' has not been run yet"

def generate_compression(input_file):
    return [
                Compression("7z a -t7z {1} {0}", input_file, f"{input_file}.7z", False),
                Compression("bzip2 {}", input_file, f"{input_file}.bz2", True, temp=True),
                Compression("compress -f {}", input_file, f"{input_file}.Z", True, temp=True),
                Compression("lzma {}", input_file, f"{input_file}.lzma", True, temp=True),
                Compression("pack {} {}", input_file, f"{input_file}.packed", False),
                Compression("rar a -r {1} {0}", input_file, f"{input_file}.rar", False),
                Compression("tar cfz {1} {0}", input_file, f"{input_file}.tar", False),
                Compression("xz {0}", input_file, f"{input_file}.xz", True, temp=True),
                Compression("zip {1} {0}", input_file, f"{input_file}.zip", False),
            ]

def run(input_file, count):
    algos = generate_compression(input_file)
    for algo in algos:
        threading.Thread(algo.exe())
        print(algo)
        if count > 0:
            run(algo.output_file, count-1)
        os.remove(algo.output_file)

def create_parser():
    parser = argparse.ArgumentParser(description="Benchmark compressions algorithms")
    parser.add_argument("-f", "--file", help="Specify the input file name")
    parser.add_argument("-c", "--count", default=0,
            help="How deep is your recurtion")
    return parser

def main(argv):
    args = create_parser().parse_args(argv[1:])
    if not args.file:
        raise ValueError("No file provided, see --help")
    print("algo,command,file size,return code")
    run(args.file, count=int(args.count))

if __name__ == "__main__":
    main(sys.argv)
