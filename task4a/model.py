import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, log_loss, classification_report
import tensorflow as tf
from tqdm import tqdm
import matplotlib.pyplot as plt


class generate_samples(object):
  """ Generate the train and test samples"""

  def __init__(self):
    self.plain_train_file = 'train_plain.txt'
    self.cipher_train_file = 'train_cipher.txt'
    self.plain_test_file = 'test_plain.txt'
    self.cipher_test_file = 'test_cipher.txt'
    with open(self.plain_train_file, "r") as plain_text:
      self.plain_train_data = plain_text.read()
    with open(self.cipher_train_file, "r") as cipher_text:
      self.cipher_train_data = cipher_text.read()
    with open(self.plain_test_file, "r") as plain_text:
      self.plain_test_data = plain_text.read()
    with open(self.cipher_test_file, "r") as cipher_text:
      self.cipher_test_data = cipher_text.read()
    """ The train x dataset consists of 304 samples of cipher text each having frequency count of characters and the train y dataset 
    consists of 305 samples of one hot encoded vector for the two cryptograms. The test dataset consists of 20 samples each"""
    self.train_data_x = np.zeros((305, 26))
    self.train_data_y = np.zeros((305, 2))
    self.test_data_x = np.zeros((20, 26))
    self.test_data_y = np.zeros((20, 2))
    self.train_data_y[152:, 1] = 1
    self.train_data_y[:152, 0] = 1
    self.test_data_y[10:, 1] = 1
    self.test_data_y[0:10, 0] = 1

  def generate_data(self, cipher_data, flag):
    """ Arguments:
        cipher_text, flag to determine test and train dataset
        Computes the frequency count of each character in both train and test dataset"""
    sample_count, char_count = 0, 0
    for c in cipher_data:
      if char_count == 200:
        sample_count += 1
        char_count = 0
      if ord(c) == 32:
        char_count += 1
        continue
      elif ord(c) >= 65 and ord(c) <= 90:
        if flag == True:
          self.train_data_x[sample_count][ord(c) - ord('A')] += 1
        else:
          self.test_data_x[sample_count][ord(c) - ord('A')] += 1
        char_count += 1

  def get_train_data(self):
    return self.train_data_x, self.train_data_y

  def get_test_data(self):
    return self.test_data_x, self.test_data_y

  def get_cipher_text(self):
    return self.cipher_train_data, self.cipher_test_data


class models(object):
  """Class containing SVM and BPNN model"""

  def svm(self, X_train, Y_train, X_test, Y_test):
    """Arguments: X_train, Y_train: Training dataset
                  X_test, Y_test: Testing dataset"""
    scores = []
    kf = KFold(n_splits=5, shuffle=True)
    accuracy = []
    # KFold validation
    for i in range(2):
      Y = Y_train[:, i]
      for train_index, test_index in kf.split(X_train):
        x_train, x_test = X_train[train_index], X_train[test_index]
        y_train, y_test = Y[train_index], Y[test_index]
        clf = SVC(
            random_state=42, probability=True, kernel='rbf').fit(
                x_train, y_train)
        pred_train = clf.predict(x_train)
        # Logarithmic loss
        train_loss = log_loss(y_train, pred_train)
        pred_test = clf.predict(x_test)
        test_loss = log_loss(y_test, pred_test)
        # Accuracy score as performance metric
        val_acc = accuracy_score(pred_test, y_test)
        accuracy.append(val_acc)
        print("train loss:", train_loss, "validation loss", test_loss)
        print("validation accuracy", val_acc)
        print("Test accuracy",
              accuracy_score(clf.predict(X_test), (Y_test[:, i])))
    plt.xlabel("steps")
    plt.ylabel("accuracy")
    plt.plot(np.arange(10), accuracy)
    plt.show()

  def neural_network(self, X_train, Y_train, X_test, Y_test):
    """Arguments: X_train, Y_train: Training dataset
                  X_test, Y_test: Testing dataset"""
    with tf.name_scope("input"):
      x = tf.placeholder(tf.float32, [None, 26])
      y_ = tf.placeholder(tf.float32, [None, 2])
      pkeep = tf.placeholder(tf.float32)
      # Fully connected neural network
      with tf.name_scope("weights"):
        w1 = tf.Variable(tf.truncated_normal([26, 50], stddev=0.1))
        b1 = tf.Variable(tf.zeros([50]))
        w2 = tf.Variable(tf.truncated_normal([50, 2], stddev=0.1))
        b2 = tf.Variable(tf.zeros([2]))
      y1 = tf.matmul(x, w1) + b1
      logits = tf.matmul(y1, w2) + b2
      y = tf.nn.sigmoid(logits)
      # Logarithmic loss
      with tf.name_scope("log_loss"):
        loss = tf.reduce_mean(tf.losses.log_loss(y, y_))
        tf.summary.scalar("loss", loss)
      with tf.name_scope("train"):
        train_step = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
      with tf.name_scope("accuracy"):
        is_correct = tf.equal((tf.argmax(y, 1)), (tf.argmax(y_, 1)))
        accuracy = tf.reduce_mean(tf.cast(is_correct, "float"))
        tf.summary.scalar("accuracy", accuracy)
      sess = tf.Session()
      sess.run(tf.global_variables_initializer())
      summary_op = tf.summary.merge_all()
      # Store summaries for tensorboard
      writer = tf.summary.FileWriter("/tmp/logs", graph=sess.graph)
      kf = KFold(n_splits=5, shuffle=True)
      # KFold validaion metrics
      for train_index, test_index in kf.split(X_train):
        for i in tqdm(range(3)):
          x_train, x_test = X_train[train_index], X_train[test_index]
          y_train, y_test = Y_train[train_index], Y_train[test_index]
          sess.run(train_step, feed_dict={x: x_train, y_: y_train, pkeep: 0.75})
          acc = sess.run(
              [accuracy], feed_dict={
                  x: x_train,
                  y_: y_train,
                  pkeep: 0.75
              })
          s = sess.run(
              summary_op, feed_dict={
                  x: x_test,
                  y_: y_test,
                  pkeep: 1.0
              })
          writer.add_summary(s, i)
      pred, accuracy = sess.run(
          [y, accuracy], feed_dict={
              x: X_test,
              y_: Y_test,
              pkeep: 1.0
          })
      print("Accuracy", accuracy)


if __name__ == "__main__":
  generate_samples = generate_samples()
  cipher_train, cipher_test = generate_samples.get_cipher_text()
  generate_samples.generate_data(cipher_train, True)
  generate_samples.generate_data(cipher_test, False)
  train_data_x, train_data_y = generate_samples.get_train_data()
  test_data_x, test_data_y = generate_samples.get_test_data()
  model = models()
  model.svm(train_data_x, train_data_y, test_data_x, test_data_y)
  model.neural_network(train_data_x, train_data_y, test_data_x, test_data_y)
