
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
def solution(id_list, report, k):
    answer = []
    dict_a = dict() #�ǽŰ��� : �Ű���
    dict_b = dict() #�ǽŰ��� : �Ű� Ƚ��
    dict_c = dict() #��� : ���� ���� Ƚ��
    double = list() #�Ű� ����
    freeze =[]      #�������ѻ��
    for i in report:
        if i not in double: # ���� �Ű� �ߺ� üũ
            s_i = i.split()
            if s_i[0] not in freeze:
                dict_a[s_i[1]] += [s_i[0]]
                dict_b[s_i[1]] += 1
                double += [i]
                if dict_b[s_i[1]] >=k:
                    freeze += [s_i[0]]
                    for j in dict_a[s_i[1]]:
                        dict_c[j] +=1
        else:
            continue
        for i in id_list:
            if not dict_c[i]:
                dict_c[i] = 0
            answer += [dict_c[i]]
    return answer