import sys
import fire

import preprocess
import modeling
import evaluate


def features():
    """ Split data, clean, generate, preprocess and save features (listings_train.csv and listings_test.csv) """
	pass


def deploy_model():
    """ Load features, train model, finalize model and save model """
    # Preprocess Step
    pass


def evaluate_model():
    """ Load the model, load test data (unseen), evaluate model and save metrics """
    pass


def run(**kwargs):
	""" To run the complete pipeline. 
	
		Execute:
    	$ python main.py
    """
    print("Args: {}".format(kwargs))
    
    features(**kwargs) # generate dataset for training
    deploy_model(**kwargs) # deploy model and save to filesystem
    evaluate_model(**kwargs) # evaluate model and save to filesystem


def cli():
    """ Caller to transform module in a low-level CLI """
    return fire.Fire()


if __name__ == '__main__':
    cli()
