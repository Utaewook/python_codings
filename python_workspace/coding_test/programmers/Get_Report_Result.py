
def solution(id_list, report, k):
    answer=[]
    temp = []
    report_list = {}
    report_count = {}
    
    for i in range(len(id_list)):
        report_count[id_list[i]] = 0
    
    for i in range(len(report)):
        id, rep = report[i].split()
        if id in report_list:
            report_list[id].append(rep)
        else:
            report_list[id] = [rep]
            
    for iter in report_list.keys():
        for i in range(len(report_list[iter])):
            report_count[report_list[iter][i]] += 1
            
    for iter in report_count.keys():
        if report_count[iter] > k:
            temp.append = iter
            
    return answer