import subprocess
import time
import socket

ssid='example'
REMOTE_SERVER = "one.one.one.one"

def is_connected(hostname):
    """
    Check if the host is connected to the network by resolving the hostname and establishing a connection.
    Returns True if connected, False otherwise.
    """
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except socket.error:
        return False

def wifi_connected(ssid):
    """
    Check if the Wi-Fi network with the specified SSID is connected.
    Returns True if connected, False otherwise.
    """
    output = subprocess.check_output("netsh wlan show interfaces").decode('utf-8')
    return ssid in output

try:
    while True:
        # Retrieve WARP status
        warp_status = subprocess.check_output('warp-cli status').decode('utf-8')
        
        if wifi_connected(ssid) and is_connected(REMOTE_SERVER):
            if 'Disconnected' in warp_status:
                # Connect to Nittewifi and enable WARP if currently disconnected
                print('Connected to Nittewifi! Connecting WARP...')
                subprocess.run(['warp-cli', 'connect'])
        elif 'Connected' in warp_status:
            # Disconnect WARP if not connected to Nittewifi
            print('Not connected to Nittewifi! Disconnecting WARP...')
            subprocess.run(['warp-cli', 'disconnect'])
        time.sleep(300)

except KeyboardInterrupt:
    print('Program stopped by user.')

except Exception as e:
    print('Error:', str(e))
