from Testing import testCarData, testPenData, average, stDeviation


def Q5(hiddenLayers=None):
    if hiddenLayers is None:
        hiddenLayers = [[24], [16]]

    iterations = 5

    penAccuracy = []
    carAccuracy = []
    for i in range(iterations):
        penAccuracy.append(testPenData(hiddenLayers[0])[1])
        carAccuracy.append(testCarData(hiddenLayers[1])[1])

    print('---------------------------------------')
    print(f'Pen Accuracy Data ({hiddenLayers[0]} layers):')
    print(f'    Max: {max(penAccuracy)}')
    print(f'    Avg: {average(penAccuracy)}')
    print(f'    Std: {stDeviation(penAccuracy)}')
    print('---------------------------------------')
    print(f'Car Accuracy Data ({hiddenLayers[1]} layers):')
    print(f'    Max: {max(carAccuracy)}')
    print(f'    Avg: {average(carAccuracy)}')
    print(f'    Std: {stDeviation(carAccuracy)}')


if __name__ == '__main__':
    layers = [[i for i in range(0, 45, 5)], [i for i in range(0, 45, 5)]]

    for i in range(len(layers[0])):
        Q5([layers[0][i], layers[1][i]])