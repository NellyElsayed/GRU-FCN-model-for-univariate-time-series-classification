# This code is modified by Nelly Elsayed for GRU-FCN model implementation, based on the code published by Karim et al.
# which implemented LSTM-FCN model https://github.com/titu1994/LSTM-FCN
# Special thanks for the code availability
# Please cite our paper and Karim et al. paper in case of using our code.
from keras.models import Model
from keras.layers import Input, PReLU, Dense, LSTM, multiply, concatenate, Activation, GRU, SimpleRNN, Masking, Reshape
from keras.layers import Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout, GlobalMaxPooling1D

from utils.constants import MAX_SEQUENCE_LENGTH_LIST, NB_CLASSES_LIST
from utils.keras_utils import train_model, evaluate_model, set_trainable, visualize_context_vector, visualize_cam
from utils.layer_utils import AttentionLSTM
from tensorflow.contrib.rnn import Conv1DLSTMCell

import time
start_time = time.time()
DATASET_INDEX = 0  # change the number according to which model you want to use

MAX_SEQUENCE_LENGTH = MAX_SEQUENCE_LENGTH_LIST[DATASET_INDEX]
NB_CLASS = NB_CLASSES_LIST[DATASET_INDEX]

TRAINABLE = True

def generate_model_5():
    inp = Input(shape=(1, MAX_SEQUENCE_LENGTH))

    #GRU_part
    x_r = GRU(8)(inp) # GRU with 8 unrollments
    x_r = Dropout(0.8)(x_r) # 80% dropout

    #Convolutional_part
    y = Permute((2, 1))(inp)
    y = Conv1D(128, 8, padding='same', kernel_initializer='he_uniform')(y)#128
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(256, 5, padding='same', kernel_initializer='he_uniform')(y)#256
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(128, 3, padding='same', kernel_initializer='he_uniform')(y)#128
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = GlobalAveragePooling1D()(y)

    x = concatenate([x_r, y])

    output = Dense(NB_CLASS, activation='softmax')(x)

    model = Model(inp, output)

    model.summary()


    return model

if __name__ == "__main__":

    # generate_ model
    model5 = generate_model_5()#
    print("GRU-FCN")
    history = train_model(model5, DATASET_INDEX, dataset_prefix='adiac', epochs=4000, batch_size=128)
    accuracy5, loss5 = evaluate_model(model5, DATASET_INDEX, dataset_prefix='adiac', batch_size=128)

    print("--- Run Time = %s seconds ---" % ((time.time() - start_time)))
    print("--- Run Time = %s minutes ---" % ((time.time() - start_time)/60.0))  
    text_file = open("training_time.txt", "w")
    text_file.write("--- Run Time ="+ str(((time.time() - start_time)))+" seconds ---"
                    +"\n" +"--- Run Time = "+str(((time.time() - start_time)/60.0))+" minutes ---"+"\n")
    print(history.history.keys())#dict_keys(['val_loss', 'val_acc', 'loss', 'acc', 'lr'])
    