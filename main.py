import function.parse_log_1
import function.prepare_labels_2
import function.features_3
import function.train_semisup_4
import function.predict_semisup_5
import function.train_iforest_6
import time



print("======== Starting Model =============")
time.sleep(3)

print("======== Cleaning Log ===============")
function.parse_log_1.parser()
time.sleep(0.5)
print("======== Starting Phase Two =========")
function.prepare_labels_2.prepare()
time.sleep(0.5)

print("======== Sorting According Attack =======")
function.features_3.features()
time.sleep(0.5)
print("======== Training Model ================")
function.train_semisup_4.train()
print("======== Geting pattern ================== ")
function.predict_semisup_5.predict()
time.sleep(0.2)
print("==================Output csv Can be Found ===================")
function.train_iforest_6.iforest()

