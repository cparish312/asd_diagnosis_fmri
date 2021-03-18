# asd_diagnosis_fmri

duck --list s3:/fcp-indi/data/Projects/ABIDE/


sudo docker run --rm -u $UID:$UID -v ~/Capstone/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac /wkdir/data/raw/BIDS/ABIDEI /wkdir/data/cpac_output participant --participant_ndx 1 --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline.yml

python download_abide_preproc.py -d rois_cc200 -p cpac -s filt_noglobal -o ./data/ABIDEI_preprocessed/

sudo docker run --rm -u $UID:$UID -v ~/Capstone/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac /wkdir/data/raw/cpac_t /wkdir/data/cpac_output_t participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline.yml

## Running CPAC on AWS EC2 instance
* Need more than 8GB EBS for docker image
1. `git clone https://github.com/Connorpar/asd_diagnosis_fmri.git`
2. `rsync -av -e "ssh -i ~/.aws_creds/cparish_aws.pem" ~/.aws_creds/rootkey.csv ec2-user@ec2-18-225-37-222.us-east-2.compute.amazonaws.com:~/asd_diagnosis_fmri/`
3. Install Docker using https://docs.docker.com/engine/install/ubuntu/
4. Pull the latest cpac image using `docker pull fcpindi/c-pac`
5. `sudo docker run --rm -u $UID:$UID -v ~/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac s3://fcp-indi/data/Projects/ABIDE/RawDataBids s3://cpacpreprocessed/abideI_output/output participant --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline_cloud.yml`