import pickle


def import_classifier():
    f = open('classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier


def main():
    classifier = import_classifier()


if __name__ == '__main__':
    main()
