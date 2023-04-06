import shutil

path = "/home/trapsat/Desktop"
path2 = "/home/trapsat/Desktop/Janus_Photos"
stat = shutil.disk_usage(path).free
stat2 = shutil.disk_usage(path2).free
print(stat)
print(stat2)