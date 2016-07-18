import caesar

#message = "PMTTW NZWU BPM XIAB! BPMZM QA VWBPQVO BW AMM PMZM. EMTKWUM BW BPM EWZTL WN KZGXBWOZIXPG. BWBITTG NCV ABCNN!"
message = "YRJ REPFEV IVRCCP SVVE WRI RJ UVTZUVU KF LJV VMVE XF NREK KF UF CFFB DFIV CZBV"

for x in range(26):
    print("Key {}: {}".format(x,caesar.decrypt(x,message)))