# Benchmark

A tool to build benchmark on compression algorithms

This tool create a csv file with file size like:
```csv
algo,command,file size,return code
7z,'test.txt.7z',158,0,
bzip2,'test.txt.bz2',80,0,
compress,'test.txt.Z',35,0,
lzma,'test.txt.lzma',55,0,
pack,'test.txt.packed',40,0,
rar,'test.txt.rar',106,0,
tar,'test.txt.tar',151,0,
xz,'test.txt.xz',88,0,
zip,'test.txt.zip',198,0,
```

This tool can be used to find out which compression algorithm to use for your file type.
And if you need to chain algorithms in order to reduce your output file size

## Usage
```bash
make
```
