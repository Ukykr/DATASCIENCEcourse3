require(data.table)
require(dplyr)
require(tidyr)


feat<-fread("features.txt")
names(feat)[2]<-"feature"
write.csv(feat$feature,"feat.csv")

#cat("Press [enter] in console to continue")  #optional:you can rerun the python script and then resume this script

line <- readline()

act<-fread("activity_labels.txt")
names(act)[2]<-"action"
setwd("train")
sub0<-fread("subject_train.txt")
t0<-fread("X_train.txt")
t00<-fread("y_train.txt")
setwd("..")
setwd("test")
sub1<-fread("subject_test.txt")
t01<-fread("y_test.txt")
t1<-fread("X_test.txt")
setwd("..")
data0<--bind_rows(t0,t1)   
t1$action<-t01
t0$action<-t00
t1$subject<-sub1
t0$subject<-sub0
t1$asource<-"testing"
t0$asource<-"training"
data1<-bind_rows(t0,t1)                                 #step1                                    
subset0<-grepl("mean()",feat$feature,fixed=T)
subset1<-grepl("std()",feat$feature,fixed=T)
logic0<-subset1|subset0
pos0<-which(logic0==TRUE)
pos1<-c(pos0,562,563,564)
data02<-select(data0,pos0)                                #step2
data2<-select(data1,pos1)  
data3<-mutate(data2, action=act$action[action])            #step3
f<-file("myfile.txt")
featurenames<-readLines(f)

names(data3)<-c(featurenames,"action","subject","asource")       #step4 

info<-data3 %>%
        select(subject ,asource ) %>%
                unique(by='subject')#%>%#print
data4<-data3%>%
        select(-asource, -action)
summary01<-data4%>% group_by(subject) %>% summarise_each(funs(mean))    #means by subject
data5<-data3%>%
        select(-asource, -subject)

summary02<-data5%>% group_by(action) %>% summarise_each(funs(mean))     #means by activity
summary01$action<-NA
summary01<-merge(summary01, info, by = "subject")
summary02$subject<-NA
summary02$asource<-NA
summary1<-bind_rows(summary01,summary02)
summary2<-summary1[,c(1,69,68,2:67)]
names(summary2)<-sapply(names(summary2),paste,".mean",sep="")
names(summary2)[names(summary2)=='subject.mean']<-"by.subject"
names(summary2)[names(summary2)=='action.mean']<-"by.activity"
names(summary2)[names(summary2)=="asource.mean"]<-"source"
write.table(summary2,file="tidy.txt",row.name=FALSE)                           #step5
closeAllConnections()


