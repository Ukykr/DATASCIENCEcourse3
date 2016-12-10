import re
with open("feat.csv") as f:
    s=f.readlines()
    #print s
    new="mean(): Mean value :0,std(): Standard deviation :0,mad(): Median absolute deviation :0,max(): Largest value in array :0,min(): Smallest value in array :0,sma(): Signal magnitude area :0,energy(): Energy measure. Sum of the squares divided by the number of values.:2,iqr(): Interquartile range :0,entropy(): Signal entropy :1,arCoeff(): Autorregresion coefficients with Burg order equal to 4 :1,correlation(): correlation coefficient between two signals :1,maxinds: index of the frequency component with largest magnitude :1,skewness(): skewness :1,kurtosis(): kurtosis :1,angle: Angle between two vectors :3"
    extra="meanFreq(): Weighted average of the frequency components to obtain a mean frequency :0,bandsEnergy(): Energy of a frequency interval within the 64 bins of the FFT of each window :1,mag: by magnitude,gravityMean:		 average gravity acceleration in signal window sample-time domain signal :0,tBodyAccMean:		average linear acceleration of the body in signal window sample-time domain signal :0,tBodyAccJerkMean:	average linear jerk of the body in signal window sample-time domain signal :0,tBodyGyroMean:		average angular acceleration of the body in signal window sample-time domain signal :0,tBodyGyroJerkMean:	average angular jerk of the body in signal window sample-time domain signal :0"
    dict={}
    units={}
    for i in range(0,15):
        feat=new.split(",")[i].split(":")[0].lower().strip()
        desc=new.split(",")[i].split(":")[1].strip().lower()+":"
        dict[feat]=desc
    xdict={}
    for i in range(0,8):
        feat=extra.split(",")[i].split(":")[0].lower().strip()
        desc=extra.split(",")[i].split(":")[1].strip().lower()
        xdict[feat]=desc
    code=[]
    parse1=[]
    j=-1
    for aline in s:
        j+=1
        if j==0:continue
        include=0
        feature=aline.split(",",1)[1].lower()
        myitem1=[]
        try:
            feature.index("mean()")
        except:
            pass
        else:
            include=1
        try:
            feature.index("std()")
        except:
            pass
        else:
            include=1
        for key, value in xdict.iteritems():
            matches=[m.start() for m in re.finditer(key, feature)]
            if len(matches)>0:
                for match in matches:
                    myitem1.append(value)
                    if key=="meanfreq()":
                        feature="!"+feature.replace(key,'',1).strip()
                    else:
                        feature=feature.replace(key,"!", 1).strip()
                        #print feature
        myitem2=[]
        for key,value in dict.iteritems():
                matches = [m.start() for m in re.finditer(key, feature)]
                if len(matches)>0:
                    if len(matches)>0:
                        for match in matches:
                            myitem2.append(value)
                            feature="@"+feature.replace(key,'',1).strip()
                            #print feature
        temp=feature
        #print temp
        temp=temp.replace("t","#",1).replace("f","~",1).replace('gyrojerk','<').replace("accjerk",">").replace("acc","%").replace("body","&").replace("gravity","*").replace("gyro","?")
        temp=temp.replace("x","on the x axis of the phone ").replace("y","on the y axis of the phone ").replace("z","on the z axis of the phone ")
        temp=temp.replace("#","time domain signal:").replace("~","frequency domain signal:").replace("<","angular acceleration " ).replace("?","angular velocity ").replace("%","linear acceleration ").replace(">","linear jerk ")
        temp=temp.replace("&",' of the body ').replace("*",'of gravity ')
        #print temp
        if len(myitem1)>0:
            for item1 in myitem1:
                temp=temp.replace("!",item1,1)
        if len(myitem2)>0:
            for item2 in myitem2:
                temp=temp.replace("@",item2,1)
        temp=re.sub(r'-+', '-', temp)
        temp=temp.replace('"','').replace("\."," ").strip().rstrip('-')
        #print temp
        #parse.append(temp)
        feature=aline.split(",",1)[1].strip()+" - "+temp
        #print unit

        if include==1:
            code.append(feature)
            parse1.append(temp)
    #print len(parse)
with open('variables.txt','w') as w:
    w.write ("labels, description of variables used the tidy dataset\n")
    for line in code:
        myline=line+"\n"
        w.write(myline)

with open('myfile.txt','w') as w:
    for line in parse1:
        #print line
        myline=line.replace(',','_').replace('-','').replace(':','').replace('(','_').replace(')','_').replace(' ','.').strip()+"\n"
        w.write(myline)
