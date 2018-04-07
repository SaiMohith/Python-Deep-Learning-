import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data  # import MNIST Data
mnist_data = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Placeholders for graph
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# Set model weights
Weights = tf.Variable(tf.zeros([784, 10]))
bias = tf.Variable(tf.zeros([10]))

# Construct model
y_pred = tf.nn.softmax(tf.matmul(x, Weights) + bias)

# cross entropy to minimize error
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(y_pred), reduction_indices=1))

# Hyper Parameters
learning_rate = 0.1
epochs = 40

# Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Start training
with tf.Session() as sess:
    # Run the Global Initializer to initialize all the values
    sess.run(tf.global_variables_initializer())
    # Write the graph in the log_reg directory
    writer = tf.summary.FileWriter('./graphs/log_reg', sess.graph)
    # Start training cycle
    for epoch in range(epochs):
        AverageCost = 0.
        Batch_tot = int(mnist_data.train.num_examples/100)
        # This loops over all batches
        for i in range(Batch_tot):
            batch_xs, batch_ys = mnist_data.train.next_batch(batch_size=100)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs, y: batch_ys})
            # Compute average loss
            AverageCost += c / Batch_tot
        # Display logs per epoch step
        if (epoch+1) % 1 == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(AverageCost))

    writer.close()
    w, b = sess.run([Weights, bias])

    # Run the test model
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))

    # Calculate accuracy
    accu = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accu.eval({x: mnist_data.test.images, y: mnist_data.test.labels}))
