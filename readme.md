##What the scripts do:

run_analysis.R  reads data from UCI HAR Dataset. It also writes feat.csv, tidy.txt, reads feature names from myfile.txt
The resulting tidy data is stored in tidy.txt

parse.py reads feat.csv and writes myfile.txt


##How to reproduce the tidying of the dataset:

1. Working directory is UCI HAR Dataset folder. It contains run_analysis.R, parse.py.
2. Feat.csv was written by R command: feat<-fread("features.txt");write.csv(feat$V2,"feat.csv")
3. parse.py was run in Python 2.7 to write myfile.txt
4. run_analysis.R  was run in R


==================================================================

The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. Each person performed six activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. The experiments have been video-recorded to label the data manually. The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data.

The sensor signals (accelerometer and gyroscope) were pre-processed by applying noise filters and then sampled in fixed-width sliding windows of 2.56 sec and 50% overlap (128 readings/window). The sensor acceleration signal, which has gravitational and body motion components, was separated using a Butterworth low-pass filter into body acceleration and gravity. The gravitational force is assumed to have only low frequency components, therefore a filter with 0.3 Hz cutoff frequency was used. From each window, a vector of features was obtained by calculating variables from the time and frequency domain. See 'features_info.txt' for more details.
