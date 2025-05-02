Shred File
==========

A CLI tool to truly destroy a file by rewriting it's binary contents and then deleting the file on the file system.

The motivation for this project is that on typical operating systems, "deleted" files aren't truly deleted on the hardware-level.

This project will re-write the file contents first into a random/specific binary sequence to make its contents truly unrecoverable, such that even one with strong hardware knowledge cannot recover the file contents.

