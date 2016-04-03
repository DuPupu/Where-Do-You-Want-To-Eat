from random import choice
from time import sleep

def disp(strx):
	print("\n"*40+strx+"\n"*3)
disp('')
[ac1 , ac2 , ac3 , hmk , gc , df , yn , pl , mcd , tb] = ["AC1","AC2","AC3","Homey Kitchen","Garden Cafe","Deliferance","Yoshinoya","Pepper Lunch", "McDonald's", "3rd Bro"]
[allcan,acs,hall,fw,liba] = [[ac1,ac2,ac3,hmk,gc,df,yn,pl,mcd,tb], [ac1,ac2,ac3], [hmk,ac3,ac2], [yn,pl,mcd,tb], [ac1]]; liba.extend(fw)
reslist={'1':acs,'2':hall,'3':fw,'4':liba,'5':allcan}

print('======== WDYWTE? ========\n  1) AC Canteens \n  2) Hall \n  3) Festival Walk \n  4) Liba \n  5) ALL CANTEEN')
k=str(input('Where Do You Want To Eat? '))

if k in ['1','2','3','4','5']:
	for i in range(100):
		disp("Waiting... "+choice(reslist.get(k)))
		sleep(0.02)
	disp("Your Choice is: "+choice(reslist.get(k)))
else:
	disp("Unsuccessful, Please Retry by Using !!")

