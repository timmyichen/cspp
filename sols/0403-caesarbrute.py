import caesar

message = "PMTTW NZWU BPM XIAB! BPMZM QA VWBPQVO BW AMM PMZM. EMTKWUM BW BPM EWZTL WN KZGXBWOZIXPG. BWBITTG NCV ABCNN!"

for x in range(26):
    print(caesar.decrypt(x,message))