import dynamo
import numpy as np
import dynamo as dyn
from utils import *


def test_save_rank_info(adata):
    dyn.save_rank_excel(adata)


if __name__ == "__main__":
    adata = gen_or_read_zebrafish_data()
    print(adata)
    test_save_rank_info(adata)
