from utils import *

def test_tuple_slice_get():
    dp_mat, nc_mat = rand_dp_nc_matrix(5, 5, seed=0)
    print(cmp_dp_nc_matrix(dp_mat[1:3, 0:2], nc_mat[0:2, 0:2]))

test_tuple_slice_get()