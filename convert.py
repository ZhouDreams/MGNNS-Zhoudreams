from gensim.scripts.glove2word2vec import glove2word2vec


def transfer(gloveFile, word2vecFile):
    glove2word2vec(gloveFile, word2vecFile)


if __name__ == '__main__':
    transfer('data/glove/glove.6B.300d.txt', 'data/glove_300d_w2v_format.txt')