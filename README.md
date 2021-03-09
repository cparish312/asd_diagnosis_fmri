# asd_diagnosis_fmri

duck --list s3:/fcp-indi/data/Projects/ABIDE/


sudo docker run --rm -u $UID:$UID -v ~/Capstone/asd_diagnosis_fmri:/wkdir -v /tmp:/scratch fcpindi/c-pac /wkdir/data/raw/BIDS/ABIDEI /wkdir/data/cpac_output participant --participant_ndx 1 --pipeline_file /wkdir/cpac_configs/settings/abide_cpac_pipeline.yml

python download_abide_preproc.py -d rois_cc200 -p cpac -s filt_noglobal -o ./data/ABIDEI_preprocessed/