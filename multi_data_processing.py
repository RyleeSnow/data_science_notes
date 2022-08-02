import pandas as pd
import math
from multiprocessing import Pool, cpu_count


class FasterDataProcessing:
    def __init__(self,
                 df: pd.DataFrame = None,
                 chunk_size: int = 100000,
                 csv_raw: bool = False,
                 csv_file: str = None):
        self.df = df
        self.chunk_size = chunk_size
        self.csv_raw = csv_raw
        self.csv_file = csv_file
        self.n_cpu = cpu_count()
        self.n_chunks = None

    @staticmethod
    def df_processing(df_seg: pd.DataFrame) -> pd.DataFrame:
        df_seg["column_b"] = df_seg["column_a"] * 2
        return df_seg

    def process_by_batch(self, i):
        if self.csv_raw:

        else:
            self.n_chunks = math.ceil(len(self.df) / self.chunk_size)
            if self.n_chunks < self.n_cpu:
                self.chunk_size = math.ceil(len(self.df) / self.n_cpu)
            else:
                pass

        start = math.floor(self.chunk_size * i)
        if i < (self.n - 1):
            end = math.floor(self.chunk_size * (i + 1))
        else:
            end = math.floor(self.chunk_size * (i + 1)) + 1

        df_seg = self.df[start:end]
        df_seg = self.df_processing(df_seg)

        self.res.append(df_seg)

    def run_speedup_by_frag(self):

        p = Pool(self.n)
        for i in range(self.n):
            res.append(p.apply_async(self.speedup_by_frag, args=(i,)))
        p.close()
        p.join()
        for i in res:
            print(i.get())





if __name__ == '__main__':
    df_raw = pd.read_csv('example.csv')
    m = FasterDataProcessing(df=df_raw)
    table = m.run()




