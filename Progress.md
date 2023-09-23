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
        - PatchTST, Autoformer, Informer, Reformer and Pyraformer is selected
8. Test out the models with dummy btc data
    - PatchTST    2023 --- Done 
    - Autoformer  2022 --- Done
    - Informer    2021 --- Done
    - Reformer    2021 --- Done
    - Pyraformer  2022 --- A lot of rework need to be done on this model; leave it for now
    - Transformer 2017 --- Done 
9. Overall test steps: 
    - Train the model with the best params for each model 
        - metircs: mse and mae 
        - Tunning: 
            - params: 
                - what params should be applied on the BTC datasets? 
                    | Parameter | Autoformer | PatchTST |
                    |---------|---------|---------|
                    | Input/Output Data| 96 - [96, 192, 336, 720]| 336 - 96|
                    | Batch Size| 32| Unknown|
                    | Loss| L2| Unknown|
                    | Optimizer| Adam| Unknown|
                    | Activation| Unknown| GELU|
                    | Early stop| 10| Unknown|
                    | Encoder Layer| Unknown| 3|
                    | Head number| Unknown| 16|
                    | D latent space| Unknown| 128|
                    | dropout| Unknown| 0.2|
                    | patch length| Unknown| [8, 16]|
                    
                    PatchTST: for a very small datasets (ILI, ETTh1, ETTh2), a reduced size of parameters is used (H = 4, D = 16 and F = 128) to mitigate the possible overfitting
                - Qustion: How to define small datasets here? 
                - shoudl the params be different depends on the granuarity of the data? 
            - details: 
                - Pyraformer: DataLoader: line139 - the orignal code has wrong time encoding frequency. Should be h instead of m 

    - Pred piece of data using the trained model 
        - Data to collect: 
            - plot pred and true 
            - record pred time


