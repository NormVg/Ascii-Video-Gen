import os

ll = [
    "/home/vishnu/Downloads/71a6f737403d7a81096d190a80195525.mp4",
    "/home/vishnu/Downloads/515b007db5b6ce49a05b11aef21ceff0.mp4",
    "/home/vishnu/Downloads/bb6f151e6674c8b9ceb98e91bb47fa5e.mp4",
    "/home/vishnu/Downloads/df1ced3c1e40f964b63a98b70093c58d.mp4",
    "/home/vishnu/Downloads/f42a916c5b0e811b38164e3a30fafa9c.mp4",
]

for i in ll:
    open("file.txt","w").write(i)
    os.system("python multi-run.py")