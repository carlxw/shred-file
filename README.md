Shred File
==========

This is a CLI tool used to truly destroy a file by rewriting it's binary contents and then deleting the file on the file system.

The motivation for this project is that on typical operating systems, "deleted" files aren't truly deleted on the hardware-level. They are merely "marked" and unaccessible, however, on the hardware itself, the file contents are still there until the hardware block is overwritten.

This project will re-write the file contents first into a random byte sequence to make its contents truly unrecoverable on a low-level.

## Adding To PATH

This is a CLI program with the intention to have the cloned directory be added to the system PATH. To do this:

```
Environment Variables > System Variables > PATH > (Add {...}/shred-file directory)
```

Which allows `shred-file` to be called anywhere. The Python file in theory works across all OS, however, this repository uses a `.bat` script to call the Python file for Windows only.

## Using This Program

This program takes the following CLI arguments:

```bash
shred-file fileName fileDirectory
```

| Argument | Description | Required? | 
| - | - | - |
| fileName | The name of the file to be destroyed | Yes |
| fileDirectory | The directory where the file resides. If null, defaults to the Python file cwd | No | 

Through the provided `.bat` script, obtaining `fileDirectory` is done through there.
