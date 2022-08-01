import pandas as pd
import math
from multiprocessing import Pool, cpu_count


class FasterDataProcessing:
    def __init__(self, df, n=cpu_count()):
        self.df = df
        self.n = n

    @staticmethod
    def df_processing(df_seg: pd.DataFrame) -> pd.DataFrame:
        df_seg["column_b"] = df_seg["column_a"] * 2
        return df_seg

    def run_speedup_by_frag(self):
        res = []
        p = Pool(self.n)
        for i in range(self.n):
            res.append(p.apply_async(self.speedup_by_frag, args=(i,)))
            print(str(i) + ' processor started !')
        p.close()
        p.join()
        for i in res:
            print(i.get())

    def speedup_by_frag(self, i):
        interval = math.ceil(len(self.df) / self.n)

        start = math.floor(interval * i)
        if i < (self.n - 1):
            end = math.floor(interval * (i + 1))
        else:
            end = math.floor(interval * (i + 1)) + 1

        df_seg = self.df[start:end]
        return df_seg

    def speedup_by_split_file(self, i):
        df_seg_save = self.speedup_by_frag(i)
        df_seg_save.to_csv('temp_' + str(i) + '.csv', index=False)
        del df_seg_save



        interval = math.ceil(len(self.df) / self.n)

        start = math.floor(interval * i)
        if i < (self.n - 1):
            end = math.floor(interval * (i + 1))
        else:
            end = math.floor(interval * (i + 1)) + 1

        df_seg = self.df[start:end]
        return df_seg



if __name__ == '__main__':
    df_raw = pd.read_csv('example.csv')
    m = MultiDataProcessing(df=df_raw)
    table = m.run()




