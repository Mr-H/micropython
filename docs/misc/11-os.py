# Sample OS functions

Thonny does not allow you to delete files.  To do this you will need to use the "os" functions.

```python
import os
os.listdir()
os.remove('myfile')
os.listdir()
```

To find out all the os functions use:

```python
import os
print(dir(os))
``

Returns

```
['__class__', '__name__', 'remove', 'VfsFat', 'VfsLfs2', 'chdir', 'getcwd', 
'ilistdir', 'listdir', 'mkdir', 'mount', 'rename', 'rmdir', 'stat', 'statvfs', 
'umount', 'uname', 'urandom']`

## References

https://www.youtube.com/watch?v=jnSX8ZMmHZ4