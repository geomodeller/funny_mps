import sklearn as sk
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'MPSlib\\scikit-mps')
import mpslib as mps



if __name__ == '__main__':
    TI, TI_filename=mps.trainingimages.strebelle()
    plt.imshow(TI.squeeze()[:,::-1].T)
    plt.show()

    # define global parameters such as facies ratio, number of realizations, random seed, etc.
    
    # define the training image size and template size

    # extract the training image to make a tabular form data

    # train some ML model the above tabular data

    # generate model 