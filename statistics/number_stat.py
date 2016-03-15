import os


def get_position_num(jobrootdir):
    job_num_map = {}
    for jobdir in os.listdir(jobrootdir):
        job_numer = 0
        if os.path.exists(jobrootdir + '/' + jobdir) is True and os.path.isdir(jobrootdir + '/' + jobdir) is True:
            for each_json in os.listdir(jobrootdir + '/' + jobdir):
                job_numer += len(each_json)
        job_num_map[jobdir] = job_numer

    return job_num_map


if __name__ == '__main__':
    my_map = get_position_num('H:/lagou')
    for item, value in my_map.items():
        print(item + ' : ' + str(value))
