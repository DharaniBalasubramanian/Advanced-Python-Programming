import re
from collections import Counter
from datetime import datetime


def parse_log_file(file_path):
    log_entries = []
    
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}) (.+)')
    
    
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                timestamp_str, severity, ip, message = match.groups()
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                log_entries.append({
                    'timestamp': timestamp,
                    'severity': severity,
                    'ip': ip,
                    'message': message
                })
    
    return log_entries

def summarize_logs(log_entries):
    error_count = 0
    warning_count = 0
    ip_counter = Counter()

    for entry in log_entries:
        if entry['severity'] == 'ERROR':
            error_count += 1
        elif entry['severity'] == 'WARNING':
            warning_count += 1
        ip_counter[entry['ip']] += 1

    most_common_ips = ip_counter.most_common(3)
    
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")
    print("Most Frequent IP Addresses:")
    for ip, count in most_common_ips:
        print(f"{ip}: {count} occurrences")

def filter_logs(log_entries, start_date=None, end_date=None, severity=None):
    filtered_logs = log_entries
    
    if start_date:
        filtered_logs = [log for log in filtered_logs if log['timestamp'] >= start_date]
    if end_date:
        filtered_logs = [log for log in filtered_logs if log['timestamp'] <= end_date]
    if severity:
        filtered_logs = [log for log in filtered_logs if log['severity'] == severity]
    
    return filtered_logs

def analyze_log_file(file_path):
    log_entries = parse_log_file(file_path)
    summarize_logs(log_entries)
    
    start_date = datetime(2024, 9, 30, 12, 34, 0)
    end_date = datetime(2024, 9, 30, 12, 35, 0)
    filtered_logs = filter_logs(log_entries, start_date=start_date, end_date=end_date, severity='ERROR')
    
    print("\nFiltered Logs (Errors between 12:30 and 12:34):")
    for log in filtered_logs:
        print(f"{log['timestamp']} - {log['severity']} - {log['ip']} - {log['message']}")


analyze_log_file('server_log.txt')
