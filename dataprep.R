library(Hmisc)

setwd("c:/Users/alicia/Documents")
load("~/WV6_Data_rdata_v_2014_06_04/WV6_Data_rdata_v_2014_06_04.rdata")
head("WV6_Data_spss_v_2014_06_04",12)

#subset for trial
smaller<-subset(WV6_Data_spss_v_2014_06_04, select = c(V2:V9,V12:V23,V242,V238,V240,V245,V248,V250,V255))
smaller2<-subset(smaller,select=c(-V2A))

setwd("c:/Users/Alicia/PycharmProjects/WorldValues")
write.csv(smaller2, "answersonly.csv",row.names=FALSE)
