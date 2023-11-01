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
                    - Qustion: How to define small datasets in PatchTST's perspective? 
                        - The dataset PatchTST used is Electricity (26k rows), Weather (52k rows), traffic (17k rows), ETTh1 and ETTh2 (17k rows). Len=20k is a threshold for defining big/small dataset. 
            - details: 
                - Pyraformer: DataLoader: line139 - the orignal code has wrong time encoding frequency. Should be h instead of m 
        - metircs: mse and mae 
    - Pred piece of data using the trained model 
        - Data to collect: 
            - plot pred and true 
            - record pred time
10. Tests run on BTC data
    <table>
    <tr>
        <td>Model</td>
        <td>input size - output size</td>
        <td>data type</td>
    </tr>
    <tr>
        <td rowspan="4">Transformer</td>
        <td rowspan="4">96-336</td>
        <td>daily data</td>
    </tr>
    <tr>
        <td>1hr data</td>
    </tr>
    <tr>
        <td>30min data</td>
    </tr>
    <tr>
        <td>5min data</td>
    </tr>
    <tr>
        <td rowspan="4">Informer</td>
        <td rowspan="4">96-336</td>
        <td>daily data</td>
    </tr>
    <tr>
        <td>1hr data</td>
    </tr>
    <tr>
        <td>30min data</td>
    </tr>
    <tr>
        <td>5min data</td>
    </tr>
    <tr>
        <td rowspan="4">Autoformer</td>
        <td rowspan="4">96-336</td>
        <td>daily data</td>
    </tr>
    <tr>
        <td>1hr data</td>
    </tr>
    <tr>
        <td>30min data</td>
    </tr>
    <tr>
        <td>5min data</td>
    </tr>
    <tr>
        <td rowspan="4">Reformer</td>
        <td rowspan="4">96-336</td>
        <td>daily data</td>
    </tr>
    <tr>
        <td>1hr data</td>
    </tr>
    <tr>
        <td>30min data</td>
    </tr>
    <tr>
        <td>5min data</td>
    </tr>
    <tr>
        <td rowspan="4">PatchTST</td>
        <td rowspan="4">96-336</td>
        <td>daily data</td>
    </tr>
    <tr>
        <td>1hr data</td>
    </tr>
    <tr>
        <td>30min data</td>
    </tr>
    <tr>
        <td>5min data</td>
    </tr>
    </table>

## Next after Oct meet up: 
1. More model runs: 
    - Follow the other Former papers to do the following runs: 
        - look-back window & forecasting horizon: <b> 96: 96, 192, 336, 720 </b>
    - Pick a TS length for running the test for 1min data: <b> pick a date range and then use the date range to trunck the dataset </b>
        - The full 1min dataset is too expensive to test on.  1 run cost more than 24hrs and 400euros on AWS. 
        - Tried to pick the lastest 20k rows of datasets for all the datasets. The coefficient of variation (CV) value shows that 5min dataset is less volatie than 30min dataset. So simply picking the latest x number of rows of data can not reflect the real volatieties in the datasets. 
        - Date range picked: 
            <br> Date range: 2019-12-04 - 2023-05-07 </br>
            <table>
                <tr>
                    <td>Data Type</td>
                    <td>Data Length</td>
                    <td>Coefficient of Variantion</td>
                </tr>
                <tr>
                    <td>1hr</td>
                    <td>30,000</td>
                    <td>0.5867397316818509</td>
                </tr>
                <tr>
                    <td>30min</td>
                    <td>59,995</td>
                    <td>0.5874570516249259</td>
                </tr>
                <tr>
                    <td>5min</td>
                    <td>359,961</td>
                    <td>0.5874634333005645</td>
                </tr>
                <tr>
                    <td>1min</td>
                    <td>1,799,669</td>
                    <td>0.587479701609147</td>
                </tr>
            </table>

            <br> Date range: 2021-01-24 - 2023-05-07 </br>
            <table>
                <tr>
                    <td>Data Type</td>
                    <td>Data Length</td>
                    <td>Coefficient of Variantion</td>
                </tr>
                <tr>
                    <td>1hr</td>
                    <td>20,000</td>
                    <td>0.38709920725934677</td>
                </tr>
                <tr>
                    <td>30min</td>
                    <td>39,998</td>
                    <td>0.3871035153233582</td>
                </tr>
                <tr>
                    <td>5min</td>
                    <td>239,974</td>
                    <td>0.38709531593582147</td>
                </tr>
                <tr>
                    <td>1min</td>
                    <td>1,199,730</td>
                    <td>0.3870864315034914</td>
                </tr>
            </table>
    - What measurement can be used to tell how volatile a dataset is? coefficient of variation (CV) 
        
2. Answer the questions: 
    - why PatchTST stop performing better in more granular data - more noise in more granular dataset
3. Models & Methods that can be used to imporve the Former models: 
    - In the existing Transformer variants, which ones are using Fourier Transform, Discrete Fourier Transform or Wavelet Transform? - FedFormer has applied Discrete Fourier Transform. 
    - < A Multi-Scale Decomposition MLP-Mixer for Time Series Analysis >: Patch TST in different scales https://wx.zsxq.com/dweb2/index/topic_detail/211225181441511
    - < Blockchain Transaction Fee Forecasting: A Comparison of Machine Learning Methods > - Wavelet to decompose the data; wavelet figures are of interest and can go in the paper.
    - < Analysis of Cryptocurrency Commodities with Motifs and LSTM > - Motif to find small repeat patterns in data
