import numpy as np
import os


def main():
    results_lists = sorted(os.listdir('./disorder_result_native_AA'))
    os.chdir('./disorder_result_native_AA')
    disorder_percentage=[]
    for result in results_lists:
        dat = np.loadtxt(result, delimiter=',', dtype='str')
        count=np.sum(dat[:, 2].astype(float) > 0.5) / len(dat)
        disorder_percentage.append(count)
    disorder_percentage=np.array(disorder_percentage)

    #(">30%:" + str(np.sum(disorder_percentage > 0.3) / len(disorder_percentage)))
    #print(">50%:" + str(np.sum(disorder_percentage > 0.5)/ len(disorder_percentage)))
    #print(">70%:" + str(np.sum(disorder_percentage > 0.7) / len(disorder_percentage)))
    #print(">90%:" + str(np.sum(disorder_percentage > 0.9) / len(disorder_percentage)))
    #print("=100%:" + str(np.sum(disorder_percentage == 1) / len(disorder_percentage)))


    np.savetxt('disorder_percentage_native_AA.csv',disorder_percentage,delimiter=',')

if __name__ == '__main__':
    main()