#----------------- NOMOR 1-------------------------
# Data skor daya tahan (endurance scores)
scores <- c(93.6, 89.1, 97.7, 84.4, 97.8, 94.5, 88.3, 97.3, 94.7, 85.5, 82.6)

# Median yang dibandingkan
median_test <- 97.5

# Menghitung tanda (+ atau -)
positive_signs <- sum(scores > median_test)
negative_signs <- sum(scores < median_test)

# Melakukan uji binomial untuk tanda negatif
binom.test(negative_signs, length(scores), p = 0.5, alternative = "less")
#data:  negative_signs and length(scores)

#number of successes = 9, number of trials = 11, p-value = 0.9941
#alternative hypothesis: true probability of success is less than 0.5
#95 percent confidence interval:
#  0.0000000 0.9666808
#sample estimates:
#  probability of success 
#0.8181818 

#--------- NOMOR 2 ---------------
# Data berat tubuh
weights <- c(188.0, 211.2, 170.8, 212.4, 156.9, 223.1, 235.9, 183.9, 214.4, 221.0, 162.0, 222.8, 174.1, 210.3, 195.2)

# Median yang dibandingkan
median_test <- 163.5

# Menghitung tanda (+ atau -)
positive_signs <- sum(weights > median_test)
negative_signs <- sum(weights < median_test)

# Melakukan uji binomial untuk tanda positif
binom.test(positive_signs, length(weights), p = 0.5, alternative = "greater")

#data:  positive_signs and length(weights)
#number of successes = 13, number of trials = 15, p-value = 0.003693
#alternative hypothesis: true probability of success is greater than 0.5
#95 percent confidence interval:
#  0.6365582 1.0000000
#sample estimates:
#  probability of success 
#0.8666667 

#----------- NOMOR 3 ------------
# Data median usia lampu pijar
median_data <- c(1100, 1280, 1460, 1350, 1060, 1250, 1440, 1230, 
                 1630, 2100, 1830, 720, 730, 2080, 1550, 1140, 
                 1210, 1620, 1130, 1240, 1560, 1390, 1160, 1560, 
                 1300, 1260, 1560, 1560, 1300, 1600, 1260, 1140)

# Mengubah data menjadi format simbol + dan -
runs_test_data <- ifelse(median_data > 1435, 1, 0)

# Melakukan uji runs menggunakan package lawstat
install.packages("lawstat")
library(lawstat)

# Uji runs
runs.test(runs_test_data)


#------------- NOMOR 5---------------
# Data patukan burung eksperimental
eksperimental <- c(0, 0, 0, 2, 17, 58, 67, 68, 74, 79, 95, 98, 95, 107, 150, 181)

# Data patukan burung kontrol
kontrol <- c(0, 0, 0, 8, 8, 13, 20, 33, 33, 34, 35, 50, 57, 60, 74)

# Menggabungkan kedua data
combined <- c(eksperimental, kontrol)

# Hitung median gabungan
median_combined <- median(combined)

# Jumlah nilai di atas dan di bawah median untuk setiap kelompok
above_median_exp <- sum(eksperimental > median_combined)
below_median_exp <- sum(eksperimental <= median_combined)

above_median_ctrl <- sum(kontrol > median_combined)
below_median_ctrl <- sum(kontrol <= median_combined)

# Buat tabel kontingensi
contingency_table <- matrix(c(above_median_exp, below_median_exp, 
                              above_median_ctrl, below_median_ctrl), 
                            nrow = 2, byrow = TRUE)

# Lakukan uji chi-square pada tabel kontingensi
chisq.test(contingency_table)

#Pearson's Chi-squared test with Yates' continuity correction
#data:  contingency_table
#X-squared = 3.9343, df = 1, p-value = 0.04731


#----------------- NOMOR 6----------------
# Data frekuensi belanja online
online <- c(5, 1, 10, 3, 6, 3, 6, 3, 4, 9, 10)

# Data frekuensi belanja offline
offline <- c(3, 2, 10, 3, 3, 2, 3)

# Menggabungkan kedua data
combined <- c(online, offline)

# Hitung median gabungan
median_combined <- median(combined)

# Jumlah nilai di atas dan di bawah median untuk setiap kelompok
above_median_online <- sum(online > median_combined)
below_median_online <- sum(online <= median_combined)

above_median_offline <- sum(offline > median_combined)
below_median_offline <- sum(offline <= median_combined)

# Buat tabel kontingensi
contingency_table6 <- matrix(c(above_median_online, below_median_online, 
                              above_median_offline, below_median_offline), 
                            nrow = 2, byrow = TRUE)

# Lakukan uji chi-square pada tabel kontingensi
chisq.test(contingency_table6)
#Pearson's Chi-squared test with Yates' continuity correction

#data:  contingency_table6
#X-squared = 2.4575, df = 1, p-value = 0.117

# CHI SQUARE
table1=matrix(c(84,132,16,18),ncol=2)
colnames(table1)=c("Berkecambah","Tidak Berkecambah")
rownames(table1)=c("Perlakuan","Tanpa Perlakuan")
table1
Uji=chisq.test(table1)

# BARTLETT
#Setting Directory
setwd("D:/UNAIR/1. Perkuliahan/Statnonpar/2023-2024/M4")
#Import Data
library(readxl)
Data <- read_excel("Data.xlsx")
View(Data)
library(mvtnorm)
Uji1=bartlett.test(Diameter~Batch,data=Data)
Uji1
Uji

# LEVENE
#Setting Directory
setwd("D:/UNAIR/1. Perkuliahan/Statnonpar/2023-2024/M4")
#Import Data
library(readxl)
Data <- read_excel("Data.xlsx")
View(Data)
library(misty)
Uji2=test.levene(Diameter~Batch,data=Data,method = "mean", conf.level = 0.95)
Uji2

# 

