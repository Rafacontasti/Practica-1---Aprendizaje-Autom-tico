pd = open("pr1_disponibles_st1-98ns1_compressed", "r")
disp_df = pd.read_csv("disp_st23ns1.txt.bz2", compression="bz2",index_col=0)