import os
print('Exist:', os.access(r"C:\Users\User\projects\PP2-2024\lab6\dir-and-files", os.F_OK))
print('Readable:', os.access(r"C:\Users\User\projects\PP2-2024\lab6\dir-and-files", os.R_OK))
print('Writable:', os.access(r"C:\Users\User\projects\PP2-2024\lab6\dir-and-files", os.W_OK))
print('Executable:', os.access(r"C:\Users\User\projects\PP2-2024\lab6\dir-and-files", os.X_OK))