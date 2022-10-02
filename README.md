# gcp-functions-cronJob

conda create -n gcp_ad_network python=3.8  
pip install functions-framework 
pip list --format=freeze > requirements.txt
CURRENCY_TABLE='dreamcaseemin.case_study.daily_currency_rate_dev' GOOGLE_APPLICATION_CREDENTIALS='/Users/limon/Documents/personal_workspace/case_study/gcp-functions-cronJob/dreamcaseemin-984e8be7fab6.json' functions-framework --target http_currency_updater --debug 
