from subprocess import call
def send_request(mc):
    [call(f"dbus-send --print-reply --system --dest=org.bluez /org/bluez/hci0/dev_{mc} org.bluez.MediaControl1.VolumeUp",shell=True) for i in range(4)]
    return "Successful."
def switch_colon_to_underscore(y):
	return "".join(map(str,[(x if x!=":" else "_") for x in y]))
	
    
#SETUP YOUR ROOT PASSWORD AND MAC ADDRESS OF YOUR DEVICE HERE
#--------------------------------------------------
pwd = "Your Password"
mac = "Your mac address" #format as AA:BB:CC:DD:EE:FF
#--------------------------------------------------


mac2 = switch_colon_to_underscore(mac)
cmd = "sudo /etc/init.d/bluetooth restart"
call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
call(f"bluetoothctl connect {mac}",shell=True)
print(send_request(mac2))

