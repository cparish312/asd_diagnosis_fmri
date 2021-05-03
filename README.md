# asd_diagnosis_fmri

## Running CPAC on AWS EC2 instance
* Need more than 8GB EBS for docker image (150GB)
* Amazon linux c.5.2xlarge
* c3.4xlarge 
1. `sudo yum update -y`
2. `sudo yum install git -y`
3. `git clone https://github.com/Connorpar/asd_diagnosis_fmri.git`
4. `rsync -av -e "ssh -i ~/.aws_creds/cparish_aws.pem" ~/.aws_creds/rootkey.csv ec2-user@ec2-18-225-37-222.us-east-2.compute.amazonaws.com:~/asd_diagnosis_fmri/`
5. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
6. Pull the latest cpac image using `sudo docker pull fcpindi/c-pac:dev-1.7.2`
7. `sudo docker run --rm -u $UID:$UID -v ~/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac:dev-1.7.2 s3://fcp-indi/data/Projects/ABIDE/RawDataBIDS s3://cpacpreprocessed/abideI_output/ participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline_cloud.yml`

## Runnin ASD Class training
* notebooks/Subject_Generator.ipynb : Create Subject objects
* notebooks/Data_generator.ipynb : Generate Datasets for training using Subjects
* notebooks/colab/ASD_class_pure.ipynb : LSTM and Transformer training without pre-training
* notebooks/colab/rs_fMRI_transfomer_pretraining_total.ipynb : Transfomer multi-task and pre-training

# Data Sources
* s3://fcp-indi/data/Projects/ADHD200/Outputs/cpac/raw_outputs/pipeline_adhd200-benchmark__freq-filter/
* s3://fcp-indi/data/Projects/ACPI/Outputs/ants_s1_g0/


# Errors
* NYU_2: FATAL ERROR:[0m tpattern file /tmp/resting_preproc_sub-29155_ses-1/_scan_rest_run-1/scan_params_0/tpattern.txt has 33 values but have 34 slices
