import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

model_name = "model-1615052292"


def content_graph(model_name):
    contents = open("model.log", "r").read().split('\n')

    time = []
    accu = []
    losses = []
    val_accu = []
    val_losses = []

    for c in contents:
        if model_name in c:
            name, timestamp, acc, loss, val_acc, val_loss = c.split(",")

            time.append(float(timestamp))
            accu.append(float(acc))
            losses.append(float(loss))

            val_accu.append(float(val_acc))
            val_losses.append(float(val_loss))

    fig = plt.figure

    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

    ax1.plot(time, accu, Label="Accuracy")
    ax1.plot(time, val_accu, Label="Val_Accuracy")
    ax1.legend(loc=2)

    ax2.plot(time, losses, Label="Loss")
    ax2.plot(time, val_losses, Label="Val_Loss")
    ax2.legend(loc=2)

    plt.show()

    # plt.plot(time, accu)
    # plt.show()

    # plt.plot(time, val_accu)
    # plt.show()


content_graph(model_name)
