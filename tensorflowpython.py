import tensorflow as tf
tf.compat.v1.disable_eager_execution()
tf.executing_eagerly()

ones_tensor = tf.ones([2,3], tf.int32)

with tf.compat.v1.Session() as sess:
    print(sess.run(ones_tensor))

