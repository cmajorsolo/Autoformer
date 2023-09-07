## Steps
1. Save the trained model into S3 bucket  
    - Done by adding sm-model-dir in the parameter in run.py
2. Use GPU to train 
    - Done by changing the estimator attribute to: instance_type = "ml.p3.2xlarge", #Type of EC2 instance with GPU needed for training
3. Print out the test charts
    - Done by updating folder_path params in exp_main.py
4. Get BTC data running with Autoformer
    - Done by fixing params like enc_in, dec_in, c_out in run.py
5. Set up early stop on epochs
    - Done by set up patience in run.py
6. Draw charts for test
    - Done by adding code in exp_main.py->predict(). See commit 'adding prediction chart'
7. Read the publish paper to find out more evaluation ways of a model 
    - Read my report again to find out the categorized models; find the latest models
8. Test out the other 3 models 

