library(Hmisc)

setwd("c:/Users/alicia/Documents")
load("~/WV6_Data_rdata_v_2014_06_04/WV6_Data_rdata_v_2014_06_04.rdata")
head("WV6_Data_spss_v_2014_06_04",12)
setwd("c:/Users/Alicia/PycharmProjects/WorldValues")
countries<-read.csv("countriesonly.csv",header=T,stringsAsFactors=F)
countries["V2"]=countries["CountryID"]
countries<-subset(countries, select=c("V2","CountryName"))

#subset for trial
smaller<-subset(WV6_Data_spss_v_2014_06_04, select = c(V2:V9,V12:V23,V242,V238,V240,V245,V248,V250,V255,V144))
smaller1<-merge(smaller, countries, by="V2",all.x=TRUE)
smaller2<-subset(smaller1,select=c(-V2A))
smaller2["ID"]=row.names(smaller2)


smaller2$GenderName[smaller2$V240==1]<-"Male" 
smaller2$GenderName[smaller2$V240==2]="Female"
table(smaller2["GenderName"])
  
setwd("c:/Users/Alicia/PycharmProjects/WorldValues")

write.csv(smaller2, "answersonly.csv",row.names=FALSE)

