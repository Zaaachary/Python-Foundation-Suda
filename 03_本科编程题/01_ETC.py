"""
01data.txt
ETC编号  FG-102-934
时间格式  2016-01-08#07:21:31
整条记录  BA-724-433|2016-01-08#07:21:31|2016-01-08#17:01:09
每行一个ETC
每辆车都是当天出入  日期相同

要求：
识别ETC 记录总条数
计算ETC中有多少辆不同的车  正则 or 切片
找出进出次数最多的5辆车
找出累计停留时间最长的5辆车
将计算结果输出到01report.txt
"""


def main():
    vehicle_lst = get_record("data.txt")			# 读文件，获取全部ETC记录，构成列表
    vehicle_set = get_v(vehicle_lst)				# 获取全部不同的ETC编号，构成集合
    fre_dict = count_v(vehicle_lst, vehicle_set)		# 构造车辆进出校园次数的字典
    inter_dict = count_t(vehicle_lst, vehicle_set)		# 构造车辆累计停留时间的字典
    write_to_file(vehicle_lst, fre_dict, inter_dict, "report.txt")	# 输出结果到文件中
    return


if __name__ == "__main__":
    main()
