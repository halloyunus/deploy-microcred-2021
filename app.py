from flask import Flask, render_template, request
import pickle
import numpy as np


# app = Flask(__name__)

# model_file = open("knn_model", "rb")
# model = pickle.load(model_file, encoding="bytes")


# @app.route("/")
# def index():
#     return render_template("index.html", STATUS_KELULUSAN=0)


# @app.route("/predict", methods=["POST"])
# def predict():
# """
# Predict the insurance cost based on user inputs
# and render the result to the html page
# """
# # age, sex, smoker = [x for x in request.form.values()]
# nama, status, ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8 = [x for x in request.form.values()]

# datas = []
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":

        with open("KNN_MODEL.pkl", "rb") as r:
            model = pickle.load(r)

        status = request.form["status"]
        if status == "Bekerja":
            status = 0
        else:
            status = 1

        ip1 = float(request.form["ip1"])
        ip2 = float(request.form["ip2"])
        ip3 = float(request.form["ip3"])
        ip4 = float(request.form["ip4"])
        ip5 = float(request.form["ip5"])
        ip6 = float(request.form["ip6"])
        ip7 = float(request.form["ip7"])
        ip8 = float(request.form["ip8"])
        ipk = float(request.form["ipk"])

        datas = np.array((ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ipk))
        datas = np.reshape(datas, (1, -1))

        pred = model.predict(datas)

        if pred == 1:
            return render_template(
                "index.html", status=status, ipk=ipk, pred="TERLAMBAT"
            )
        else:
            return render_template("index.html", status=status, ipk=ipk, pred="TEPAT")
        return render_template("index.html")
    #     return render_template(
    #         "index.html",
    #         STATUS_KELULUSAN=output,
    #         status=status,
    #         ip1=ip1,
    #         ip2=ip2,
    #         ip3=ip3,
    #         ip4=ip4,
    #         ip5=ip5,
    #         ip6=ip6,
    #         ip7=ip7,
    #         ip8=ip8,
    #
    #     )


if __name__ == "__main__":
    app.run(debug=True)
