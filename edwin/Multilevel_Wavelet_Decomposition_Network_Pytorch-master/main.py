from load_data import load_data
from model import Wavelet_LSTM
from train import train,test
import numpy as np

def main():
    data_path = "./Data/POWER-DATA.csv"
    P = 8  #sequence length
    step = 4 #ahead predict steps

    X_train,Y_train,X_test,Y_test,data_df_combined_clean = load_data(data_path,P=P,step=step)
    print(X_train.shape)
    print(Y_train.shape)
    
    model = Wavelet_LSTM(P,8,1)
    model = model.double()
    train(model,X_train,Y_train,epochs=1)
    test(model,X_test,Y_test,data_df_combined_clean)


if __name__ == "__main__":
    main()