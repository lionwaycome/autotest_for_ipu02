import time
final_directory = "D:\\UDP_Autolibrary_Project\\Python\\logdata"

def writefile(filename,data):
    timename = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    pathfile = final_directory+"/"+filename+".txt"
    with open(pathfile,"a+") as f:
        f.write(filename+"_"+timename+">>> "+data)
    f.close
