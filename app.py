# Import SQL Alchemy `automap`, Flask, custom function and other dependencies.
from sqlalchemy import create_engine, MetaData, desc
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify, render_template

# Import and establish Base for which classes will be constructed
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float, inspect

import numpy as np

#import custom functions
#from get_sample_cols import return_sample_names

app = Flask(__name__)

# Create a connection to a SQLite database
engine = create_engine('sqlite:///Datasets/belly_button_biodiversity.sqlite', echo=False)

# Create a connection to the engine called `conn`
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Otu = Base.classes.otu
Samples = Base.classes.samples
Samples_metadata = Base.classes.samples_metadata

#create session (link) from Python to the DB
session = Session(engine)

@app.route("/")
def home():
    return render_template("index.html")
    #return(
    #f"Available Routes:<br/>"
    #f"/names<br/>"
    #f"/otu<br/>"
    #f"/metadata/<sample></br>"
    #f"/wfreq/<sample></br>"
    #f"/samples/<sample>"
    #)
	#return render_template("index.html")


@app.route("/names")
def names():
    sample_names = Samples.__table__.columns
    sample_names_ls = [name.key for name in sample_names]
    sample_names_ls.remove("otu_id")
    return jsonify(sample_names_ls)
    #return render_template("index.html", selDataset=sample_names_ls)

@app.route("/otu")
def otu():
    otu_descriptions = session.query(Otu.lowest_taxonomic_unit_found).all()
    otu_descriptions_list = [x for (x), in otu_descriptions]
    return jsonify(otu_descriptions_list)


@app.route("/otu_descriptions")
def otu_disc():
    otu_descriptions = session.query(Otu.otu_id, Otu.lowest_taxonomic_unit_found).all()
    otu_dict = {}
    for row in otu_descriptions:
        otu_dict[row[0]] = row[1]
    return jsonify(otu_dict)

@app.route("/metadata/<sample>")
def sample_query(sample):
    sample_name = sample.replace("BB_", "")
    result = session.query(Samples_metadata.AGE, Samples_metadata.BBTYPE, Samples_metadata.ETHNICITY,
                           Samples_metadata.GENDER, Samples_metadata.LOCATION, Samples_metadata.SAMPLEID).filter_by(
        SAMPLEID=sample_name).all()
    print(result)
    record = result[0]
    record_dict = {
        "AGE": record[0],
        "BBTYPE": record[1],
        "ETHNICITY": record[2],
        "GENDER": record[3],
        "LOCATION": record[4],
        "SAMPLEID": record[5]
    }
    return jsonify(record_dict)


@app.route('/wfreq/<sample>')
def wash_freq(sample):
    sample_name = sample.replace("BB_", "")
    result = session.query(Samples_metadata.WFREQ).filter_by(SAMPLEID=sample_name).all()
    print(result)
    wash_freq = result[0][0]
    return jsonify(wash_freq)


@app.route('/samples/<sample>')
def get_sample_value(sample):
    otu_ids = []
    sample_values = []
    samples_result = {}

    my_query = "Samples." + sample  # eg. 'Samples.BB_940'
    print(my_query)
    query_result = session.query(Samples.otu_id, my_query).order_by(desc(my_query)).limit(10)

    for result in query_result:
        otu_ids.append(result[0])
        sample_values.append(result[1])

    # Add the above lists to the dictionary
    samples_result = {
        "otu_ids": otu_ids,
        "sample_values": sample_values
    }
    return jsonify(samples_result)


if __name__ == '__main__':
    app.run(debug=False)

