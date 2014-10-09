library(Hmisc)

setwd("c:/Users/alicia.powers/Documents/MyProjects/WorldValues")
load("~/WV6_Data_rdata_v_2014_06_04/WV6_Data_rdata_v_2014_06_04.rdata")
head("WV6_Data_spss_v_2014_06_04",12)

#subset for trial
smaller<-subset(WV6_Data_spss_v_2014_06_04, select = c(V2:V9))
smaller2<-subset(smaller,select=c(-V2A))

write.csv(smaller2, "answers.csv",row.names=FALSE)