import os,time

def rep(a,b,files):
    for i in range(0,len(files)):
        files[i]=files[i].replace(a,b)

def print_files(files):
    print("Files :")
    for i in files:
        print(i)
    print('\n')

def main():
    os.system("cls")
    while True:
        files=[]
        path="D:\\change\\code\\link related\\"
        for file in os.listdir(path):
            files.append(file)
        files.sort()
        copy_files=files.copy()
        print_files(files)
        rm=input("Do you want to remove any files from the list(0/1) :")
        try:
            rm=int(rm)
        except:
            rm=0
        if int(rm)==1:
            os.system("cls")
            for i in range(0,len(files)):
                print(str(i+1)+"."+str(files[i]))
            rmove=[]
            try:
                rmove = [int(x) for x in input("Remove :").split(",")]
            except:
                print("Invalid input")
            if len(rmove) > 0:
                for y in rmove:
                    if y > 0:
                        files.remove(copy_files[y-1])
            os.system("cls")
            print_files(files)
        else:
            os.system("cls")
            print_files(files)
        main_files=[]
        for i in files:
            main_files.append(i)
        if len(files) > 0:
            while True:
                st=input("Enter What to Replace (Enter to Continue to replace) :")
                st.strip()
                if st=="":
                    break
                tr=input("Replace it With :")
                if st!=tr:
                    if tr=="":
                        rep(st,"",files)
                    else:
                        rep(st,tr,files)
                    print_files(files)
            print_files(files)
            st=input("Continue :")
            try:
                st=int(st)
            except:
                st=0
            if st==1:
                if len(main_files)==len(files):
                    for i in range(0,len(files)):
                        print(main_files[i],"->",files[i])
                        os.rename(path+"\\"+main_files[i],path+"\\"+files[i])
            retry=input("Retry :")
            try:
                retry=int(retry)
            except:
                retry=-1
            if retry!=1:
                break
            else:
                os.system("cls")
        else:
            break


if __name__=="__main__":
    main()