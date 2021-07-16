import os,time

def rep(a,b):
    for i in range(0,len(files)):
        files[i]=files[i].replace(a,b)

def print_files():
    for i in files:
        print(i)

os.system("cls")
while True:
    global files
    files=[]
    path=""
    for file in os.listdir(path):
        files.append(file)
    files.sort()
    copy_files=files.copy()
    print_files()
    rm=input("Do you want to remove any files from the list:")
    try:
        rm=int(rm)
    except:
        rm=0
    if int(rm)==1:
        os.system("cls")
        for i in range(0,len(files)):
            print(str(i+1)+"."+str(files[i]))
        rmove = [int(x) for x in input("Remove: ").split(",")]
        if len(rmove) > 0:
            for y in rmove:
                if y > 0:
                    files.remove(copy_files[y-1])
        os.system("cls")
        print_files()
    else:
        os.system("cls")
        print_files()
    main_files=[]
    for i in files:
        main_files.append(i)
    if len(files) > 0:
        while True:
            st=input("Enter What to Replace :")
            st.strip()
            if st=="":
                break
            tr=input("Replace it With :")
            if st!=tr:
                if tr=="":
                    rep(st,"")
                else:
                    rep(st,tr)
                print_files()
        print_files()
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
    