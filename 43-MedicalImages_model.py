"""
@author: Nelly Elsayed
This code is modified by Nelly Elsayed for GRU-FCN model implementation, based on the code published by Karim et al.
# which implemented LSTM-FCN model https://github.com/titu1994/LSTM-FCN
# Special thanks for the code availability
# Please cite our paper and Karim et al. paper in case of using our code.
# The MLP and FCN are implemented according to Wang et al. : Time series classification from scratch with deep neural networks: a strong baseline
"""

from keras.models import Model
from keras.layers import Input, PReLU, Dense, LSTM, multiply, concatenate, Activation, GRU, SimpleRNN, Masking, Reshape
from keras.layers import Flatten, Bidirectional,Conv1D, BatchNormalization, GlobalAveragePooling1D, Permute, Dropout, GlobalMaxPooling1D

from utils.constants import MAX_SEQUENCE_LENGTH_LIST, NB_CLASSES_LIST
from utils.keras_utils_1 import train_model, evaluate_model, set_trainable, visualize_context_vector, visualize_cam
from utils.layer_utils import AttentionLSTM

# For Graphs plotting and training time evaluation
import pylab as plt
import time

DATASET_INDEX = 43

MAX_SEQUENCE_LENGTH = MAX_SEQUENCE_LENGTH_LIST[DATASET_INDEX]
NB_CLASS = NB_CLASSES_LIST[DATASET_INDEX]

TRAINABLE = True



#The proposed GRU-FCN model code
#GRU-FCN model
def generate_GRU_FCN_model():
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
################################################################################
# same code LSTM-FCN model proposed by arim et al. paper in case of using our code
def generate_LSTM_FCN_model():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))

    x = LSTM(8)(ip)
    x = Dropout(0.8)(x)

    y = Permute((2, 1))(ip)
    y = Conv1D(128, 8, padding='same', kernel_initializer='he_uniform')(y)#128
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(256, 5, padding='same', kernel_initializer='he_uniform')(y)#256
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(128, 3, padding='same', kernel_initializer='he_uniform')(y)#128
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = GlobalAveragePooling1D()(y)#GlobalMaxPooling1D()(y)#

    x = concatenate([x, y])

    out = Dense(NB_CLASS, activation='softmax')(x)

    model = Model(ip, out)

    model.summary()

    # add load model code here to fine-tune

    return model

#ALSTM-FCN
def generate_ALSTM_FCN_model():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))

    x = AttentionLSTM(8)(ip)
    x = Dropout(0.8)(x)

    y = Permute((2, 1))(ip)
    y = Conv1D(128, 8, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(256, 5, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = Conv1D(128, 3, padding='same', kernel_initializer='he_uniform')(y)
    y = BatchNormalization()(y)
    y = Activation('relu')(y)

    y = GlobalAveragePooling1D()(y)

    x = concatenate([x, y])

    out = Dense(NB_CLASS, activation='softmax')(x)

    model = Model(ip, out)

    model.summary()

    # add load model code here to fine-tune

    return model

###############################################################################
    
def generate_MLP_model():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))
    
    y= Dropout(0.1)(ip)
    y = Flatten()(y)
    y = Dense(500, activation='relu')(y)
    y = Dropout(0.2)(y)
    y = Dense(500, activation='relu')(y)
    y = Dropout(0.2)(y)
    y = Dense(500, activation = 'relu')(y)
    y = Dropout(0.3)(y)
    out = Dense(NB_CLASS, activation='softmax')(y)
    model = Model(ip, out)
    model.summary()
    return model
###############################################################################
def generate_FCN_model():
    ip = Input(shape=(1, MAX_SEQUENCE_LENGTH))
  

    y = Permute((2, 1))(ip)
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

    out = Dense(NB_CLASS, activation='softmax')(y)

    model = Model(ip, out)

    model.summary()

    # add load model code here to fine-tune

    return model    
###############################################################################
if __name__ == "__main__":
    
    print("1- GRU-FCN model")
    print("2- LSTM-FCN model")
    print("3- ALSTM-FCN model")
    print("4- FCN model")
    print("5- MLP model")
    select = input("Enter which model you want to simulate: ")
    if select == '1':
        model = generate_GRU_FCN_model()
        start_time = time.time()
    elif select == '2':
        model = generate_LSTM_FCN_model()
        start_time = time.time()
    elif select == '3':
        model = generate_ALSTM_FCN_model()
        start_time = time.time()
    elif select == '4':
        model = generate_FCN_model()
        start_time = time.time()
    elif select == '5':
        model = generate_MLP_model() 
        start_time = time.time()

    history = train_model(model, DATASET_INDEX, dataset_prefix='medical_images', epochs=2000, batch_size=64)
    model.summary()
    accuracy, loss, f_score = evaluate_model(model, DATASET_INDEX, dataset_prefix='medical_images', batch_size=128)

    print("--- Run Time = %s seconds ---" % ((time.time() - start_time)))
    print("--- Run Time = %s minutes ---" % ((time.time() - start_time)/60.0))  
    text_file = open("training_time.txt", "w")
    text_file.write("--- Run Time ="+ str(((time.time() - start_time)))+" seconds ---"
                    +"\n" +"--- Run Time = "+str(((time.time() - start_time)/60.0))+" minutes ---"+"\n")
    print(history.history.keys())
    
    
    plt.plot(history.history['loss'])
    plt.xlabel('epoch', fontsize=16)
    plt.ylabel('loss',fontsize=16)
    plt.savefig("./resulted_plotes/train_loss.jpg")
    plt.show()
    
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.legend(['train', 'validation'], loc='upper right', fontsize ='large')

    plt.ylabel('loss',fontsize=16)
    plt.xlabel('epoch',fontsize=16)
    plt.savefig("./resulted_plotes/all_loss.jpg")
    plt.show()
    
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.xlabel('epoch',fontsize=16)
    plt.ylabel('accuracy',fontsize=16)
    plt.legend(['train', 'validation'], loc='lower right', fontsize ='large')
    plt.savefig("./resulted_plotes/_accuracy.jpg")
    plt.show()
    
    plt.plot(history.history['lr'])
    plt.xlabel('epoch', fontsize=16)
    plt.ylabel('learning rate',fontsize=16)
    plt.savefig("./resulted_plotes/learning_rate.jpg")
    plt.show()