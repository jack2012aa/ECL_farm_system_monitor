import general.general as general

'''
Bitwise masks
'''
CONNECTION_ERROR = 1
FILE_NUMBER_ERROR = 2

def connection_test(ip_list, monitor_status_flag):
    '''
    Check whether monitors are in connection by ping their ips. 用ping測試監視器是否斷線，結果會存在monitor_status_flag中。
    :param ip_list: a list of monitors' ip
    :param monitor_status_flag: a flag
    '''
    for ip in ip_list:
        #If any monitor isn't in connection, turn on the flag and return.
        if not general.mac_ping(ip):
            monitor_status_flag = monitor_status_flag | CONNECTION_ERROR
            return
        
    #If all of the monitors in connection but the flag is turn on, turn off the flag.
    if is_connection_error(monitor_status_flag):
        monitor_status_flag ^ CONNECTION_ERROR
        return

def is_connection_error(monitor_status_flag):
    return (monitor_status_flag & CONNECTION_ERROR) != 0

def recording_check(dir: str, num: int, monitor_status_flag):
    '''
    Check the number of files in a directory. 通過計算文件夾中的檔案數量是否符合預期檢查錄影狀況。
    :param dir: the directory of recording files
    :param num: assert number of file in the directory
    :param monitor_status_flag: a flag
    '''

    try:
        count = 0
        for path in general.os.listdir(dir):
            if general.os.path.isfile(general.os.path.join(dir, path)):
                count += 1
        if count != num:
            monitor_status_flag = monitor_status_flag | FILE_NUMBER_ERROR
    except:
        monitor_status_flag = monitor_status_flag | FILE_NUMBER_ERROR

def is_recording_error(monitor_status_flag):
    return (monitor_status_flag & FILE_NUMBER_ERROR) != 0