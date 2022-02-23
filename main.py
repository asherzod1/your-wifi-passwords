import subprocess, re
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks = networks.decode("866")
network_names = re.findall("(?:пользователей\s*:\s)(.*)", networks)
for network_name in network_names:
    command = f'netsh wlan show profile {network_name} key=clear'
    current_result = subprocess.check_output(command, shell=True)
    current_result = current_result.decode("866")
    network_password = re.findall("(?:Содержимое ключа\s*:\s)(.*)", current_result)
    if network_password :
        print(f'WI-FI name:{network_name}\n password:{network_password[0]}')
    else:
        print(f'WI-FI name:{network_name}\n password:')