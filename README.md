# asd_diagnosis_fmri

duck --list s3:/fcp-indi/data/Projects/ABIDE/

aws s3 ls s3://fcp-indi/data/Projects/ABIDE2/RawData/ --no-sign-request

aws s3 cp --recursive s3://fcp-indi/data/Projects/ADHD200/Outputs/cpac/raw_outputs/pipeline_adhd200-benchmark__freq-filter/ ./ --no-sign-request


sudo docker run --rm -u $UID:$UID -v ~/Capstone/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac /wkdir/data/raw/BIDS/ABIDEI /wkdir/data/cpac_output participant --participant_ndx 1 --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline.yml

python download_abide_preproc.py -d rois_cc200 -p cpac -s filt_noglobal -o ./data/ABIDEI_preprocessed/

sudo docker run --rm -u $UID:$UID -v ~/Capstone/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac /wkdir/data/raw/cpac_t /wkdir/data/cpac_output_t participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline.yml

## Running CPAC on AWS EC2 instance
* Need more than 8GB EBS for docker image (150GB)
* Amazon linux c.5.2xlarge
* c3.4xlarge 
1. `sudo yum update -y`
2. `sudo yum install git -y`
1. `git clone https://github.com/Connorpar/asd_diagnosis_fmri.git`
2. `rsync -av -e "ssh -i ~/.aws_creds/cparish_aws.pem" ~/.aws_creds/rootkey.csv ec2-user@ec2-18-225-37-222.us-east-2.compute.amazonaws.com:~/asd_diagnosis_fmri/`
3. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
4. Pull the latest cpac image using `sudo docker pull fcpindi/c-pac:dev-1.7.2`
5. `sudo docker run --rm -u $UID:$UID -v ~/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac:dev-1.7.2 s3://fcp-indi/data/Projects/ABIDE/RawDataBIDS s3://cpacpreprocessed/abideI_output/ participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline_cloud.yml`

`sudo docker run --cpus="8" --rm -u $UID:$UID -v ~/asd_diagnosis_fmri:/wkdir -v /tmp:/tmp fcpindi/c-pac:dev-1.7.2 s3://fcp-indi/data/Projects/ABIDE/RawDataBIDS/Stanford s3://cpacpreprocessed/abideI_output_Stanford/ participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline_cloud.yml --n_cpus 8 --mem_gb 15`

`sudo docker run --cpus="8" --rm -u $UID:$UID -v ~/asd_diagnosis_fmri:/wkdir -v /tmp:/tmp fcpindi/c-pac:dev-1.7.2 s3://fcp-indi/data/Projects/ABIDE2/RawData/ABIDEII-GU_1 s3://cpacpreprocessed/abideII_output_GU/ participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline_cloud.yml --n_cpus 8 --mem_gb 15`

# Errors
* NYU_2: FATAL ERROR:[0m tpattern file /tmp/resting_preproc_sub-29155_ses-1/_scan_rest_run-1/scan_params_0/tpattern.txt has 33 values but have 34 slices
* USM need sub-29526/ and sub-29527/